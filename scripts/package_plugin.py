#!/usr/bin/env python3
"""Build portable plugin and OpenAI local marketplace releases, without installing."""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
import zipfile

from validate_pack import validate_plugin

# Explicit roots keep personal files, Git state and prior builds out of releases.
RELEASE_FILES = (
    'plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json',
    '.claude-plugin/marketplace.json', 'README.md', 'INSTALL.md', 'LICENSE',
)
RELEASE_DIRS = ('skills', 'scripts', 'tests', 'evals')


def zip_bytes(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return buffer.getvalue()


def build_release(root: Path, output: Path) -> dict[str, Path]:
    root, output = root.resolve(), output.resolve()
    issues = validate_plugin(root)
    if issues:
        raise ValueError('\n'.join(issues))
    files = {}
    paths = [root / name for name in RELEASE_FILES]
    for directory in RELEASE_DIRS:
        paths.extend(path for path in (root / directory).rglob('*')
                     if path.is_file() and path.suffix in ('.md', '.yaml', '.py')
                     and '__pycache__' not in path.parts)
    for path in sorted(paths):
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f'Release source must be a regular file inside the pack: {path}')
        files[path.relative_to(root).as_posix()] = path.read_bytes()
    manifest = json.loads(files['plugin.json'])
    version = manifest['version']
    catalog = {
        'name': 'kopi-local',
        'interface': {'displayName': 'Kopi Local'},
        'plugins': [{
            'name': 'kopi',
            'source': {'source': 'local', 'path': './plugins/kopi'},
            'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'},
            'category': 'Productivity',
        }],
    }
    marketplace_files = {f'plugins/kopi/{name}': content for name, content in files.items()}
    marketplace_files['.agents/plugins/marketplace.json'] = (json.dumps(catalog, indent=2) + '\n').encode()
    marketplace_root = output / f'kopi-openai-{version}'
    plugin_zip = output / f'kopi-{version}.zip'
    marketplace_zip = output / f'kopi-openai-{version}.zip'
    writes = {plugin_zip: zip_bytes(files), marketplace_zip: zip_bytes(marketplace_files)}
    writes.update({marketplace_root / name: content for name, content in marketplace_files.items()})
    # Check everything before writing. Identical rebuilds are safe; changed files
    # require a new version or output directory, never silent replacement.
    for path, content in writes.items():
        if path.is_symlink() or (path.exists() and (not path.is_file() or path.read_bytes() != content)):
            raise FileExistsError(f'Refusing to replace {path}; use a new version or --output directory')
    for path, content in writes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_bytes(content)
    return {'plugin_zip': plugin_zip, 'marketplace_root': marketplace_root, 'marketplace_zip': marketplace_zip}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'dist')
    args = parser.parse_args()
    try:
        result = build_release(Path(__file__).resolve().parents[1], args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Packaging failed: {error}\n')
    for label, path in result.items():
        print(f'{label}: {path}')


if __name__ == '__main__':
    main()
