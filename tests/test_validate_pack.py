import importlib.util
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


if __name__ == "__main__":
    unittest.main()
