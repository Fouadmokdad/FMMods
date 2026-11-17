import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_whatsapp_compat import arrays, matches
from audit_feature_registry import inventory


class CompatibilityAuditTests(unittest.TestCase):
    def test_real_resource_arrays_present(self):
        rules = arrays()
        self.assertIn("supported_versions_wpp", rules)

    def test_whatsapp_246_is_not_declared(self):
        self.assertFalse(matches("2.26.46.10", arrays()["supported_versions_wpp"]))

    def test_upstream_update_checker_disabled(self):
        source = (Path(__file__).resolve().parents[1] /
                  "app/src/main/java/com/wmods/wppenhacer/UpdateChecker.kt").read_text()
        self.assertIn("override fun run() = Unit", source)
        self.assertNotIn("api.github.com/repos/Dev4Mod", source)
        self.assertNotIn("httpClient.newCall", source)

    def test_home_does_not_show_upstream_update_card(self):
        source = (Path(__file__).resolve().parents[1] /
                  "app/src/main/java/com/wmods/wppenhacer/ui/fragments/HomeFragment.kt").read_text()
        self.assertIn("binding.updateCard.visibility = View.GONE", source)
        self.assertNotIn("        checkForUpdates()\n", source)
        self.assertNotIn('Utils.openLink(requireActivity(), "https://t.me/waenhancher")', source)

    def test_registry_inventory_has_unique_sources(self):
        items = inventory()
        self.assertGreater(len(items), 0)
        self.assertEqual(len(items), len({name for name, _ in items}))
        self.assertTrue(all(str(path).endswith(".kt") for _, path in items))

    def test_version_prefix_boundary(self):
        self.assertTrue(matches("2.26.44.74", ["2.26.44.xx"]))
        self.assertFalse(matches("2.26.440.1", ["2.26.44.xx"]))
        self.assertFalse(matches("2.26.45.1", ["2.26.44.xx"]))


if __name__ == "__main__":
    unittest.main()
