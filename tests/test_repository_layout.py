from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]


class MacOSRepositoryLayoutTests(unittest.TestCase):
    def test_required_release_files_exist(self):
        required = [
            "README.md",
            "README_EN.md",
            "LICENSE",
            "SECURITY.md",
            ".gitignore",
            ".github/workflows/test.yml",
            "skills/safe-disk-slimmer-macos/SKILL.md",
            "skills/safe-disk-slimmer-macos/agents/openai.yaml",
            "skills/safe-disk-slimmer-macos/references/macos-policy.json",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_skill_frontmatter_has_expected_name(self):
        skill = (ROOT / "skills/safe-disk-slimmer-macos/SKILL.md").read_text("utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertIn("\nname: safe-disk-slimmer-macos\n", skill)

    def test_policy_is_read_only_design(self):
        policy = json.loads(
            (ROOT / "skills/safe-disk-slimmer-macos/references/macos-policy.json").read_text("utf-8")
        )
        self.assertEqual("read_only_design", policy["status"])
        self.assertFalse(policy["supports_deletion"])
        self.assertIn("/System", policy["forbidden_roots"])

    def test_no_cleanup_executor_is_present(self):
        scripts = list((ROOT / "skills/safe-disk-slimmer-macos").rglob("*"))
        forbidden = [path for path in scripts if "execute" in path.name.lower() or "delete" in path.name.lower()]
        self.assertEqual([], forbidden)

    def test_practical_cleanup_scenarios_reference_is_discoverable_and_read_only(self):
        reference = ROOT / "skills/safe-disk-slimmer-macos/references/practical-cleanup-scenarios.md"
        self.assertTrue(reference.is_file())
        text = reference.read_text("utf-8")
        for phrase in ["Docker", "Xcode", "Homebrew", "APFS", "hash", "read-only"]:
            self.assertIn(phrase, text)
        skill = (ROOT / "skills/safe-disk-slimmer-macos/SKILL.md").read_text("utf-8")
        self.assertIn("practical-cleanup-scenarios.md", skill)


if __name__ == "__main__":
    unittest.main()
