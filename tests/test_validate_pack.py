import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_pack.py"
SPEC = importlib.util.spec_from_file_location("validate_pack", SCRIPT)
validate_pack = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validate_pack)


class ValidateSkillTests(unittest.TestCase):
    def make_skill(self, root: Path, body: str, extra: dict[str, str] | None = None) -> Path:
        skill = root / "sample-skill"
        skill.mkdir()
        (skill / "SKILL.md").write_text(body, encoding="utf-8")
        for relative, content in (extra or {}).items():
            path = skill / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return skill

    def test_detects_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = self.make_skill(Path(directory), "# Sample\n")
            issues = validate_pack.validate_skill(skill)
            self.assertTrue(any("frontmatter" in issue for issue in issues))

    def test_detects_broken_relative_link(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = self.make_skill(
                Path(directory),
                "---\nname: sample-skill\ndescription: Use when testing a sample.\n---\n\n[Missing](references/nope.md)\n",
            )
            issues = validate_pack.validate_skill(skill)
            self.assertTrue(any("broken link" in issue for issue in issues))

    def test_detects_legacy_operating_term(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = self.make_skill(
                Path(directory),
                "---\nname: sample-skill\ndescription: Use when testing a sample.\n---\n\nRun poteto-mode first.\n",
            )
            issues = validate_pack.validate_skill(skill)
            self.assertTrue(any("legacy term" in issue for issue in issues))

    def test_detects_unreferenced_resource(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = self.make_skill(
                Path(directory),
                "---\nname: sample-skill\ndescription: Use when testing a sample.\n---\n\n# Sample\n",
                {"references/orphan.md": "# Orphan\n"},
            )
            issues = validate_pack.validate_skill(skill)
            self.assertTrue(any("unreferenced resource" in issue for issue in issues))


class ValidatePackTests(unittest.TestCase):
    def test_real_pack_is_valid(self):
        root = Path(__file__).parents[1]
        self.assertEqual([], validate_pack.validate_plugin(root))

    def copy_pack(self, directory):
        root = Path(directory) / "kopi-main"
        shutil.copytree(Path(__file__).parents[1], root,
                        ignore=shutil.ignore_patterns(".git", "dist", "__pycache__"))
        return root

    def test_renamed_checkout_is_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual([], validate_pack.validate_plugin(self.copy_pack(directory)))

    def test_missing_portable_manifest_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_pack(directory)
            (root / "plugin.json").unlink(missing_ok=True)
            self.assertTrue(any(f"{root / 'plugin.json'}:" in issue for issue in validate_pack.validate_plugin(root)))

    def test_platform_version_drift_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_pack(directory)
            path = root / ".claude-plugin/plugin.json"
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps({"name": "kopi", "version": "9.0.0"}))
            self.assertTrue(any("version" in issue for issue in validate_pack.validate_plugin(root)))

    def test_non_object_manifest_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.copy_pack(directory)
            (root / ".codex-plugin/plugin.json").write_text('[1]')
            self.assertTrue(any("JSON object" in issue for issue in validate_pack.validate_plugin(root)))


if __name__ == "__main__":
    unittest.main()
