# ================================= #
# Module: scale_factors.py          #
# Version: 0.1                      #
# Version date: 2022-01-14          #
# Author: Mino Girimonti            #
# License: GPL                      #
# ================================= #
"""This module provides definitions of scale units for common electronics calculations. \n
The Enum values equate to the exponent for: (10 ** value)."""

from enum import Enum


def scale_in(amount, factor: Enum):
    """The scaled in value is used for the electronics calculations and ensures consistent unit scale."""
    if factor is not None and factor.value != 1:
        retval = amount * pow(10, factor.value)
    else:
        retval = amount

    return retval


def scale_out(amount, factor: Enum):
    """The scaled out values are used for display of results in any unit scale required."""
    if factor is not None and factor.value != 1:
        retval = amount / pow(10, factor.value)
    else:
        retval = amount

    return retval


# Capacitance
class Capacitance(Enum):
    """Defines the scale factors for capacitance (Farads - F)."""
    FARADS = 1          # F     = 1E+01
    MILLIFARADS = -3    # mF    = 1E-03
    MICROFARADS = -6    # µF    = 1E-06
    NANOFARADS = -9     # nF    = 1E-09
    PICOFARADS = -12    # pF    = 1E-12


# Resistance
class Resistance(Enum):
    """Defines the scale factors for resistance, reactance and impedance (Ohms - Ω)."""
    OHMS = 1            # Ω     = 1E+01
    KILOHMS = 3         # KΩ    = 1E+03
    MEGAOHMS = 6        # MΩ    = 1E+06


# Frequency
class Frequency(Enum):
    """Defines the scale factors for frequency (Hertz - Hz)."""
    HERTZ = 1           # Hz    = 1E+01
    KILOHERTZ = 3       # KHz   = 1E+03
    MEGAHERTZ = 6       # MHz   = 1E+06
    GIGAHERTZ = 9       # GHz   = 1E+09


# Current
class Current(Enum):
    """Defines the scale factors for current (Amperes - A)."""
    AMPERES = 1         # A     = 1E+01
    MILLIAMPERES = -3   # mA    = 1E-03
    MICROAMPERES = -6   # µA    = 1E-06


# Power
class Power(Enum):
    """Defines the scale factors for power (Watts - W)."""
    WATTS = 1           # W     = 1E+01
    MEGAWATTS = 6       # MW    = 1E+06
    MILLIWATTS = -3     # mW    = 1E-03
    MICROWATTS = -6     # µW    = 1E-06


# Voltage
class Voltage(Enum):
    """Defines the scale factors for voltage (Volts - V)."""
    VOLTS = 1           # V     = 1E+01
    KILOVOLTS = 3       # KV    = 1E+03
    MILLIVOLTS = -3     # mV    = 1E-03
    MICROVOLTS = -6     # µV    = 1E-06


# Distance
class Distance(Enum):
    """Defines the scale factors for distance (Meters - m)."""
    METERS = 1          # m     = 1E+01
    CENTIMETERS = -2    # cm    = 1E-02
    MILLIMETERS = -3    # mm    = 1E-03
    KILOMETERS = 3      # Km    = 1E+03
