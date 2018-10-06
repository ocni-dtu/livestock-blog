__author__ = "Christian Kongsgaard"
__license__ = 'MIT'

# -------------------------------------------------------------------------------------------------------------------- #
# IMPORTS

# Modules
import numpy as np
import matplotlib.pyplot as plt
from content.scripts import utci_implementations as ui
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------------------------------------------------------------------------------- #
# Functions


def change_relhum():
    temp = np.linspace(-30, 40, 200)
    relhum = np.linspace(10, 90, 200)
    t, rh = np.meshgrid(temp, relhum)
    mrt = t
    wind = np.ones((200, 200)) * 3

    utci = ui.utci_numpy(t, mrt, wind, rh)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(t, rh, utci, cmap='afmhot')
    ax.set_ylabel('Relative Humidity')
    ax.set_xlabel('Air Temperature')
    ax.set_zlabel('UTCI')
    plt.show()


#change_relhum()


def change_wind():
    temp = np.linspace(-30, 40, 200)
    wind = np.linspace(0.5, 17, 200)
    relhum = np.ones((200, 200)) * 50
    t, wi = np.meshgrid(temp, wind)
    mrt = t
    utci = ui.utci_numpy(t, mrt, wi, relhum)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(t, wi, utci, cmap='afmhot')
    ax.set_ylabel('Wind Speed')
    ax.set_xlabel('Air Temperature')
    ax.set_zlabel('UTCI')
    plt.show()


#change_wind()


def change_mrt():
    temp = np.linspace(-30, 40, 200)
    wind = np.ones((200, 200)) * 3
    relhum = np.ones((200, 200)) * 50
    mrt = np.linspace(-30, 70, 200)
    t, mt = np.meshgrid(temp, mrt)
    utci = ui.utci_numpy(t, mt, wind, relhum)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(t, mt, utci, cmap='afmhot')
    ax.set_ylabel('Mean Radiant Temperature')
    ax.set_xlabel('Air Temperature')
    ax.set_zlabel('UTCI')
    plt.show()


#change_mrt()