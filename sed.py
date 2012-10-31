import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for f in ['0.0001', '1e-07', '1e-10']:
    # Open the model - we specify the name without the .rtout extension
    m = ModelOutput('loop_' + f + '.rtout')

# Extract the SED for the smallest inclination and largest aperture, and
# scale to 300pc. In Python, negative indices can be used for lists and
# arrays, and indicate the position from the end. So to get the SED in the
# largest aperture, we set aperture=-1.
    wav, nufnu = m.get_sed(inclination=0, aperture=-1, distance=300 * pc)

# Plot the SED. The loglog command is similar to plot, but automatically
# sets the x and y axes to be on a log scale.
    ax.loglog(wav, nufnu, label=f)
    print f

ax.legend()
# Add some axis labels (we are using LaTeX here)
ax.set_xlabel(r'$\lambda$ [$\mu$m]')
ax.set_ylabel(r'$\lambda F_\lambda$ [ergs/s/cm$^2$]')

# Set view limits
ax.set_xlim(0.1, 5000.)
ax.set_ylim(1.e-16, 1.e-8)

# Write out the plot
fig.savefig('sed.png')