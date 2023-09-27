# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:50:54 2023

@author: Jelle
"""

import numpy as np
import pandas as pd
import matplotlib as mpl

###############################################################################
# Setting the default figure properties for my thesis
mpl.pyplot.close('all')
mpl.pyplot.rcParams["figure.figsize"] = [6, 5]
label_spacing = 1.1
marker = ['o', 'x', '^']

# Fonts
mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["axes.grid"] = "False"

# Sizes of specific parts
mpl.rcParams['axes.labelsize'] = 'large'
mpl.rcParams['xtick.major.pad']= 7
mpl.rcParams['ytick.major.pad']= 5
mpl.rcParams['xtick.labelsize']= 'large'
mpl.rcParams['ytick.labelsize']= 'large'
mpl.rcParams['lines.markersize'] = 10
mpl.rcParams['lines.markeredgewidth'] = 1
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['xtick.major.size'] = 5
mpl.rcParams['xtick.major.width'] = 1
mpl.rcParams['ytick.major.size'] = 5
mpl.rcParams['ytick.major.width'] = 1
mpl.rcParams['legend.fontsize'] = 'large'
# File properties and location
# mpl.use("SVG")
mpl.rcParams["svg.fonttype"] = "none"
# figures = r'C:\Users\Jelle\Delft University of Technology\Jelle Lagerweij Master - Documents\General\Personal Thesis files\00 Literature study\figures'
# Done

# My Data
folder = ['../runningS2\m_2', '../runningS2\m_4']
file = '/postprocessed.csv'

m = np.array([2, 4])
m_real = np.zeros(len(m))
E_Ons = np.zeros(len(m))
E_Ons_err = np.zeros(len(m))

E_NE = np.zeros(len(m))
E_NE_err = np.zeros(len(m))

for i in range(len(m)):
    data = pd.read_csv(folder[i]+file)
    m_real[i] = data['Molality/[mol/kg]'][0]

    E_Ons[i] = data['E conduct Ons/[S/m]'][0]
    E_Ons_err[i] = data['E conduct Ons/[S/m]'][1]

    E_NE[i] = data['E conduct NEYH_cor /[S/m]'][0]
    E_NE_err[i] = data['E conduct NEYH_cor /[S/m]'][1]

data = pd.read_csv('../KCl.csv', header=None, sep=' ', decimal=",")
data = data.to_numpy()
mpl.pyplot.figure()
mpl.pyplot.errorbar(m_real, E_Ons, yerr=E_Ons_err, fmt='o', capsize=11,
                    elinewidth=2, capthick=2, markersize=9, label=r'E $\sigma$')
mpl.pyplot.errorbar(m_real, E_NE, yerr=E_NE_err, fmt='<', capsize=11,
                    elinewidth=2, capthick=2, markersize=9, label=r'E $\sigma_{NE}$')
mpl.pyplot.plot(data[:, 0], data[:, 1], label=r'reference')
mpl.pyplot.legend(loc='upper left')
mpl.pyplot.xlim(0, 6.25)
mpl.pyplot.ylim(0, 50)
mpl.pyplot.xlabel(r'molality/[mol/kg]')
mpl.pyplot.ylabel(r'electric conductivity/[S/m]')
mpl.pyplot.tight_layout()
mpl.pyplot.grid()
mpl.pyplot.savefig('KCl.svg', format='svg')