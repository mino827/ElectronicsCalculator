# ================================= #
# Module: electronics_calculator.py #
# Version: 0.1                      #
# Version date: 2022-01-12          #
# Author: Mino Girimonti            #
# License: GPL v3.0                 #
# ================================= #
"""This module provides methods to perform common electronics calculations."""

import math

# ========= #
# CONSTANTS #
# ========= #
SPEED_OF_LIGHT = 300000000  # Meters per second
PI = math.pi


# ========= #
# OHM'S LAW #
# ========= #
def power(current=0, voltage=0, resistance=0):
    """Calculates power based on any two available values using Ohm's Law. Pass in any two of the three parameters.
    The third (unsupplied) parameter will simply default to a value of 0.

    Inputs:
        current: I (Amperes)
        voltage: V (Volts)
        resistance: R (Ohms)

    Output:
        power: P (Watts)
    """
    retval = 0

    if current != 0 and voltage != 0:
        retval = current * voltage

    elif current != 0 and resistance != 0:
        retval = pow(current, 2) * resistance

    elif voltage != 0 and resistance != 0:
        retval = pow(voltage, 2) / resistance

    return retval


def current(power=0, voltage=0, resistance=0):
    """Calculates current based on any two available values using Ohm's Law. Pass in any two of the three parameters.
    The third (unsupplied) parameter will simply default to a value of 0.

    Inputs:
        power: P (Watts)
        voltage: V (Volts)
        resistance: R (Ohms)

    Output:
        current: I (Amperes)
    """
    retval = 0

    if power != 0 and voltage != 0:
        retval = power / voltage

    elif power != 0 and resistance != 0:
        retval = math.sqrt(power / resistance)

    elif voltage != 0 and resistance != 0:
        retval = voltage / resistance

    return retval


def voltage(power=0, current=0, resistance=0):
    """Calculates voltage based on any two available values using Ohm's Law. Pass in any two of the three parameters.
    The third (unsupplied) parameter will simply default to a value of 0.

    Inputs:
        power: P (Watts)
        current: I (Amperes)
        resistance: R (Ohms)

    Output:
        voltage: V (Volts)
    """
    retval = 0

    if power != 0 and current != 0:
        retval = power / current

    elif power != 0 and resistance != 0:
        retval = math.sqrt(power * resistance)

    elif current != 0 and resistance != 0:
        retval = current * resistance

    return retval


def resistance(power=0, current=0, voltage=0):
    """Calculates resistance based on any two available values using Ohm's Law. Pass in any two of the three parameters.
    The third (unsupplied) parameter will simply default to a value of 0.

    Inputs:
        power: P (Watts)
        current: I (Amperes)
        voltage: V (Volts)

    Output:
        resistance: R (Ohms)
    """
    retval = 0

    if power != 0 and current != 0:
        retval = power / pow(current, 2)

    elif power != 0 and voltage != 0:
        retval = pow(voltage, 2) / power

    elif voltage != 0 and current != 0:
        retval = voltage / current

    return retval


def voltage_divider_r(voltage_in, resistance_1, resistance_2):
    """Calculates output voltage when two resistors are used as a voltage divider. The output voltage will always
    be lower than the input voltage.

    Inputs:
        voltage_in: Vin (Volts)
        resistance_1: R1 (Ohms)
        resistance_2: R2 (Ohms)

    Output:
        voltage_out: Vout (Volts)
    """
    retval = 0

    try:
        retval = voltage_in * (resistance_2 / (resistance_1 + resistance_2))

    except ZeroDivisionError:
        _error_zero_division('voltage_divider_r', 'single', "'resistance_1', 'resistance_2'")

    return retval


# ================================================================================================================= #
#                                                   DIRECT CURRENT                                                  #
# ================================================================================================================= #

# =============== #
# SERIES CIRCUITS #
# =============== #
def total_series_current(currents: tuple):
    """Takes a tuple of current measurements in a series circuit and returns the total current.

    Inputs:
        currents: I (Amperes)

    Output:
        total_current: I (Amperes)
    """
    retval = currents[0]

    try:
        for item in currents:
            if item != retval:
                raise ValueError

    except ValueError:
        print("ERROR: method 'total_series_current' all current measurements in a series circuit should be identical.")
        retval = 0
    return retval


def total_series_resistance(resistances: tuple):
    """Takes a tuple of resistance measurements in a series circuit and returns the total resistance.

    Inputs:
        resistances: R (Ohms)

    Output:
        total_resistance: R (Ohms)
    """
    return _sums(resistances)


def total_series_voltage(voltages: tuple):
    """Takes a tuple of voltage measurements in a series circuit and returns the total voltage.

    Inputs:
        voltages: V (Volts)

    Output:
        total_voltage: V (Volts)
    """
    return _sums(voltages)


def total_series_capacitance(capacitances: tuple):
    """Takes a tuple of capacitance measurements in a series circuit and returns the total capacitance.

    Inputs:
        capacitances: C (Farads)

    Output:
        total_capacitance: C (Farads)
    """
    return _inverse_sums(capacitances, 'total_series_capacitance')


def total_series_inductance(inductances: tuple):
    """Takes a tuple of inductance measurements in a series circuit and returns the total inductance.

    Inputs:
        inductances: L (Henries)

    Output:
        total_inductance: L (Henries)
    """
    return _sums(inductances)


# ================= #
# PARALLEL CIRCUITS #
# ================= #
def total_parallel_current(currents: tuple):
    """Takes a tuple of current measurements in a parallel circuit and returns the total current.

    Inputs:
        currents: I (Amperes)

    Output:
        total_current: I (Amperes)
    """
    return _sums(currents)


def total_parallel_resistance(resistances: tuple):
    """Takes a tuple of resistance measurements in a parallel circuit and returns the total resistance.

    Inputs:
        resistances: R (Ohms)

    Output:
        total_resistance: R (Ohms)
    """
    return _inverse_sums(resistances, 'total_parallel_resistance')


def total_parallel_voltage(voltages: tuple):
    """Takes a tuple of voltage measurements in a parallel circuit and returns the total voltage.

    Inputs:
        voltages: V (Volts)

    Output:
        total_voltage: V (Volts)
    """
    retval = voltages[0]

    try:
        for item in voltages:
            if item != retval:
                raise ValueError

    except ValueError:
        print("ERROR: method 'total_parallel_voltage' all voltage measurements in a parallel circuit "
              "should be identical.")
        retval = 0

    return retval


def total_parallel_capacitance(capacitances: tuple):
    """Takes a tuple of capacitance measurements in a parallel circuit and returns the total capacitance.

    Inputs:
        capacitances: C (Farads)

    Output:
        total_capacitance: C (Farads)
    """
    return _sums(capacitances)


def total_parallel_inductance(inductances: tuple):
    """Takes a tuple of inductance measurements in a parallel circuit and returns the total inductance.

    Inputs:
        inductances: L (Henries)

    Output:
        total_inductance: L (Henries)
    """
    return _inverse_sums(inductances, 'total_parallel_inductance')


# ================================================================================================================= #
#                                               ALTERNATING CURRENT                                                 #
# ================================================================================================================= #
# ========= #
# FREQUENCY #
# ========= #
def frequency_cxc(capacitance, capacitive_reactance):
    """Calculates frequency when capacitance and capacitive reactance are known.

    Inputs:
        capacitance: C (Farads)
        capacitive_reactance: Xc (Ohms)

    Output:
        frequency: f (Hertz)
    """
    return _inverse_tau(capacitance, capacitive_reactance, 'frequency_cxc')


def frequency_lxl(inductance, inductive_reactance):
    """Calculates frequency when inductance and inductive reactance are known.

    Inputs:
        inductance: L (Henries)
        inductive_reactance: Xl (Ohms)

    Output:
        frequency: f (Hertz)
    """
    retval = 0

    try:
        retval = inductive_reactance / (2 * PI * inductance)

    except ZeroDivisionError:
        _error_zero_division('frequency_lxl', 'single', 'inductance')

    return retval


def frequency_wl(wavelength):
    """Calculates frequency when wavelength is known.

    Inputs:
        wavelength: w (Meters)

    Output:
        frequency: f (Hertz)
    """
    retval = 0

    try:
        retval = SPEED_OF_LIGHT / wavelength

    except ZeroDivisionError:
        _error_zero_division('frequency_wl', 'single', 'wavelength')

    return retval


def wavelength(frequency):
    """Calculates wavelength when frequency is known.

    Inputs:
        frequency: f (Hertz)

    Output:
        wavelength: w (Meters)
    """
    retval = 0

    try:
        retval = SPEED_OF_LIGHT / frequency

    except ZeroDivisionError:
        _error_zero_division('wavelength', 'single', 'frequency')

    return retval


def antenna_length_qw(frequency):
    """Calculates optimal quarter wave antenna length to receive input frequency. This is useful when
    designing dipole radio antennae.

    Inputs:
        frequency: f (Hertz)

    Output:
        quarter_wavelength: w (Meters)

    """
    wl = wavelength(frequency)

    return wl / 4.0


# =========== #
# CAPACITANCE #
# =========== #
def capacitance_fxc(frequency, capacitive_reactance):
    """Calculates capacitance when frequency and capacitive reactance are known.

    Inputs:
        frequency: f (Hertz)
        capacitive_reactance: Xc (Ohms)

    Output:
        capacitance: C (Farads)
    """
    return _inverse_tau(frequency, capacitive_reactance, 'capacitance_fxc')


# ========== #
# INDUCTANCE #
# ========== #
def inductance_fxl(frequency, inductive_reactance):
    """Calculates inductance when frequency and inductive reactance are known.

    Inputs:
        frequency: f (Hertz)
        inductive_reactance: Xl (Ohms)

    Output:
        inductance: L (Henries)
    """
    retval = 0

    try:
        retval = inductive_reactance / (2 * PI * frequency)

    except ZeroDivisionError:
        _error_zero_division('inductance_fxl', 'single', 'frequency')

    return retval


def back_emf(inductance, current_t1, current_t2, time):
    """Calculates back EMF when current stops flowing in an inductor. Large voltages tend to get produced
    which can damage components unless sufficient protective diodes are used in the circuits.

    Inputs:
        inductance: L (Henries)
        current_t1: It1 (Amperes) - Current at T1
        current_t2: It2 (Amperes) - Current at T2
        time: s (Seconds) - Elapsed time between T1 and T2

    Output:
        back_emf: V (Volts)
    """
    retval = 0

    try:
        retval = -inductance * ((current_t2 - current_t1) / time)

    except ZeroDivisionError:
        _error_zero_division('back_emf', 'single', 'time')

    return retval


# ========= #
# REACTANCE #
# ========= #
def reactance_inductive_fl(frequency, inductance):
    """Calculates inductive reactance (Ohms) when frequency (Hertz) and inductance (Henries) are known."""
    return _tau(frequency, inductance)


def reactance_capacitive_fc(frequency, capacitance):
    """Calculates capacitive reactance (Ohms) when frequency (Hertz) and capacitance (Farads) are known."""
    return _inverse_tau(frequency, capacitance, 'reactance_capacitive_fc')


def reactance_capacitive_zr(impedance, resistance):
    """Calculates capacitive reactance: Xc (Ohms) when impedance: Z (Ohms) and resistance: R (Ohms) are known."""
    return math.sqrt(pow(impedance, 2) - pow(resistance, 2))


# =================== #
# VOLTAGE (Sine wave) #
# =================== #
def voltage_rms_from_peak(peak_voltage):
    """Calculates AC rms voltage: Vrms (Volts, sine) from peak voltage: Vp (Volts)."""
    return (1 / math.sqrt(2)) * peak_voltage


def voltage_rms_from_peak_to_peak(peak_to_peak_voltage):
    """Calculates AC rms voltage: Vrms (Volts, sine) from peak to peak voltage: Vp-p (Volts)."""
    return (1 / (2 * math.sqrt(2))) * peak_to_peak_voltage


def voltage_rms_from_average(average_voltage):
    """Calculates AC rms voltage: Vrms (Volts, sine) from average voltage: Vav (Volts)."""
    return (PI / (2 * math.sqrt(2))) * average_voltage


def voltage_average_from_peak(peak_voltage):
    """Calculates AC average voltage: Vav (Volts, sine) from peak voltage: Vp (Volts)."""
    return (2 * peak_voltage) / PI


def voltage_average_from_peak_to_peak(peak_to_peak_voltage):
    """Calculates AC average voltage: Vav (Volts, sine) from peak to peak voltage: Vp-p (Volts)."""
    return peak_to_peak_voltage / PI


def voltage_average_from_rms(rms_voltage):
    """Calculates AC average voltage: Vav (Volts, sine) from rms voltage: Vrms (Volts)."""
    return rms_voltage * ((2 * math.sqrt(2)) / PI)


def voltage_peak_from_peak_to_peak(peak_to_peak_voltage):
    """Calculates AC peak voltage: Vp (Volts, sine) from peak to peak voltage: Vp-p (Volts)."""
    return peak_to_peak_voltage * 0.5


def voltage_peak_from_rms(rms_voltage):
    """Calculates AC peak voltage: Vp (Volts, sine) from rms voltage: Vrms (Volts)."""
    return rms_voltage * math.sqrt(2)


def voltage_peak_from_average(average_voltage):
    """Calculates AC peak voltage: Vp (Volts, sine) from average voltage (Volts)."""
    return average_voltage * (PI / 2)


def voltage_peak_to_peak_from_average(average_voltage):
    """Calculates AC peak to peak voltage: Vp-p (Volts, sine) from average voltage: Vav (Volts)."""
    return average_voltage * PI


def voltage_peak_to_peak_from_rms(rms_voltage):
    """Calculates AC peak to peak voltage: Vp-p (Volts, sine) from rms voltage: Vrms (Volts)."""
    return rms_voltage * (2 * math.sqrt(2))


def voltage_peak_to_peak_from_peak(peak_voltage):
    """Calculates AC peak to peak voltage: Vp-p (Volts, sine) from peak voltage: Vp (Volts)."""
    return peak_voltage * 2


def voltage_divider_c(voltage_in, impedance, capacitive_reactance):
    """Calculates output voltage when a capacitor is used as a voltage divider.

    Inputs:
        voltage_in: Vin (Volts)
        impedance: Z (Ohms)
        capacitive_reactance: Xc (Ohms)

    Output:
        voltage_out: Vout (Volts)
    """
    return voltage_in * (capacitive_reactance / impedance)


# ========= #
# IMPEDANCE #
# ========= #
def impedance_rc(resistance, capacitive_reactance):
    """Calculate impedance in an RC (resistor capacitor) circuit.

    Inputs:
        resistance: R (Ohms)
        capacitive_reactance: Xc (Ohms).

    Output:
        impedance: Z (Ohms)
    """
    return math.sqrt(pow(resistance, 2) + pow(capacitive_reactance, 2))


def impedance_rcl(resistance, capacitive_reactance, inductive_reactance):
    """Calculate impedance in an RCL (resistor capacitor inductor) circuit.

    Inputs:
        resistance: R (Ohms)
        capacitive_reactance: Xc (Ohms)
        inductive_reactance: Xl (Ohms)

    Output:
        impedance: Z (Ohms)
    """
    return math.sqrt(pow(resistance, 2) + pow(inductive_reactance - capacitive_reactance, 2))


def impedance_rcl_phase_angle(resistance, capacitive_reactance, inductive_reactance):
    """Calculates the phase angle (Degrees) for impedance vectors in an RCL (resistor capacitor inductor) circuit.

    Inputs:
        resistance: R (Ohms)
        capacitive_reactance: Xc (Ohms)
        inductive_reactance: Xl (Ohms)

    Output:
        phase_angle: 𝜃 (Degrees)
    """
    return math.degrees(math.atan((inductive_reactance - capacitive_reactance) / resistance))


# ======================== #
# AMPLIFIERS / ATTENUATORS #
# ======================== #
def gain(input_value, output_value):
    """Calculates the gain ratio of either voltage, current or power.  If greater than 1 it is an amplification,
    and if less than 1 it is an attenuation.

    Inputs:
        input_value: voltage: V (Volts), current: I (Amperes) or power: P (Watts)
        output_value: voltage: V (Volts), current: I (Amperes) or power: P (Watts)

    Output:
        gain: A (ratio)
    """
    return output_value / input_value


def gain_db(input_value, output_value):
    """Calculates the dB gain of either voltage or current. If positive it is an amplification, and if negative it
    is an attenuation.

    Inputs:
        input_value: voltage: V (Volts) or current: I (Amperes)
        output_value: voltage: V (Volts) or current: I (Amperes)

    Output:
        gain: A (deciBels)
    """
    gain_ratio = gain(input_value, output_value)

    return 20 * math.log10(gain_ratio)


def gain_db_power(input_power, output_power):
    """Calculates the dB gain of power. If positive it is an amplification, and if negative it is an attenuation.

    Inputs:
        input_value: power: P (Watts)
        output_value: power: P (Watts)

    Output:
        power gain: A (deciBels)
    """
    db = gain_db(input_power, output_power)

    return db / 2


# ====== #
# COMMON #
# ====== #
def _sums(items: tuple):
    """Sums values in a tuple of numeric values."""
    total = 0.0

    for item in items:
        total += item

    return total


def _inverse_sums(items: tuple, calling_method):
    """Inverts the sum of values in a tuple of numeric values."""
    retval = 0

    for item in items:
        try:
            retval += (1 / item)

        except ZeroDivisionError:
            _error_zero_division(calling_method, 'tuple')
            return 0

    return 1 / retval


def _tau(item_a, item_b):
    """Returns 2 * PI times the inputs."""
    return 2 * PI * item_a * item_b


def _inverse_tau(item_a, item_b, calling_method):
    """Returns the inverse of 2 * PI times the inputs."""
    retval = 0
    tau = _tau(item_a, item_b)

    try:
        retval = 1 / tau

    except ZeroDivisionError:
        _error_zero_division(calling_method, 'multiple')
        retval = 0

    return retval


def _error_zero_division(calling_method, message_type, bad_parameter=''):
    if message_type == "single":
        print("ERROR: method '{}', parameter '{}' cannot be zero.".format(calling_method, bad_parameter))

    elif message_type == "multiple":
        print("ERROR: method '{}', none of the parameters can be zero.".format(calling_method))

    elif message_type == "tuple":
        print("ERROR: method '{}' tuple item used as divisor cannot be zero.".format(calling_method))

    return


# =============================== #
# TODO: handle divide by 0 errors #
# =============================== #
