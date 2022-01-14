import unittest
from Code import electronics_calculator as ec


class Test_electronics_calculator(unittest.TestCase):
    def test_power_ie(self):
        self.assertEqual(round(ec.power(current=2.0, voltage=3.0), 2), 6.00)

    def test_power_ir(self):
        self.assertEqual(round(ec.power(current=2.0, resistance=1.5), 2), 6.00)

    def test_power_er(self):
        self.assertEqual(round(ec.power(resistance=1.5, voltage=3.0), 2), 6.00)

    def test_current_pe(self):
        self.assertEqual(round(ec.current(power=6.0, voltage=3.0), 2), 2.00)

    def test_current_pr(self):
        self.assertEqual(round(ec.current(power=6.0, resistance=1.5), 2), 2.00)

    def test_current_er(self):
        self.assertEqual(round(ec.current(resistance=1.5, voltage=3.0), 2), 2.00)

    def test_reactance_capacitive(self):
        self.assertEqual(round(ec.reactance_capacitive(1000, 0.0000001), 2), 1591.55)

    def test_frequency_from_capacitance(self):
        self.assertEqual(round(ec.frequency_from_capacitance(0.0000001, 1591.55), 2), 1000.00)


if __name__ == '__main__':
    unittest.main()
