import electronics_calculator as ec
import scale_factors as sf

f = sf.Frequency
d = sf.Distance

input_wavelength = sf.scale_in(12.5, d.CENTIMETERS)
frequency = ec.frequency_from_wavelength(input_wavelength)
output_frequency = sf.scale_out(frequency, f.GIGAHERTZ)
print("input_wavelength (m): %f" % input_wavelength)
print("output_frequency (GHz): %f" % output_frequency)
