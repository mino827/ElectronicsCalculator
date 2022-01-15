# ================================= #
# Module: electronics_calculator.py #
# Version: 0.1                      #
# Version date: 2022-01-12          #
# Author: Mino Girimonti            #
# License: GPL                      #
# ================================= #
"""This module provides methods to perform common electronics calculations."""

import math


# ========= #
# CONSTANTS #
# ========= #
SPEED_OF_LIGHT = 300000000  # Metres per second
PI = math.pi


# ========= #
# OHM'S LAW #
# ========= #
def power(current: float = 0.0, voltage: float = 0.0, resistance: float = 0.0) -> float:
    """Calculates power based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: current (Amperes); voltage (Volts); resistance (Ohms)"""

    if current > 0.0 and voltage > 0.0:
        retval = current * voltage

    elif current > 0.0 and resistance > 0.0:
        retval = pow(current, 2) * resistance

    else:
        retval = pow(voltage, 2) / resistance

    return retval


def current(power: float = 0.0, voltage: float = 0.0, resistance: float = 0.0) -> float:
    """Calculates current based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: power (Watts); voltage (Volts); resistance (Ohms)"""

    if power > 0.0 and voltage > 0.0:
        retval = power / voltage

    elif power > 0.0 and resistance > 0.0:
        retval = math.sqrt(power / resistance)

    else:
        retval = voltage / resistance

    return retval


def voltage(power: float = 0.0, current: float = 0.0, resistance: float = 0.0) -> float:
    """Calculates voltage (Volts) based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: power (Watts); current (Amperes); resistance (Ohms)"""

    if power > 0.0 and current > 0.0:
        retval = power / current

    elif power > 0.0 and resistance > 0.0:
        retval = math.sqrt(power * resistance)

    else:
        retval = current * resistance

    return retval


def resistance(power: float = 0.0, current: float = 0.0, voltage: float = 0.0) -> float:
    """Calculates resistance (Ohms) based on any two available values using Ohm's Law. \n
    Pass in any two of the three parameters: power (Watts); current (Amperes); voltage (Volts)"""

    if power > 0.0 and current > 0.0:
        retval = power / pow(current, 2)

    elif power > 0.0 and voltage > 0.0:
        retval = pow(voltage, 2) / power

    else:
        retval = voltage / current

    return retval


# ========================================================= #
#                       DIRECT CURRENT                      #
# ========================================================= #

# =============== #
# SERIES CIRCUITS #
# =============== #
def total_series_current(currents: tuple) -> float:
    """Takes a tuple of all current (Amperes) measurements in a
    series circuit and returns the total current (Amperes)."""
    return currents[-1]


def total_series_resistance(resistances: tuple) -> float:
    """Takes a tuple of all resistance measurements (Ohms) in a
    series circuit and returns the total resistance (Ohms)."""
    return _sums(resistances)


def total_series_voltage(voltages: tuple) -> float:
    """Takes a tuple of all voltage measurements (Volts) in a
    series circuit and returns the total voltage (Volts)."""
    return _sums(voltages)


def total_series_capacitance(capacitances: tuple) -> float:
    """Takes a tuple of all capacitance measurements (Farads) in a
    series circuit and returns the total capacitance (Farads)."""
    return _inverse_sums(capacitances)


def total_series_inductance(inductances: tuple) -> float:
    """Takes a tuple of all inductance measurements (Henries) in a
    series circuit and returns the total inductance (Henries)."""
    return _sums(inductances)


# ================= #
# PARALLEL CIRCUITS #
# ================= #
def total_parallel_current(currents: tuple) -> float:
    """Takes a tuple of all current measurements (Amperes) in a
    parallel circuit and returns the total current (Amperes)."""
    return _sums(currents)


def total_parallel_resistance(resistances: tuple) -> float:
    """Takes a tuple of all resistance measurements (Ohms) in a
    parallel circuit and returns the total resistance (Ohms)."""
    return _inverse_sums(resistances)


def total_parallel_voltage(voltages: tuple) -> float:
    """Takes a tuple of all voltage measurements (Volts) in a
    parallel circuit and returns the total voltage (Volts)."""
    return voltages[-1]


def total_parallel_capacitance(capacitances: tuple) -> float:
    """Takes a tuple of all capacitance measurements (Farads) in a
    parallel circuit and returns the total capacitance (Farads)."""
    return _sums(capacitances)


def total_parallel_inductance(inductances: tuple) -> float:
    """Takes a tuple of all inductance measurements (Henries) in a
    parallel circuit and returns the total inductance (Henries)."""
    return _inverse_sums(inductances)


# ============================================================== #
#                       ALTERNATING CURRENT                      #
# ============================================================== #
def frequency_from_capacitance(capacitance: float, capacitive_reactance: float) -> float:
    """Calculates frequency (Hertz) when capacitance (Farads) and capacitive reactance (Ohms) are known."""
    return _inverse_tau(capacitance, capacitive_reactance)


def capacitance_from_frequency(frequency: float, capacitive_reactance: float) -> float:
    """Calculates capacitance (Farads) when frequency (Hertz) and capacitive reactance (Ohms) are known."""
    return _inverse_tau(frequency, capacitive_reactance)


def reactance_capacitive(frequency: float, capacitance: float) -> float:
    """Calculates capacitive reactance (Ohms) when frequency (Hertz) and capacitance (Farads) are known."""
    return _inverse_tau(frequency, capacitance)


def frequency_from_inductance(inductance: float, inductive_reactance: float) -> float:
    """Calculates frequency (Hertz) when inductance (Henries) and inductive reactance (Ohms) are known."""
    return inductive_reactance / (2 * PI * inductance)


def inductance_from_frequency(frequency: float, inductive_reactance: float) -> float:
    """Calculates inductance (Henries) when frequency (Hertz) and inductive reactance (Ohms) are known."""
    return inductive_reactance / (2 * PI * frequency)


def reactance_inductive(frequency: float, inductance: float) -> float:
    """Calculates inductive reactance (Ohms) when frequency (Hertz) and inductance (Henries) are known."""
    return _tau(frequency, inductance)


def back_emf(inductance: float, current_t1: float, current_t2: float, time: float) -> float:
    """Calculates back EMF (Volts) when current stops flowing in an inductor. \n
    Inputs: inductance (Henries); current_t1: current at time 1 (Amperes); current_t2: current at time 2 (Amperes);
    time: the time it took from t1 to t2 (Seconds)"""
    return -inductance * ((current_t2 - current_t1) / time)

def wavelength(frequency: float) -> float:
    """Calculates wavelength (Meters) from frequency (Hertz)."""
    return SPEED_OF_LIGHT / frequency


def frequency_from_wavelength(wavelength: float) -> float:
    """Calculates frequency (Hertz) from wavelength (Meters)."""
    return SPEED_OF_LIGHT / wavelength


def antenna_length_quarter_wave(frequency: float) -> float:
    """Calculates optimal quarter-wave antenna length (Meters) to receive input frequency (Hertz)."""
    wl = wavelength(frequency)

    return wl / 4.0


def antenna_length_half_wave(frequency: float) -> float:
    """Calculates optimal half-wave antenna length (Meters) to receive input frequency (Hertz)."""
    wl = wavelength(frequency)
    return wl / 2.0


def antenna_length_full_wave(frequency: float) -> float:
    """Calculates optimal full-wave antenna length (Meters) to receive input frequency (Hertz)."""
    wl = wavelength(frequency)
    return wl


def voltage_rms_from_peak(peak_voltage: float) -> float:
    """Calculates AC rms voltage (Volts, sine) from peak voltage (Volts)."""
    return (1 / math.sqrt(2)) * peak_voltage


def voltage_rms_from_peak_to_peak(peak_to_peak_voltage: float) -> float:
    """Calculates AC rms voltage (Volts, sine) from peak to peak voltage (Volts)."""
    return (1 / (2 * math.sqrt(2))) * peak_to_peak_voltage


def voltage_rms_from_average(average_voltage: float) -> float:
    """Calculates AC rms voltage (Volts, sine) from average voltage (Volts)."""
    return (PI / (2 * math.sqrt(2))) * average_voltage


def voltage_average_from_peak(peak_voltage: float) -> float:
    """Calculates AC average voltage (Volts, sine) from peak voltage (Volts)."""
    return (2 * peak_voltage) / PI


def voltage_average_from_peak_to_peak(peak_to_peak_voltage: float) -> float:
    """Calculates AC average voltage (Volts, sine) from peak to peak voltage (Volts)."""
    return peak_to_peak_voltage / PI


def voltage_average_from_rms(rms_voltage: float) -> float:
    """Calculates AC average voltage (Volts, sine) from rms voltage (Volts)."""
    return rms_voltage * ((2 * math.sqrt(2)) / PI)


def voltage_peak_from_peak_to_peak(peak_to_peak_voltage: float) -> float:
    """Calculates AC peak voltage (Volts, sine) from peak to peak voltage (Volts)."""
    return peak_to_peak_voltage * 0.5


def voltage_peak_from_rms(rms_voltage: float) -> float:
    """Calculates AC peak voltage (Volts, sine) from rms voltage (Volts)."""
    return rms_voltage * math.sqrt(2)


def voltage_peak_from_average(average_voltage: float) -> float:
    """Calculates AC peak voltage (Volts, sine) from average voltage (Volts)."""
    return average_voltage * (PI / 2)


def voltage_peak_to_peak_from_average(average_voltage: float) -> float:
    """Calculates AC peak to peak voltage (Volts, sine) from average voltage (Volts)."""
    return average_voltage * PI


def voltage_peak_to_peak_from_rms(rms_voltage: float) -> float:
    """Calculates AC peak to peak voltage (Volts, sine) from rms voltage (Volts)."""
    return rms_voltage * (2 * math.sqrt(2))


def voltage_peak_to_peak_from_peak(peak_voltage: float) -> float:
    """Calculates AC peak to peak voltage (Volts, sine) from peak voltage (Volts)."""
    return peak_voltage * 2


def impedance(resistance: float, capacitive_reactance: float, inductive_reactance: float) -> float:
    """Calculate impedance (Ohms) given resistance (Ohms) and reactance (Ohms) vectors."""
    return math.sqrt(pow(resistance, 2) + pow(inductive_reactance - capacitive_reactance, 2))


def impedance_phase_angle(resistance: float, capacitive_reactance: float, inductive_reactance: float) -> float:
    """Calculates the phase angle (Degrees) for impedance vectors:
    resistance (Ohms); capacitive reactance (Ohms); inductive reactance (Ohms)."""
    return math.degrees(math.atan((inductive_reactance - capacitive_reactance) / resistance))


# ========== #
# AMPLIFIERS #
# ========== #
def gain(input_value, output_value) -> float:
    """Calculates the gain ratio of either voltage (Volts), current (Amperes) or power (Watts)."""
    return output_value / input_value


def gain_db(input_value, output_value) -> float:
    """Calculates the gain (deciBels) of either voltage (Volts) or current (Amperes)."""
    gain_ratio = gain(input_value, output_value)

    return 20 * math.log10(gain_ratio)


def gain_db_power(input_power, output_power) -> float:
    """Calculates the gain (deciBels) for power (Watts)."""
    db = gain_db(input_power, output_power)

    return db / 2


# ====== #
# COMMON #
# ====== #
def _sums(items: tuple) -> float:
    """Sums values in a tuple of numeric values."""
    total = 0.0

    for item in items:
        total += item

    return total


def _inverse_sums(items: tuple) -> float:
    """Inverts the sum of values in a tuple of numeric values."""
    total = 0.0

    for item in items:
        total += (1 / item)

    return 1 / total


def _tau(item_a: float, item_b: float) -> float:
    """Returns 2 * PI times the inputs."""
    return 2 * PI * item_a * item_b


def _inverse_tau(item_a: float, item_b: float) -> float:
    """Returns the inverse of 2 * PI times the inputs."""
    return 1 / (2 * PI * item_a * item_b)
