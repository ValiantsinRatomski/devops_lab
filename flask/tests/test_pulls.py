from unittest import TestCase
import handlers.pulls as hpulls


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_update_params(self):
        self.assertEqual(hpulls.update_params({"state": "all"}),
                         {"per_page": "100", "state": "all"})
        self.assertEqual(hpulls.update_params({"state": "open"}),
                         {"per_page": "100", "state": "open"})
        self.assertEqual(hpulls.update_params({"state": "closed"}),
                         {"per_page": "100", "state": "closed"})

    def test_get_pulls(self):
        """Test for get_pulls"""
        self.assertIsInstance(hpulls.get_pulls("open"), list)
        self.assertIsInstance(hpulls.get_pulls("closed"), list)
        self.assertIsInstance(hpulls.get_pulls("accepted"), list)
        self.assertIsInstance(hpulls.get_pulls("needs work"), list)

    def tearDown(self):
        """Finish"""
