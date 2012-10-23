from hyperion.model import AnalyticalYSOModel
from hyperion.util.constants import pc, lsun, rsun, msun, au,pi
from hyperion.model import ModelOutput
import numpy as np

m = AnalyticalYSOModel()
m.set_n_photons(initial=100000, imaging=100000)
m.star.luminosity = 5 * lsun
m.star.radius = 2 * rsun
m.star.temperature = 6000.

disk = m.add_flared_disk()
disk.mass = 0.01 * msun             # Disk mass
disk.rmin = 10 * rsun               # Inner radius
disk.rmax = 300 * au                # Outer radius
disk.r_0 = 100. * au                # Radius at which h_0 is defined
disk.h_0 = 5 * au                   # Disk scaleheight at r_0
disk.p = -1                         # Radial surface density exponent
disk.beta = 1.25                    # Disk flaring power

envelope = m.add_power_law_envelope()
envelope.mass = 0.001 * msun          # Envelope mass
envelope.rmin = au                  # Inner radius
envelope.rmax = 10000 * au          # Outer radius
envelope.power = -2                 # Radial power
envelope.r_0 = au                   # Inner density radius

#dust
disk.dust = 'www003.hdf5'
envelope.dust = 'kmh.hdf5'
#cavity.dust = 'kmh_hdf5'

#coordinates
n_r = 200
n_theta = 200
n_phi = 1
m.set_spherical_polar_grid_auto(n_r, n_theta, n_phi)


#viewing angles
image = m.add_peeled_images(image=False)
# Set number of viewing angles
n_view = 10
# Generate the viewing angles
theta = np.linspace(0., 90., n_view)
phi = np.repeat(45., n_view)
# Set the viewing angles
image.set_viewing_angles(theta, phi)
#sed interval
n_wav=250
wav_min=0.1
wav_max=1000
image.set_wavelength_range(n_wav, wav_min, wav_max)

#write out hyperion input
m.write('test_disc.rtin')