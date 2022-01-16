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
def power(current = 0.0, voltage = 0.0, resistance = 0.0):
    """Calculates power based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: current (Amperes); voltage (Volts); resistance (Ohms)"""

    if current > 0.0 and voltage > 0.0:
        retval = current * voltage

    elif current > 0.0 and resistance > 0.0:
        retval = pow(current, 2) * resistance

    else:
        retval = pow(voltage, 2) / resistance

    return retval


def current(power = 0.0, voltage = 0.0, resistance = 0.0):
    """Calculates current based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: power (Watts); voltage (Volts); resistance (Ohms)"""

    if power > 0.0 and voltage > 0.0:
        retval = power / voltage

    elif power > 0.0 and resistance > 0.0:
        retval = math.sqrt(power / resistance)

    else:
        retval = voltage / resistance

    return retval


def voltage(power = 0.0, current = 0.0, resistance = 0.0):
    """Calculates voltage (Volts) based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: power (Watts); current (Amperes); resistance (Ohms)"""

    if power > 0.0 and current > 0.0:
        retval = power / current

    elif power > 0.0 and resistance > 0.0:
        retval = math.sqrt(power * resistance)

    else:
        retval = current * resistance

    return retval


def resistance(power = 0.0, current = 0.0, voltage = 0.0):
    """Calculates resistance (Ohms) based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: power (Watts); current (Amperes); voltage (Volts)"""

    if power > 0.0 and current > 0.0:
        retval = power / pow(current, 2)

    elif power > 0.0 and voltage > 0.0:
        retval = pow(voltage, 2) / power

    else:
        retval = voltage / current

    return retval


def voltage_divider_r(voltage_in, resistance_1, resistance_2):
    """Calculates output voltage: Vout (Volts) given input voltage: Vin (Volts) and two
    resistor values: R1 & R2 (Ohms).\n\n This works when two resistors are used as a voltage divider."""
    return voltage_in * (resistance_2 / (resistance_1 + resistance_2))


# ================================================================================================================= #
#                                                   DIRECT CURRENT                                                  #
# ================================================================================================================= #

# =============== #
# SERIES CIRCUITS #
# =============== #
def total_series_current(currents: tuple):
    """Takes a tuple of all current (Amperes) measurements in a
    series circuit and returns the total current (Amperes)."""
    return currents[-1]


def total_series_resistance(resistances: tuple):
    """Takes a tuple of all resistance measurements (Ohms) in a
    series circuit and returns the total resistance (Ohms)."""
    return _sums(resistances)


def total_series_voltage(voltages: tuple):
    """Takes a tuple of all voltage measurements (Volts) in a
    series circuit and returns the total voltage (Volts)."""
    return _sums(voltages)


def total_series_capacitance(capacitances: tuple):
    """Takes a tuple of all capacitance measurements (Farads) in a
    series circuit and returns the total capacitance (Farads)."""
    return _inverse_sums(capacitances)


def total_series_inductance(inductances: tuple):
    """Takes a tuple of all inductance measurements (Henries) in a
    series circuit and returns the total inductance (Henries)."""
    return _sums(inductances)


# ================= #
# PARALLEL CIRCUITS #
# ================= #
def total_parallel_current(currents: tuple):
    """Takes a tuple of all current measurements (Amperes) in a
    parallel circuit and returns the total current (Amperes)."""
    return _sums(currents)


def total_parallel_resistance(resistances: tuple):
    """Takes a tuple of all resistance measurements (Ohms) in a
    parallel circuit and returns the total resistance (Ohms)."""
    return _inverse_sums(resistances)


def total_parallel_voltage(voltages: tuple):
    """Takes a tuple of all voltage measurements (Volts) in a
    parallel circuit and returns the total voltage (Volts)."""
    return voltages[-1]


def total_parallel_capacitance(capacitances: tuple):
    """Takes a tuple of all capacitance measurements (Farads) in a
    parallel circuit and returns the total capacitance (Farads)."""
    return _sums(capacitances)


def total_parallel_inductance(inductances: tuple):
    """Takes a tuple of all inductance measurements (Henries) in a
    parallel circuit and returns the total inductance (Henries)."""
    return _inverse_sums(inductances)


# ================================================================================================================= #
#                                               ALTERNATING CURRENT                                                 #
# ================================================================================================================= #
# ========= #
# FREQUENCY #
# ========= #
def frequency_cxc(capacitance, capacitive_reactance):
    """Calculates frequency (Hertz) when capacitance (Farads) and capacitive reactance (Ohms) are known."""
    return _inverse_tau(capacitance, capacitive_reactance)


def frequency_lxl(inductance, inductive_reactance):
    """Calculates frequency (Hertz) when inductance (Henries) and inductive reactance (Ohms) are known."""
    return inductive_reactance / (2 * PI * inductance)


def frequency_wl(wavelength):
    """Calculates frequency (Hertz) from wavelength (Meters)."""
    return SPEED_OF_LIGHT / wavelength


def wavelength(frequency):
    """Calculates wavelength (Meters) from frequency (Hertz)."""
    return SPEED_OF_LIGHT / frequency


def antenna_length_qw(frequency):
    """Calculates optimal quarter wave antenna length (Meters) to receive input frequency (Hertz).\n
    This is useful when designing dipole antennae"""
    wl = wavelength(frequency)

    return wl / 4.0


# =========== #
# CAPACITANCE #
# =========== #
def capacitance_fxc(frequency, capacitive_reactance):
    """Calculates capacitance (Farads) when frequency (Hertz) and capacitive reactance (Ohms) are known."""
    return _inverse_tau(frequency, capacitive_reactance)


# ========== #
# INDUCTANCE #
# ========== #
def inductance_fxl(frequency, inductive_reactance):
    """Calculates inductance: L (Henries) when frequency: F (Hertz) and inductive reactance: Xl (Ohms) are known."""
    return inductive_reactance / (2 * PI * frequency)


def back_emf(inductance, current_t1, current_t2, time):
    """Calculates back EMF (Volts) when current stops flowing in an inductor. Large voltages tend to get produced
    which can damage components unless sufficient diodes are used to protect the circuits.\n
    Inputs: inductance (Henries); current_t1: current at time 1 (Amperes); current_t2: current at time 2 (Amperes);
    time: the time it took from t1 to t2 (Seconds)"""
    return -inductance * ((current_t2 - current_t1) / time)


# ========= #
# REACTANCE #
# ========= #
def reactance_inductive_fl(frequency, inductance):
    """Calculates inductive reactance (Ohms) when frequency (Hertz) and inductance (Henries) are known."""
    return _tau(frequency, inductance)


def reactance_capacitive_fc(frequency, capacitance):
    """Calculates capacitive reactance (Ohms) when frequency (Hertz) and capacitance (Farads) are known."""
    return _inverse_tau(frequency, capacitance)


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


def _inverse_sums(items: tuple):
    """Inverts the sum of values in a tuple of numeric values."""
    total = 0.0

    for item in items:
        total += (1 / item)

    return 1 / total


def _tau(item_a, item_b):
    """Returns 2 * PI times the inputs."""
    return 2 * PI * item_a * item_b


def _inverse_tau(item_a, item_b):
    """Returns the inverse of 2 * PI times the inputs."""
    tau = _tau(item_a, item_b)

    return 1 / tau

# =============================== #
# TODO: handle divide by 0 errors #
# =============================== #
