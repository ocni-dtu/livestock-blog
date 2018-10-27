__author__ = "Christian Kongsgaard"
__license__ = 'MIT'

# -------------------------------------------------------------------------------------------------------------------- #
# IMPORTS

# Modules
import numpy as np
import matplotlib.pyplot as plt
from content.scripts import utci_implementations as ui
import matplotlib.cm as cm
import os

# -------------------------------------------------------------------------------------------------------------------- #
# Functions

folder = r'C:\Users\ocni\PycharmProjects\ocni-dtu.github.io\content\images\utci_parameters'


def mm2inch(*tuple_):
    inch = 25.4
    if isinstance(tuple_[0], tuple):
        return tuple(i/inch for i in tuple_[0])
    elif isinstance(tuple_[0], list):
        return tuple(i/inch for i in tuple_[0])
    else:
        return tuple(i/inch for i in tuple_)


def change_relhum():
    temp = np.linspace(-30, 40, 200)
    relhum = np.linspace(10, 90, 200)
    t, rh = np.meshgrid(temp, relhum)
    mrt = t
    wind = np.ones((200, 200)) * 3

    utci = ui.utci_numpy(t, mrt, wind, rh)

    return t, rh, utci


def plot3d_relhum():
    temp, relhum, utci = change_relhum()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(temp, relhum, utci, cmap='afmhot')
    ax.set_ylabel('Relative Humidity')
    ax.set_xlabel('Air Temperature')
    ax.set_zlabel('UTCI')
    plt.show()


#plot3d_relhum()


def change_wind():
    temp = np.linspace(-30, 40, 200)
    wind = np.linspace(0.5, 17, 200)
    relhum = np.ones((200, 200)) * 50
    t, wi = np.meshgrid(temp, wind)
    mrt = t
    utci = ui.utci_numpy(t, mrt, wi, relhum)

    return t, wi, utci


def plot3d_wind():
    temp, wind, utci = change_wind()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(temp, wind, utci, cmap='afmhot')
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

    return t, mt, utci


def plot3d_mrt():
    temp, mrt, utci = change_mrt()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(temp, mrt, utci, cmap='afmhot')
    ax.set_ylabel('Mean Radiant Temperature')
    ax.set_xlabel('Air Temperature')
    ax.set_zlabel('UTCI')
    plt.show()


#change_mrt()


def standard_utci():
    temp = np.linspace(-30, 40, 200)
    wind = np.ones((200, 200)) * 3
    relhum = np.ones((200, 200)) * 50
    t, mt = np.meshgrid(temp, temp)
    mrt = t
    utci = ui.utci_numpy(t, mrt, wind, relhum)

    return utci


def relhum_difference(save=False):
    temp, relhum, utci_rh = change_relhum()
    utci_std = standard_utci()

    diff_utci = utci_rh - utci_std

    colors = cm.RdBu_r
    fig, ax = plt.subplots(1, 1, figsize=mm2inch(250, 200))
    plot = ax.pcolor(temp, relhum, diff_utci, cmap=colors, vmin=-35, vmax=35)
    levels = [-2, -1, 0, 1, 2, 5, 10, 15, 20]
    con = ax.contour(temp, relhum, diff_utci, levels, colors='k')
    plt.clabel(con, inline=1, fontsize=10, fmt='%d')
    ax.set_xlabel('Air Temperature [°C]')
    ax.set_ylabel('Relative Humidity [%]')
    bar = fig.colorbar(plot, ax=ax)
    bar.set_label('UTCI Difference [°C]')
    plt.tight_layout()

    if save:
        plt.savefig(os.path.join(folder, 'utci_relhum.png'), dpi=300)

    plt.show()


relhum_difference(True)


def wind_difference(save=False):
    temp, wind, utci_wind = change_wind()
    utci_std = standard_utci()

    diff_utci = utci_wind - utci_std

    colors = cm.RdBu_r
    fig, ax = plt.subplots(1, 1, figsize=mm2inch(250, 200))
    plot = ax.pcolor(temp, wind, diff_utci, cmap=colors, vmin=-35, vmax=35)
    levels = [-30, -25, -20, -15, -10, -5, 0, 5, 10]
    con = ax.contour(temp, wind, diff_utci, levels, colors='k')
    plt.clabel(con, levels, inline=1, fontsize=10, fmt='%d')
    ax.set_xlabel('Air Temperature [°C]')
    ax.set_ylabel('Wind Speed [m/s]')
    bar = fig.colorbar(plot, ax=ax)
    bar.set_label('UTCI Difference [°C]')
    plt.tight_layout()

    if save:
        plt.savefig(os.path.join(folder, 'utci_wind.png'), dpi=300)

    plt.show()


wind_difference(True)


def mrt_difference(save=False):
    temp, mrt, utci_mrt = change_mrt()
    utci_std = standard_utci()

    diff_utci = utci_mrt - utci_std

    colors = cm.RdBu_r
    fig, ax = plt.subplots(1, 1, figsize=mm2inch(250, 200))
    plot = ax.pcolor(temp, mrt, diff_utci, cmap=colors, vmin=-35, vmax=35)
    levels = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
    con = ax.contour(temp, mrt, diff_utci, levels, colors='k')
    plt.clabel(con, inline=1, fontsize=10, fmt='%d')
    ax.set_xlabel('Air Temperature [°C]')
    ax.set_ylabel('Mean Radiant Temperature [°C]')
    bar = fig.colorbar(plot, ax=ax)
    bar.set_label('UTCI Difference [°C]')
    plt.tight_layout()

    if save:
        plt.savefig(os.path.join(folder, 'utci_mrt.png'), dpi=300)

    plt.show()


mrt_difference(True)
