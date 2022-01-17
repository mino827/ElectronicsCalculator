import unittest

from ElectronicsCalculator import electronics_calculator as ec


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

    def test_voltage_divider_r(self):
        self.assertEqual(round(ec.voltage_divider_r(5.0, 1000.0, 2000.0), 2), 3.33)
        self.assertEqual(round(ec.voltage_divider_r(5.0, 0, 0), 2), 0)

    def test_total_series_current(self):
        self.assertEqual(round(ec.total_series_current((2.0, 2.0, 3.0, 2.0)), 2), 0)

    def test_total_series_resistance(self):
        self.assertEqual(round(ec.total_series_resistance((1000.0, 2000.0, 3000.0, 4000.0)), 2), 10000.0)

    def test_total_series_voltage(self):
        self.assertEqual(round(ec.total_series_voltage((3.0, 2.0, 3.0, 4.0)), 2), 12.0)

    def test_total_series_capacitance(self):
        self.assertEqual(ec.total_series_capacitance((0.000001, 0.0000047, 0.0000000004)
                                                     ), 3.9980605153244808901213879224546e-10)
        self.assertEqual(ec.total_series_capacitance((0.000001, 0, 0.0000000004)), 0)

    def test_total_series_inductance(self):
        self.assertEqual(ec.total_series_inductance((0.0001, 0.0047, 0.0003)), 0.0051)

    def test_total_parallel_current(self):
        self.assertEqual(ec.total_parallel_current((1.0, 0.002, 0.025, 0.0002)), 1.0272)

    def test_total_parallel_resistance(self):
        self.assertEqual(round(ec.total_parallel_resistance((1000.0, 2000.0, 3000.0, 4000.0)), 2), 480.0)
        self.assertEqual(round(ec.total_parallel_resistance((1000.0, 2000.0, 0, 4000.0)), 2), 0)

    def test_total_parallel_voltage(self):
        self.assertEqual(round(ec.total_parallel_voltage((7.5, 7.5, 7.5, 7.5)), 2), 7.5)
        self.assertEqual(round(ec.total_parallel_voltage((12.0, 9.0, 3.0, 7.5)), 2), 0)

    def test_total_parallel_capacitance(self):
        self.assertEqual(ec.total_parallel_capacitance((0.000004, 0.000003, 0.000002, 0.000001)), 0.00001)

    def test_total_parallel_inductance(self):
        self.assertEqual(round(ec.total_parallel_inductance((0.004, 0.003, 0.002, 0.001)), 5), 0.00048)
        self.assertEqual(round(ec.total_parallel_inductance((0.004, 0, 0.002, 0.001)), 5), 0)

    def test_frequency_cxc(self):
        self.assertEqual(round(ec.frequency_cxc(0.0000001, 1591.55), 2), 1000.00)
        self.assertEqual(round(ec.frequency_cxc(0, 1591.55), 2), 0)

    def test_capacitance_fxc(self):
        self.assertEqual(round(ec.capacitance_fxc(1.0, 100.00), 4), 0.0016)
        self.assertEqual(round(ec.capacitance_fxc(1.0, 0), 4), 0)

    def test_reactance_capacitive_fc(self):
        self.assertEqual(round(ec.reactance_capacitive_fc(1000, 0.0000001), 2), 1591.55)

    def test_reactance_capacitive_zr(self):
        self.assertEqual(round(ec.reactance_capacitive_zr(25.0, 22.91), 2), 10.01)

    def test_frequency_lxl(self):
        self.assertEqual(round(ec.frequency_lxl(0.001, 6.28319), 2), 1000.00)
        self.assertEqual(round(ec.frequency_lxl(0, 6.28319), 2), 0)

    def test_inductance_fxl(self):
        self.assertEqual(round(ec.inductance_fxl(1000.0, 6.28319), 3), 0.001)
        self.assertEqual(round(ec.inductance_fxl(0, 6.28319), 3), 0)

    def test_reactance_inductive_fl(self):
        self.assertEqual(round(ec.reactance_inductive_fl(1000, 0.001), 5), 6.28319)

    def test_back_emf(self):
        self.assertEqual(round(ec.back_emf(0.2, 2.0, 0.0, 0.01), 2), 40.00)
        self.assertEqual(round(ec.back_emf(0.2, 2.0, 0.0, 0), 2), 0)

    def test_wavelength(self):
        self.assertEqual(round(ec.wavelength(2400000), 2), 125.00)
        self.assertEqual(round(ec.wavelength(0), 2), 0)

    def test_frequency_wl(self):
        self.assertEqual(round(ec.frequency_wl(125.00), 2), 2400000.00)
        self.assertEqual(round(ec.frequency_wl(0), 2), 0)

    def test_antenna_length_qw(self):
        self.assertEqual(round(ec.antenna_length_qw(2400000), 2), 31.25)
        self.assertEqual(round(ec.antenna_length_qw(0), 2), 0)

    def test_voltage_rms_from_peak(self):
        self.assertEqual(round(ec.voltage_rms_from_peak(339.41), 2), 240.0)

    def test_voltage_rms_from_peak_to_peak(self):
        self.assertEqual(round(ec.voltage_rms_from_peak_to_peak(678.8225), 2), 240.0)

    def test_voltage_rms_from_average(self):
        self.assertEqual(round(ec.voltage_rms_from_average(216.08), 2), 240.0)

    def test_voltage_average_from_peak(self):
        self.assertEqual(round(ec.voltage_average_from_peak(339.41), 2), 216.08)

    def test_voltage_average_from_peak_to_peak(self):
        self.assertEqual(round(ec.voltage_average_from_peak_to_peak(678.82), 2), 216.08)

    def test_voltage_average_from_rms(self):
        self.assertEqual(round(ec.voltage_average_from_rms(240.0), 2), 216.08)

    def test_voltage_peak_from_peak_to_peak(self):
        self.assertEqual(round(ec.voltage_peak_from_peak_to_peak(678.82), 2), 339.41)

    def test_voltage_peak_from_rms(self):
        self.assertEqual(round(ec.voltage_peak_from_rms(240.0), 2), 339.41)

    def test_voltage_peak_from_average(self):
        self.assertEqual(round(ec.voltage_peak_from_average(216.076), 2), 339.41)

    def test_voltage_peak_to_peak_from_average(self):
        self.assertEqual(round(ec.voltage_peak_to_peak_from_average(216.076), 2), 678.82)

    def test_voltage_peak_to_peak_from_rms(self):
        self.assertEqual(round(ec.voltage_peak_to_peak_from_rms(240.0), 2), 678.82)

    def test_voltage_peak_to_peak_from_peak(self):
        self.assertEqual(round(ec.voltage_peak_to_peak_from_peak(339.41), 2), 678.82)

    def test_voltage_divider_c(self):
        self.assertEqual(round(ec.voltage_divider_c(5.0, 3000.0, 2000.0), 2), 3.33)
        self.assertEqual(round(ec.voltage_divider_c(5.0, 0, 2000.0), 2), 0)

    def test_impedance_rc(self):
        self.assertEqual(round(ec.impedance_rc(22.91, 10.01), 2), 25.00)

    def test_impedance_rcl(self):
        self.assertEqual(round(ec.impedance_rcl(25.0, 20.0, 25.0), 2), 25.50)

    def test_impedance_rcl_phase_angle(self):
        self.assertEqual(round(ec.impedance_rcl_phase_angle(25, 20, 25), 2), 11.31)
        self.assertEqual(round(ec.impedance_rcl_phase_angle(0, 20, 25), 2), 0)

    def test_gain(self):
        self.assertEqual(round(ec.gain(2, 4), 2), 2)
        self.assertEqual(round(ec.gain(0, 4), 2), 0)

    def test_gain_db(self):
        self.assertEqual(round(ec.gain_db(2, 4), 2), 6.02)

    def test_gain_db_power(self):
        self.assertEqual(round(ec.gain_db_power(2, 4), 2), 3.01)

    def test__sums(self):
        self.assertEqual(round(ec._sums((2, 4, 6)), 2), 12)

    def test__inverse_sums(self):
        self.assertEqual(round(ec._inverse_sums((2, 4, 6), 'test__inverse_sums'), 2), 1.09)
        self.assertEqual(round(ec._inverse_sums((2, 4, 0), 'test__inverse_sums'), 2), 0)

    def test__tau(self):
        self.assertEqual(round(ec._tau(3, 4), 3), 75.398)

    def test__inverse_tau(self):
        self.assertEqual(round(ec._inverse_tau(3, 4, 'test__inverse_tau'), 3), 0.013)
        self.assertEqual(round(ec._inverse_tau(3, 0, 'test__inverse_tau'), 3), 0)

    def test__error_zero_division(self):
        self.assertEqual(ec._error_zero_division('test__error_zero_division', 'single', 'test'), None)
        self.assertEqual(ec._error_zero_division('test__error_zero_division', 'multiple'), None)
        self.assertEqual(ec._error_zero_division('test__error_zero_division', 'tuple'), None)


if __name__ == '__main__':
    unittest.main()
