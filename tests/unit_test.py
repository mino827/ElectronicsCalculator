import unittest

from src.ElectronicsCalculator import electronics_calculator as ec


class Test_electronics_calculator(unittest.TestCase):
    def test_power_ie(self):
        self.assertEqual(round(ec.power_ie(2.0, 3.0), 2), 6.00)
        self.assertRaises(TypeError, ec.power_ie, 'a', 12)
        self.assertRaises(TypeError, ec.power_ie, 2)

    def test_power_ir(self):
        self.assertEqual(round(ec.power_ir(2.0, 1.5), 2), 6.00)
        self.assertRaises(TypeError, ec.power_ir, 'a', 12)
        self.assertRaises(TypeError, ec.power_ir, 2)

    def test_power_er(self):
        self.assertEqual(round(ec.power_er(3.0, 1.5), 2), 6.00)
        self.assertRaises(ZeroDivisionError, ec.power_er, 12, 0)
        self.assertRaises(TypeError, ec.power_er, 'a', 12)
        self.assertRaises(TypeError, ec.power_er, 2)

    def test_current_pe(self):
        self.assertEqual(round(ec.current_pe(6.0, 3.0), 2), 2.00)
        self.assertRaises(ZeroDivisionError, ec.current_pe, 12, 0)
        self.assertRaises(TypeError, ec.current_pe, 'a', 12)
        self.assertRaises(TypeError, ec.current_pe, 2)

    def test_current_pr(self):
        self.assertEqual(round(ec.current_pr(6.0, 1.5), 2), 2.00)
        self.assertRaises(ZeroDivisionError, ec.current_pr, 12, 0)
        self.assertRaises(TypeError, ec.current_pr, 'a', 12)
        self.assertRaises(TypeError, ec.current_pr, 2)

    def test_current_er(self):
        self.assertEqual(round(ec.current_er(3.0, 1.5), 2), 2.00)
        self.assertRaises(ZeroDivisionError, ec.current_er, 12, 0)
        self.assertRaises(TypeError, ec.current_er, 'a', 12)
        self.assertRaises(TypeError, ec.current_er, 2)

    def test_voltage_pi(self):
        self.assertEqual(round(ec.voltage_pi(6.0, 2.0), 2), 3.00)
        self.assertRaises(ZeroDivisionError, ec.voltage_pi, 12, 0)
        self.assertRaises(TypeError, ec.voltage_pi, 'a', 12)
        self.assertRaises(TypeError, ec.voltage_pi, 2)

    def test_voltage_pr(self):
        self.assertEqual(round(ec.voltage_pr(6.0, 1.5), 2), 3.00)
        self.assertRaises(TypeError, ec.voltage_pr, 'a', 12)
        self.assertRaises(TypeError, ec.voltage_pr, 2)

    def test_voltage_ir(self):
        self.assertEqual(round(ec.voltage_ir(2.0, 1.5), 2), 3.00)
        self.assertRaises(TypeError, ec.voltage_ir, 'a', 12)
        self.assertRaises(TypeError, ec.voltage_ir, 2)

    def test_resistance_pi(self):
        self.assertEqual(round(ec.resistance_pi(6.0, 2.0), 2), 1.5)
        self.assertRaises(ZeroDivisionError, ec.resistance_pi, 12, 0)
        self.assertRaises(TypeError, ec.resistance_pi, 'a', 12)
        self.assertRaises(TypeError, ec.resistance_pi, 2)

    def test_resistance_pe(self):
        self.assertEqual(round(ec.resistance_pe(6.0, 3.0), 2), 1.5)
        self.assertRaises(ZeroDivisionError, ec.resistance_pe, 0, 12)
        self.assertRaises(TypeError, ec.resistance_pe, 12, 'a')
        self.assertRaises(TypeError, ec.resistance_pe, 2)

    def test_resistance_ie(self):
        self.assertEqual(round(ec.resistance_ie(2.0, 3.0), 2), 1.5)
        self.assertRaises(ZeroDivisionError, ec.resistance_ie, 0, 12)
        self.assertRaises(TypeError, ec.resistance_ie, 12, 'a')
        self.assertRaises(TypeError, ec.resistance_ie, 2)

    def test_resistance_zxc(self):
        self.assertEqual(round(ec.resistance_zxc(25.0, 10.0), 2), 22.91)
        self.assertRaises(TypeError, ec.resistance_ie, 12, 'a')
        self.assertRaises(TypeError, ec.resistance_ie, 2)

    def test_voltage_divider_r(self):
        self.assertEqual(round(ec.voltage_divider_r(5.0, 1000.0, 2000.0), 2), 3.33)
        self.assertRaises(ZeroDivisionError, ec.voltage_divider_r, 5.0, 0, 0)
        self.assertRaises(TypeError, ec.voltage_divider_r, 12, 'a', 500)
        self.assertRaises(TypeError, ec.voltage_divider_r, 2)

    def test_total_series_current(self):
        self.assertEqual(round(ec.total_series_current((2.0, 2.0, 2.0, 2.0)), 2), 2.0)
        self.assertRaises(TypeError, ec.total_series_current, ('a', 'a', 'a', 'a'))
        self.assertRaises(TypeError, ec.total_series_current, 2)
        self.assertRaises(ValueError, ec.total_series_current, (0.004, 0.003, 0.002, 0.001))
        self.assertRaises(IndexError, ec.total_series_current, ())
        self.assertRaises(TypeError, ec.total_series_current, (0.004, 'a', 0.002, 0.001))

    def test_total_series_resistance(self):
        self.assertEqual(round(ec.total_series_resistance((1000.0, 2000.0, 3000.0, 4000.0)), 2), 10000.0)
        self.assertRaises(TypeError, ec.total_series_resistance, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_series_resistance, 2)
        self.assertRaises(ValueError, ec.total_series_resistance, ())

    def test_total_series_voltage(self):
        self.assertEqual(round(ec.total_series_voltage((3.0, 2.0, 3.0, 4.0)), 2), 12.0)
        self.assertRaises(TypeError, ec.total_series_voltage, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_series_voltage, 2)
        self.assertRaises(ValueError, ec.total_series_voltage, ())

    def test_total_series_capacitance(self):
        self.assertEqual(ec.total_series_capacitance((0.000001, 0.0000047, 0.0000000004)
                                                     ), 3.9980605153244808901213879224546e-10)
        self.assertRaises(ZeroDivisionError, ec.total_series_capacitance, (0.000001, 0, 0.0000000004))
        self.assertRaises(TypeError, ec.total_series_capacitance, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_series_capacitance, 2)
        self.assertRaises(ValueError, ec.total_series_capacitance, ())

    def test_total_series_inductance(self):
        self.assertEqual(ec.total_series_inductance((0.0001, 0.0047, 0.0003)), 0.0051)
        self.assertRaises(TypeError, ec.total_series_inductance, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_series_inductance, 2)
        self.assertRaises(ValueError, ec.total_series_inductance, ())

    def test_total_parallel_current(self):
        self.assertEqual(ec.total_parallel_current((1.0, 0.002, 0.025, 0.0002)), 1.0272)
        self.assertRaises(TypeError, ec.total_parallel_current, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_parallel_current, 2)
        self.assertRaises(ValueError, ec.total_parallel_current, ())

    def test_total_parallel_resistance(self):
        self.assertEqual(round(ec.total_parallel_resistance((1000.0, 2000.0, 3000.0, 4000.0)), 2), 480.0)
        self.assertRaises(ZeroDivisionError, ec.total_parallel_resistance, (0.004, 0, 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_parallel_resistance, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_parallel_resistance, 2)
        self.assertRaises(ValueError, ec.total_parallel_resistance, ())

    def test_total_parallel_voltage(self):
        self.assertEqual(round(ec.total_parallel_voltage((7.5, 7.5, 7.5, 7.5)), 2), 7.5)
        self.assertRaises(ValueError, ec.total_parallel_voltage, (12.0, 9.0, 3.0, 7.5))
        self.assertRaises(TypeError, ec.total_parallel_voltage, ('a', 'a', 'a', 'a'))
        self.assertRaises(IndexError, ec.total_parallel_voltage, ())

    def test_total_parallel_capacitance(self):
        self.assertEqual(ec.total_parallel_capacitance((0.000004, 0.000003, 0.000002, 0.000001)), 0.00001)
        self.assertRaises(TypeError, ec.total_parallel_capacitance, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_parallel_capacitance, 2)
        self.assertRaises(ValueError, ec.total_parallel_capacitance, ())

    def test_total_parallel_inductance(self):
        self.assertEqual(round(ec.total_parallel_inductance((0.004, 0.003, 0.002, 0.001)), 5), 0.00048)
        self.assertRaises(ZeroDivisionError, ec.total_parallel_inductance, (0.004, 0, 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_parallel_inductance, (0.004, 'a', 0.002, 0.001))
        self.assertRaises(TypeError, ec.total_parallel_inductance, 2)
        self.assertRaises(ValueError, ec.total_parallel_inductance, ())

    def test_frequency_cxc(self):
        self.assertEqual(round(ec.frequency_cxc(0.0000001, 1591.55), 2), 1000.00)
        self.assertRaises(ZeroDivisionError, ec.frequency_cxc, 0, 2)
        self.assertRaises(ZeroDivisionError, ec.frequency_cxc, 2, 0)
        self.assertRaises(TypeError, ec.frequency_cxc, 2, 'a')
        self.assertRaises(TypeError, ec.frequency_cxc, 2)

    def test_capacitance_fxc(self):
        self.assertEqual(round(ec.capacitance_fxc(1.0, 100.00), 4), 0.0016)
        self.assertRaises(ZeroDivisionError, ec.capacitance_fxc, 0, 2)
        self.assertRaises(ZeroDivisionError, ec.capacitance_fxc, 2, 0)
        self.assertRaises(TypeError, ec.capacitance_fxc, 2, 'a')
        self.assertRaises(TypeError, ec.capacitance_fxc, 2)

    def test_reactance_capacitive_fc(self):
        self.assertEqual(round(ec.reactance_capacitive_fc(1000, 0.0000001), 2), 1591.55)
        self.assertRaises(TypeError, ec.reactance_capacitive_fc, '15x')
        self.assertRaises(ZeroDivisionError, ec.reactance_capacitive_fc, 0, 1000)
        self.assertRaises(ZeroDivisionError, ec.reactance_capacitive_fc, 1000, 0)

    def test_reactance_capacitive_zr(self):
        self.assertEqual(round(ec.reactance_capacitive_zr(25.0, 22.91), 2), 10.01)
        self.assertRaises(TypeError, ec.reactance_capacitive_zr, '15')
        self.assertRaises(TypeError, ec.reactance_capacitive_zr, '15x', 45)

    def test_frequency_lxl(self):
        self.assertEqual(round(ec.frequency_lxl(0.001, 6.28319), 2), 1000.00)
        self.assertRaises(ZeroDivisionError, ec.frequency_lxl, 0, 3000)
        self.assertRaises(TypeError, ec.frequency_lxl, 2, 'a')
        self.assertRaises(TypeError, ec.frequency_lxl, 2)

    def test_inductance_fxl(self):
        self.assertEqual(round(ec.inductance_fxl(1000.0, 6.28319), 3), 0.001)
        self.assertRaises(ZeroDivisionError, ec.inductance_fxl, 0, 3.1415926)
        self.assertRaises(TypeError, ec.inductance_fxl, 2, 'a')
        self.assertRaises(TypeError, ec.inductance_fxl, 2)

    def test_reactance_inductive_fl(self):
        self.assertEqual(round(ec.reactance_inductive_fl(1000, 0.001), 5), 6.28319)
        self.assertRaises(TypeError, ec.reactance_inductive_fl, 2, 'a')
        self.assertRaises(TypeError, ec.reactance_inductive_fl, 2)

    def test_back_emf(self):
        self.assertEqual(round(ec.back_emf(0.2, 2.0, 0.0, 0.01), 2), 40.00)
        self.assertRaises(ZeroDivisionError, ec.back_emf, 0.2, 2.0, 0.0, 0)
        self.assertRaises(TypeError, ec.back_emf, 2, 'a')
        self.assertRaises(TypeError, ec.back_emf, 2)

    def test_wavelength(self):
        self.assertEqual(round(ec.wavelength(2400000), 2), 125.00)
        self.assertRaises(ZeroDivisionError, ec.wavelength, 0)
        self.assertRaises(TypeError, ec.wavelength, '15x')

    def test_frequency_wl(self):
        self.assertEqual(round(ec.frequency_wl(125.00), 2), 2400000.00)
        self.assertRaises(ZeroDivisionError, ec.frequency_wl, 0)
        self.assertRaises(TypeError, ec.frequency_wl, '15x')

    def test_antenna_length_qw(self):
        self.assertEqual(round(ec.antenna_length_qw(2400000), 2), 31.25)
        self.assertRaises(ZeroDivisionError, ec.antenna_length_qw, 0)
        self.assertRaises(TypeError, ec.antenna_length_qw, '15x')

    def test_voltage_rms_from_peak(self):
        self.assertEqual(round(ec.voltage_rms_from_peak(339.41), 2), 240.0)
        self.assertRaises(TypeError, ec.voltage_rms_from_peak, '15x')

    def test_voltage_rms_from_peak_to_peak(self):
        self.assertEqual(round(ec.voltage_rms_from_peak_to_peak(678.8225), 2), 240.0)
        self.assertRaises(TypeError, ec.voltage_rms_from_peak_to_peak, '15a')

    def test_voltage_rms_from_average(self):
        self.assertEqual(round(ec.voltage_rms_from_average(216.08), 2), 240.0)
        self.assertRaises(TypeError, ec.voltage_rms_from_average, '15a')

    def test_voltage_average_from_peak(self):
        self.assertEqual(round(ec.voltage_average_from_peak(339.41), 2), 216.08)
        self.assertRaises(TypeError, ec.voltage_average_from_peak, '15a')

    def test_voltage_average_from_peak_to_peak(self):
        self.assertEqual(round(ec.voltage_average_from_peak_to_peak(678.82), 2), 216.08)
        self.assertRaises(TypeError, ec.voltage_average_from_peak_to_peak, '15a')

    def test_voltage_average_from_rms(self):
        self.assertEqual(round(ec.voltage_average_from_rms(240.0), 2), 216.08)
        self.assertRaises(TypeError, ec.voltage_average_from_rms, '15a')

    def test_voltage_peak_from_peak_to_peak(self):
        self.assertEqual(round(ec.voltage_peak_from_peak_to_peak(678.82), 2), 339.41)
        self.assertRaises(TypeError, ec.voltage_peak_from_peak_to_peak, '15a')

    def test_voltage_peak_from_rms(self):
        self.assertEqual(round(ec.voltage_peak_from_rms(240.0), 2), 339.41)
        self.assertRaises(TypeError, ec.voltage_peak_from_rms, '15a')

    def test_voltage_peak_from_average(self):
        self.assertEqual(round(ec.voltage_peak_from_average(216.076), 2), 339.41)
        self.assertRaises(TypeError, ec.voltage_peak_from_average, '15a')

    def test_voltage_peak_to_peak_from_average(self):
        self.assertEqual(round(ec.voltage_peak_to_peak_from_average(216.076), 2), 678.82)
        self.assertRaises(TypeError, ec.voltage_peak_to_peak_from_average, '15a')

    def test_voltage_peak_to_peak_from_rms(self):
        self.assertEqual(round(ec.voltage_peak_to_peak_from_rms(240.0), 2), 678.82)
        self.assertRaises(TypeError, ec.voltage_peak_to_peak_from_rms, 'a')

    def test_voltage_peak_to_peak_from_peak(self):
        self.assertEqual(round(ec.voltage_peak_to_peak_from_peak(339.41), 2), 678.82)
        self.assertRaises(TypeError, ec.voltage_peak_to_peak_from_peak, 'a')

    def test_voltage_divider_c(self):
        self.assertEqual(round(ec.voltage_divider_c(5.0, 3000.0, 2000.0), 2), 3.33)
        self.assertRaises(ZeroDivisionError, ec.voltage_divider_c, 12, 0, 1000)
        self.assertRaises(TypeError, ec.voltage_divider_c, 12, 2000, 'a')
        self.assertRaises(TypeError, ec.voltage_divider_c, 12, 2000)

    def test_impedance_rc(self):
        self.assertEqual(round(ec.impedance_rc(22.91, 10.01), 2), 25.00)
        self.assertRaises(TypeError, ec.impedance_rc, 2, 'a')
        self.assertRaises(TypeError, ec.impedance_rc, 2)

    def test_impedance_rcl(self):
        self.assertEqual(round(ec.impedance_rcl(25.0, 20.0, 25.0), 2), 25.50)
        self.assertRaises(TypeError, ec.impedance_rcl, 2, 'a', 6)
        self.assertRaises(TypeError, ec.impedance_rcl, 2)

    def test_impedance_rcl_phase_angle(self):
        self.assertEqual(round(ec.impedance_rcl_phase_angle(25, 20, 25), 2), 11.31)
        self.assertRaises(ZeroDivisionError, ec.impedance_rcl_phase_angle, 0, 2, 3)
        self.assertRaises(TypeError, ec.impedance_rcl_phase_angle, 2, 'a', 6)
        self.assertRaises(TypeError, ec.impedance_rcl_phase_angle, 2)

    def test_gain(self):
        self.assertEqual(ec.gain(2, 4), 2)
        self.assertRaises(ZeroDivisionError, ec.gain, 0, 2)
        self.assertRaises(TypeError, ec.gain, 2, 'a')
        self.assertRaises(TypeError, ec.gain, 2)

    def test_gain_db(self):
        self.assertEqual(round(ec.gain_db(2, 4), 2), 6.02)
        self.assertRaises(ZeroDivisionError, ec.gain_db, 0, 2)
        self.assertRaises(TypeError, ec.gain_db, 2, 'a')
        self.assertRaises(TypeError, ec.gain_db, 2)

    def test_gain_db_power(self):
        self.assertEqual(round(ec.gain_db_power(2, 4), 2), 3.01)
        self.assertRaises(ZeroDivisionError, ec.gain_db_power, 0, 2)
        self.assertRaises(TypeError, ec.gain_db_power, 2, 'a')
        self.assertRaises(TypeError, ec.gain_db_power, 2)

    def test__sums(self):
        self.assertEqual(round(ec._sums((2, 4, 6)), 2), 12)
        self.assertRaises(TypeError, ec._sums, ('a', 2, 5))
        self.assertRaises(TypeError, ec._sums, (2, 'a', 5))
        self.assertRaises(TypeError, ec._sums, 2)
        self.assertRaises(ValueError, ec._sums, ())

    def test__inverse_sums(self):
        self.assertEqual(round(ec._inverse_sums((2, 4, 6)), 2), 1.09)
        self.assertRaises(ZeroDivisionError, ec._inverse_sums, (2, 4, 0))
        self.assertRaises(TypeError, ec._inverse_sums, (2, 'a', 5))
        self.assertRaises(TypeError, ec._inverse_sums, 2)

    def test__tau(self):
        self.assertEqual(round(ec._tau(3, 4), 3), 75.398)
        self.assertEqual(ec._tau(0, 4), 0)
        self.assertRaises(TypeError, ec._tau, 2, 'a')
        self.assertRaises(TypeError, ec._tau, 2)

    def test__inverse_tau(self):
        self.assertEqual(round(ec._inverse_tau(3, 4), 3), 0.013)
        self.assertRaises(ZeroDivisionError, ec._inverse_tau, 0, 2)
        self.assertRaises(TypeError, ec._inverse_tau, 2, 'a')
        self.assertRaises(TypeError, ec._inverse_tau, 2)


if __name__ == '__main__':
    unittest.main()
