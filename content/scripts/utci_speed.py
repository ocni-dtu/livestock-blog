__author__ = "Christian Kongsgaard"
__license__ = 'MIT'

# -------------------------------------------------------------------------------------------------------------------- #
# IMPORTS

# Modules
import numpy as np
import matplotlib.pyplot as plt
from pyepw.epw import EPW
import time

from content.scripts.utci_implementations import *

# -------------------------------------------------------------------------------------------------------------------- #
# UTCI Speed Tests

epw_path = r'C:\Users\ocni\Dropbox\Uddannelse\DTU\Diverse\EPW_WeatherData\DNK_Copenhagen.061800_IWEC.epw'
epw = EPW()
epw.read(epw_path)

air_temp = []
rel_hum = []
wind = []

for weather_data in epw.weatherdata:
    air_temp.append(weather_data.dry_bulb_temperature)
    rel_hum.append(weather_data.relative_humidity)
    wind.append(weather_data.wind_speed)

mrt_temp = air_temp


def time_slow_utci(years=1):
    air_dub = []
    mrt_dub = []
    wind_dub = []
    rh_dub = []

    for y in range(years):
        air_dub.extend(air_temp)
        mrt_dub.extend(mrt_temp)
        wind_dub.extend(wind)
        rh_dub.extend(rel_hum)

    t0 = time.time()
    for i in range(len(air_dub)):
        utci_ladybug(air_dub[i], mrt_dub[i], wind_dub[i], rh_dub[i])
    return time.time()-t0


def time_numpy_utci(years=1):
    air_dub = []
    mrt_dub = []
    wind_dub = []
    rh_dub = []

    for y in range(years):
        air_dub.extend(air_temp)
        mrt_dub.extend(mrt_temp)
        wind_dub.extend(wind)
        rh_dub.extend(rel_hum)

    air_np = np.array(air_dub)
    rh_np = np.array(rh_dub)
    wind_np = np.array(wind_dub)
    mrt_np = np.array(mrt_dub)

    t0 = time.time()
    utci_numpy(air_np, mrt_np, wind_np, rh_np)

    return time.time() - t0


numpy_time = [time_numpy_utci(1), time_numpy_utci(2), time_numpy_utci(3), time_numpy_utci(4), time_numpy_utci(5),
              time_numpy_utci(6), time_numpy_utci(7), time_numpy_utci(8), time_numpy_utci(9), time_numpy_utci(10)]

slow_time = [time_slow_utci(i)
             for i in range(10)]

colors = ['#F44336', '#FFBF1F', '#57DA10', '#12B2FF', '#7D1BDA']

hours = [(h * 8760)
         for h in range(10)]

plt.figure(figsize=(12, 6.75))
plt.title('UTCI Computation Time Comparison\nCPython')
plt.plot(hours, numpy_time, label='NumPy', color=colors[0])
plt.plot(hours, slow_time, label='Original', color=colors[1])
plt.legend()
plt.ylabel('Time in seconds')
plt.xlabel('Number of hours computed')
plt.tight_layout()

ladybug_item_time = [6.7, 9.0, 13.8, 17.5, 21.6, 30, 37.5, 38.3, 39.0, 50.0]
ladybug_list_time = [1.1, 2.0, 3.3, 4.5, 5.5, 6.6, 7.6, 8.8, 10.0, 11.2]
ladybug_tree_time = [0.995, 1.9, 2.9, 4.0, 4.9, 5.8, 6.9, 8.0, 8.7, 10.4]
livestock_time = [0.35, 0.535, 0.629, 0.747, 0.891, 1.1, 1.3, 1.3, 1.5, 1.6]

plt.figure(figsize=(12, 6.75))
plt.title('UTCI Computation Time Comparison\nGrasshopper Component')
plt.plot(hours, ladybug_item_time, label='Item Inputs', color=colors[1])
plt.plot(hours, ladybug_list_time, label='List Inputs', color=colors[2])
plt.plot(hours, ladybug_tree_time, label='Tree Inputs', color=colors[3])
plt.plot(hours, livestock_time, label='Livestock', color=colors[0])
plt.legend()
plt.ylabel('Time in seconds')
plt.xlabel('Number of hours computed')
plt.tight_layout()

plt.show()
