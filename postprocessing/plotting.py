# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:33:01 2023

@author: Jelle
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
plt.close('all')
import seaborn as sns
sns.set_theme(style='white')

# My Data
folder = ['../runningS/m_2', '../runningS/m_4']
file = '/postprocessed.csv'

m = np.array([2, 4])
E_Ons = np.zeros(len(m))
E_Ons_err = np.zeros(len(m))

E_NE = np.zeros(len(m))
E_NE_err = np.zeros(len(m))

for i in range(len(m)):
    data = pd.read_csv(folder[i]+file)

    E_Ons[i] = data['E conduct Ons/[S/m]'][0]
    E_Ons_err[i] = data['E conduct Ons/[S/m]'][1]

    E_NE[i] = data['E conduct NEYH_cor /[S/m]'][0]
    E_NE_err[i] = data['E conduct NEYH_cor /[S/m]'][1]


# Vega Data
m_V = np.array([4])
E_Ons_V = np.array([33.30])
E_Ons_V_err = np.array([35.33]) - E_Ons_V

E_NE_V = np.array([43.25])
E_NE_V_err = np.zeros(len(m_V))

fig = plt.figure('OCTP and Vega', figsize=(4.5, 4.5), dpi=400)
ax = fig.add_axes([0, 0, 0.9, 0.9])
sns.set_theme(style='white')
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2.5)

ax.xaxis.set_tick_params(width=2)
ax.yaxis.set_tick_params(width=2)
ax.tick_params(which='both', width=2, direction='out', left=True, bottom=True)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4)
plt.xticks(fontsize=18, rotation=0)
plt.yticks(fontsize=18)
sns.set_theme(style='white')


plt.errorbar(m, E_Ons, yerr=E_Ons_err, color='C0', fmt='o', capsize=8, label='Delft Einstein')
plt.scatter(m, E_NE, color='C1', marker='<', label='Delft NE')
plt.errorbar(m_V, E_Ons_V, yerr=E_Ons_V_err, color='C2', fmt='o', capsize=8, label='Madrid GK')
plt.scatter(m_V, E_NE_V, color='C3', marker='>', label='Madrid NE')
plt.xlabel('molality/[mol/kg]', fontsize=22)
plt.ylabel('$\sigma$/[S/m]', fontsize=22)
plt.xlim(0, 6.3)
plt.ylim(0, 49)
plt.xticks(fontsize=18, rotation=0)
plt.yticks(fontsize=18)

handles, labels = plt.gca().get_legend_handles_labels()
order = [2, 0, 3, 1]
leg = ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],
                fontsize=11.5, labelspacing=0.25,loc='upper left')
leg.get_frame().set_edgecolor('0')
leg.get_frame().set_linewidth(2.0)
plt.savefig('test.pdf', bbox_inches='tight')