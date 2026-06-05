# importy:
from unittest import TestCase
from algoritmus import rule_phase_match, algoritmus


class TestRulePhaseMatch(TestCase):

    # microslovník pre testovanie funkcie rule_phase_match
    item = {
            "number": 2,
            "symbol": "He",
            "name": "Helium",
            "atomic_mass": 4.003,
            "category": "Noble Gas",
            "phase": "Gas",
            "discovered": 1868
    }

    # test, že funkcia rule_phase_match vracia True, keď sa phase of item (Gas) zhoduje s var phase_choice (Gas)
    def test_phase_match(self):
        self.assertTrue(rule_phase_match(self.item, "Gas"))

    # test, že funkcia rule_phase_match vracia False, keď sa phase of item (Gas) NEzhoduje s var phase_choice (Solid)
    def test_phase_mismatch(self):
        self.assertFalse(rule_phase_match(self.item, "Solid"))

    
class TestAlgoritmus(TestCase):
    
    # výrez z JSONu pre testy
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

    # test, že funkcia algoritmus vracia zoznam s prvkami, ktoré odpovedajú fáze "Solid"
    def test_algoritmus_solid(self):
            phase_choice = "Solid"
            returned_filtered_elements = algoritmus(self.zoznam, rule_phase_match, phase_choice)
            self.assertIn(phase_choice, returned_filtered_elements[0]["phase"])

    # test, že funkcia algoritmus vracia zoznam s prvkami, ktoré odpovedajú fáze "Gas"
    def test_algoritmus_gas(self):
            phase_choice = "Gas"
            returned_filtered_elements = algoritmus(self.zoznam, rule_phase_match, phase_choice)
            self.assertIn(phase_choice, returned_filtered_elements[0]["phase"])