# Creado por: Lucy
# Fecha: 21/08/2023

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def figsize(scale, nplots=1):
    fig_width_pt = 390.0
    inches_per_pt = 1.0/72.27
    golden_mean = (np.sqrt(5.0)-1.0)/2.0
    fig_width = fig_width_pt*inches_per_pt*scale
    fig_height = nplots*fig_width*golden_mean
    fig_size = [fig_width, fig_height]
    return fig_size

pgf_with_latex = {
    "pgf.texsystem": "pdflatex",
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": [],
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,
    "font.size": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": figsize(1.0),
    "pgf.preamble": r"\usepackage[utf8x]{inputenc} \usepackage[T1]{fontenc}",
}
mpl.rcParams.update(pgf_with_latex)

def newfig(width, nplots=1):
    fig = plt.figure(figsize=figsize(width, nplots))
    ax = fig.add_subplot(111)
    return fig, ax

def savefig(filename, crop=True):
    if crop:
        plt.savefig('{}.pdf'.format(filename), bbox_inches='tight', pad_inches=0)
        plt.savefig('{}.eps'.format(filename), bbox_inches='tight', pad_inches=0)
    else:
        plt.savefig('{}.pdf'.format(filename))
        plt.savefig('{}.eps'.format(filename))

def multi_plot(width, nrows, ncols, sharex=False, sharey=False):
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, sharex=sharex, sharey=sharey,
                             figsize=figsize(width))
    return fig, axes

def set_line_style(ax, linestyle='-', marker=None, color=None):
    lines = ax.get_lines()
    for line in lines:
        line.set_linestyle(linestyle)
        if marker:
            line.set_marker(marker)
        if color:
            line.set_color(color)

def add_legend(ax, location='best'):
    legend = ax.legend(loc=location)
    frame = legend.get_frame()
    frame.set_linewidth(0.5)
    plt.setp(legend.get_texts(), fontsize=8)

def newfig_3d(width, nplots=1):
    fig = plt.figure(figsize=figsize(width, nplots))
    ax = fig.add_subplot(111, projection='3d')
    return fig, ax

def plot_surface_3d(ax, X, Y, Z, cmap='viridis', alpha=1):
    surf = ax.plot_surface(X, Y, Z, cmap=cmap, alpha=alpha)
    return surf

def scatter_3d(ax, X, Y, Z, color='blue', marker='o', s=20):
    scatter = ax.scatter(X, Y, Z, c=color, marker=marker, s=s)
    return scatter

def set_3d_labels(ax, xlabel, ylabel, zlabel):
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
