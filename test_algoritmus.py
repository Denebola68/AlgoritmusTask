from unittest import TestCase
from algoritmus import rule_phase_match, algoritmus


class TestRulePhaseMatch(TestCase):
    item = {
            "number": 2,
            "symbol": "He",
            "name": "Helium",
            "atomic_mass": 4.003,
            "category": "Noble Gas",
            "phase": "Gas",
            "discovered": 1868
    }
    def test_phase_match(self):
        self.assertTrue(rule_phase_match(self.item, "Gas"))
    
    def test_phase_mismatch(self):
        self.assertFalse(rule_phase_match(self.item, "Solid"))

    
class TestAlgoritmus(TestCase):
    zoznam = {
        "elements": [
    {
      "number": 2,
      "symbol": "He",
      "name": "Helium",
      "atomic_mass": 4.003,
      "category": "Noble Gas",
      "phase": "Gas",
      "discovered": 1868
    },
    {
      "number": 3,
      "symbol": "Li",
      "name": "Lithium",
      "atomic_mass": 6.941,
      "category": "Alkali Metal",
      "phase": "Solid",
      "discovered": 1817
    },
        ]
    }
    def test_algoritmus_solid(self):
            phase_choice = "Solid"
            returned_filtered_elements = algoritmus(self.zoznam, rule_phase_match, phase_choice)
            self.assertIn(phase_choice, returned_filtered_elements[0]["phase"])

    def test_algoritmus_gas(self):
            phase_choice = "Gas"
            returned_filtered_elements = algoritmus(self.zoznam, rule_phase_match, phase_choice)
            self.assertIn(phase_choice, returned_filtered_elements[0]["phase"])