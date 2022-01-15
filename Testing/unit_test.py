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

    def test_voltage_pi(self):
        self.assertEqual(round(ec.voltage(power=6.0, current=2.0), 2), 3.00)

    def test_voltage_pr(self):
        self.assertEqual(round(ec.voltage(power=6.0, resistance=1.5), 2), 3.00)

    def test_voltage_ir(self):
        self.assertEqual(round(ec.voltage(resistance=1.5, current=2.0), 2), 3.00)

    def test_resistance_pi(self):
        self.assertEqual(round(ec.resistance(power=6.0, current=2.0), 2), 1.5)

    def test_resistance_pe(self):
        self.assertEqual(round(ec.resistance(power=6.0, voltage=3.0), 2), 1.5)

    def test_resistance_ei(self):
        self.assertEqual(round(ec.resistance(voltage=3.0, current=2.0), 2), 1.5)

    def test_total_series_current(self):
        self.assertEqual(round(ec.total_series_current((2.0, 2.0, 2.0, 2.0)), 2), 2.0)

    def test_total_series_resistance(self):
        self.assertEqual(round(ec.total_series_resistance((1000.0, 2000.0, 3000.0, 4000.0)), 2), 10000.0)

    def test_total_series_voltage(self):
        self.assertEqual(round(ec.total_series_voltage((3.0, 2.0, 3.0, 4.0)), 2), 12.0)

    def test_total_series_capacitance(self):
        self.assertEqual(ec.total_series_capacitance((0.000001, 0.0000047, 0.0000000004)), 3.9980605153244808901213879224546e-10)

    def test_total_series_inductance(self):
        self.assertEqual(ec.total_series_inductance((0.0001, 0.0047, 0.0003)), 0.0051)

    def test_total_parallel_current(self):
        self.assertEqual(ec.total_parallel_current((1.0, 0.002, 0.025, 0.0002)), 1.0272)

    def test_total_parallel_resistance(self):
        self.assertEqual(round(ec.total_parallel_resistance((1000.0, 2000.0, 3000.0, 4000.0)), 2), 480.0)

    def test_total_parallel_voltage(self):
        self.assertEqual(round(ec.total_parallel_voltage((12.0, 9.0, 3.0, 7.5)), 2), 7.5)

    def test_total_parallel_capacitance(self):
        self.assertEqual(ec.total_parallel_capacitance((0.000004, 0.000003, 0.000002, 0.000001)), 0.00001)

    def test_total_parallel_inductance(self):
        self.assertEqual(round(ec.total_parallel_inductance((0.004, 0.003, 0.002, 0.001)), 5), 0.00048)

    def test_frequency_from_capacitance(self):
        self.assertEqual(round(ec.frequency_from_capacitance(0.0000001, 1591.55), 2), 1000.00)

    def test_capacitance_from_frequency(self):
        self.assertEqual(round(ec.capacitance_from_frequency(1.0, 100.00), 4), 0.0016)

    def test_reactance_capacitive(self):
        self.assertEqual(round(ec.reactance_capacitive(1000, 0.0000001), 2), 1591.55)

    def test_frequency_from_inductance(self):
        self.assertEqual(round(ec.frequency_from_inductance(0.001, 6.28319), 2), 1000.00)

    def test_inductance_from_frequency(self):
        self.assertEqual(round(ec.inductance_from_frequency(1000.0, 6.28319), 3), 0.001)

    def test_reactance_inductive(self):
        self.assertEqual(round(ec.reactance_inductive(1000, 0.001), 5), 6.28319)

    def test_back_emf(self):
        self.assertEqual(round(ec.back_emf(0.2, 2.0, 0.0, 0.01), 2), 40.00)

if __name__ == '__main__':
    unittest.main()
