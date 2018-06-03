import plotly
import plotly.graph_objs as go
import numpy as np
from utci_implementations import utci_numpy, utci_ladybug
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

air_temp = np.linspace(-30, 45, 20)
rel_hum = np.linspace(0.10, 0.90, 20)
mrt_temp = np.arange(-30, 70, 5)
wind_10m = np.arange(0, 10, 0.5)
clo = np.linspace(0.1, 1.4, 20)
met = np.linspace(0.5, 2.5, 20)

constants = {'rel_hum': 0.50 * np.ones(20), 'mrt': 'air_temp', 'wind_10': 3 * np.ones(20), 'clo': 'adjusted', 'met': 2.3}

print('Air Temp:', air_temp.shape)
print('Rel Hum:', rel_hum.shape)
print('MRT Temp:', mrt_temp.shape)
print('Wind 10m:', wind_10m.shape)
print('Clo:', clo.shape)
print('MET:', met.shape)


rh_vari = utci_numpy(np.tile(air_temp, 20), np.tile(mrt_temp, 20),
                     np.tile(constants['wind_10'], 20), np.repeat(rel_hum, 20))

# Make data.
X = air_temp
Y = rel_hum
X, Y = np.meshgrid(X, Y)
Z = np.reshape(rh_vari, (20, 20))


data = [go.Surface(x=X, y=Y, z=Z)]
#print(data.shape)
layout = go.Layout(title='Variations in Relative Humidity', autosize=True,
                   xaxis=dict(title='Air Temperature - C'),
                   yaxis=dict(title='Relative Humidity - %'),
                   #zaxis={'title': 'UTCI - C'}
                   )

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='rel_hum-3d-surface.html')