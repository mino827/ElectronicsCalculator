import electronics_calculator as ec
import scale_factors as sf

# ============================================================= #
# Select appropriate Enum classes                               #
# ============================================================= #
f = sf.Frequency
d = sf.Distance
# ============================================================= #

# ============================================================= #
# Using scale_factors - More code but can use any unit scale    #
# ============================================================= #
input_wavelength = sf.scale_in(12.5, d.CENTIMETERS)             # Convert Meters to Centimeters for ease of input
frequency = ec.frequency_from_wavelength(input_wavelength)      # Still uses default unit (Meters) for calculations
output_frequency = sf.scale_out(frequency, f.GIGAHERTZ)         # Convert Hertz to Gigahertz for simpler display
print("input_wavelength (m): %f" % input_wavelength)
print("output_frequency (GHz): %f" % output_frequency)
# ============================================================= #

# ============================================================= #
# Without scale_factors - less code but always uses             #
# default unit for each parameter type                          #
# ============================================================= #
input_wavelength2 = 0.125                                       # Meters
frequency2 = ec.frequency_from_wavelength(input_wavelength2)    # Hertz
print("frequency2 (Hz): %f" % frequency2)
# ============================================================= #
