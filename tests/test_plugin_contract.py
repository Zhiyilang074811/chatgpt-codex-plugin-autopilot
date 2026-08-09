import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"

class PluginContractTests(unittest.TestCase):
    def test_manifest_declares_standalone_skill_only_plugin(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(data["name"], "chatgpt-codex-plugin-autopilot")
        self.assertEqual(data["version"], "0.1.0")
        self.assertEqual(data["skills"], "./skills/")
        self.assertNotIn("mcpServers", data)
        self.assertNotIn("apps", data)
        self.assertNotIn("hooks", data)

    def test_manifest_uses_final_directory_safe_identity(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        interface = data["interface"]
        self.assertLessEqual(len(interface["displayName"]), 30)
        self.assertLessEqual(len(interface["shortDescription"]), 30)
        self.assertLessEqual(len(interface["developerName"]), 80)
        for key in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL", "supportURL"):
            self.assertTrue(interface[key].startswith("https://"), key)

    def test_required_public_files_exist(self):
        for rel in ("README.md", "PRIVACY.md", "TERMS.md", "SUPPORT.md", "LICENSE", "assets/mark.svg"):
            self.assertTrue((ROOT / rel).is_file(), rel)

if __name__ == "__main__":
    unittest.main()
