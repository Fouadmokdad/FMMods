import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_whatsapp_compat import arrays, matches


class CompatibilityAuditTests(unittest.TestCase):
    def test_real_resource_arrays_present(self):
        rules = arrays()
        self.assertIn("supported_versions_wpp", rules)
        self.assertIn("supported_versions_business", rules)

    def test_whatsapp_246_is_not_declared(self):
        self.assertFalse(matches("2.26.46.10", arrays()["supported_versions_wpp"]))

    def test_business_244_is_declared(self):
        self.assertTrue(matches("2.26.44.74", arrays()["supported_versions_business"]))

    def test_version_prefix_boundary(self):
        self.assertTrue(matches("2.26.44.74", ["2.26.44.xx"]))
        self.assertFalse(matches("2.26.440.1", ["2.26.44.xx"]))
        self.assertFalse(matches("2.26.45.1", ["2.26.44.xx"]))


if __name__ == "__main__":
    unittest.main()
