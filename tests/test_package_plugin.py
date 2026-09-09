import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))


class PackageTests(unittest.TestCase):
    def test_release_is_clean_reproducible_and_self_contained(self):
        from package_plugin import build_release
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            release = build_release(ROOT, output)
            first = release['plugin_zip'].read_bytes()
            self.assertEqual(first, build_release(ROOT, output)['plugin_zip'].read_bytes())
            with zipfile.ZipFile(release['plugin_zip']) as archive:
                names = archive.namelist()
                self.assertIn('plugin.json', names)
                self.assertIn('.claude-plugin/plugin.json', names)
                self.assertEqual(10, sum(name.endswith('/SKILL.md') for name in names))
                self.assertFalse(any('.git/' in name or '__pycache__' in name or name.startswith('dist/') for name in names))
                archive.extractall(output / 'extracted')
            from validate_pack import validate_plugin
            self.assertEqual([], validate_plugin(output / 'extracted'))
            marketplace_root = release['marketplace_root']
            catalog = json.loads((marketplace_root / '.agents/plugins/marketplace.json').read_text())
            entry = catalog['plugins'][0]
            self.assertEqual([], validate_plugin(marketplace_root / entry['source']['path']))
            self.assertEqual('AVAILABLE', entry['policy']['installation'])
            self.assertTrue(release['marketplace_zip'].is_file())

    def test_refuses_to_overwrite_existing_release(self):
        from package_plugin import build_release
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            release = build_release(ROOT, output)
            release['plugin_zip'].write_text('user file')
            with self.assertRaises(FileExistsError):
                build_release(ROOT, output)
            self.assertEqual('user file', release['plugin_zip'].read_text())
