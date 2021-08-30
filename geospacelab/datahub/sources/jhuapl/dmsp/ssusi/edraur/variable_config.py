# Licensed under the BSD 3-Clause License
# Copyright (C) 2021 GeospaceLab (geospacelab)
# Author: Lei Cai, Space Physics and Astronomy, University of Oulu

__author__ = "Lei Cai"
__copyright__ = "Copyright 2021, GeospaceLab"
__license__ = "BSD-3-Clause License"
__email__ = "lei.cai@oulu.fi"
__docformat__ = "reStructureText"

from geospacelab.datahub import VariableModel as Var
import geospacelab.visualization.mpl.colormaps as cm

database = 'jhuapl'

timestamps = {
    'DATETIME': 'DATETIME',
}


default_colormap = "gist_ncar"

default_plot_config = {
    'line':         {
        'linestyle':        '-',
        'linewidth':        1.5,
        'marker':           '',
        'markersize':       3,
    },
    'pcolormesh':   {
        'cmap':            default_colormap,
    }
}

configured_variables = {}
visual = 'on'

depend_0 = {'UT': 'DATETIME'}
depend_c = {'SPECTRA': 'EMISSION_SPECTRA'}

####################################################################################################################
var_name = 'GRID_AUR_1216'
var = Var(name=var_name, ndim=4, variable_type='scalar', visual=visual)
# set variable attrs
var.fullname = 'Auroral emission intensity at 121.6 nm'
var.label = r'1216'
var.group = 'Emission intensity'
var.unit = 'R'
var.depends = {0: depend_0, 1: {'AACGM_LAT': 'GRID_MLAT'}, 3: {'AACGM_LON': 'GRID_MLON'}}
# set plot attrs
plot_config = var.visual.plot_config
plot_config.config(**default_plot_config)
plot_config.style = '2P'
# set axis attrs
axis = var.visual.axis


configured_variables[var_name] = var
