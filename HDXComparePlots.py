"""
Created on Thurs Jul 21 2021

@author: daniellee

Script to compare peptides of G7-0P, G7-2P, G17-0P, G17-2P

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

g7_0p_raw_data = pd.read_csv('HDX_WT_G7_0P_FT_DL_Final_Data_Cluster.csv')
g7_0p_protein = 'G7-0P'

g7_2p_raw_data = pd.read_csv('HDX_WT_G7_2P_FT_DL_Final_Data_Cluster.csv')
g7_2p_protein = 'G7-2P'

g17_0p_raw_data = pd.read_csv('HDX_WT_G17_0P_FT_DL_Final_Data_Cluster.csv')
g17_0p_protein = 'G17-0P'

g17_2p_raw_data = pd.read_csv('HDX_WT_G17_2P_FT_DL_Final_Data_Cluster.csv')
g17_2p_protein = 'G17-2P'

df1 = pd.DataFrame(g7_0p_raw_data)
df2 = pd.DataFrame(g7_2p_raw_data)
df3 = pd.DataFrame(g17_0p_raw_data)
df4 = pd.DataFrame(g17_2p_raw_data)

start = int(input("\nInput start residue: "))
end = int(input("\nInput end residue: "))
state = input("\nG or Apo? ")
scale = input("\nLog or linear scale? ")

if state in ['Apo', 'apo', 'a', 'A']:
    state1 = 'Apo-0P'
    state2 = 'Apo-2P'
    state3 = '2P-Apo'
    sub_range1 = df1[(df1['Start'] == start) & (df1['End'] == end) & (df1['State'] == state1)]
    sub_range2 = df2[(df2['Start'] == start) & (df2['End'] == end) & (df2['State'] == state3)]
    sub_range3 = df3[(df3['Start'] == start) & (df3['End'] == end) & (df3['State'] == state1)]
    sub_range4 = df4[(df4['Start'] == start) & (df4['End'] == end) & (df4['State'] == state2)]
    
elif state in ['G', 'g']:
    state1 = 'G7-0P'
    state2 = '2P-G7'
    state3 = 'G17-0P'
    state4 = 'G17-2P'
    sub_range1 = df1[(df1['Start'] == start) & (df1['End'] == end) & (df1['State'] == state1)]
    sub_range2 = df2[(df2['Start'] == start) & (df2['End'] == end) & (df2['State'] == state2)]
    sub_range3 = df3[(df3['Start'] == start) & (df3['End'] == end) & (df3['State'] == state3)]
    sub_range4 = df4[(df4['Start'] == start) & (df4['End'] == end) & (df4['State'] == state4)]
    
x1 = sub_range1.iloc[:,9]
y1 = sub_range1.iloc[:,14]
x2 = sub_range2.iloc[:,9]
y2 = sub_range2.iloc[:,14]
x3 = sub_range3.iloc[:,9]
y3 = sub_range3.iloc[:,14]
x4 = sub_range4.iloc[:,9]
y4 = sub_range4.iloc[:,14]

sequence1 = sub_range1['Sequence'].values[0]
sequence2 = sub_range2['Sequence'].values[0]
sequence3 = sub_range3['Sequence'].values[0]
sequence4 = sub_range4['Sequence'].values[0]

fig = plt.figure(figsize = (30,15))
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)
ax1.plot(x1, y1, marker = 's')
ax2.plot(x2, y2, 'tab:orange', marker = 's')
ax3.plot(x3, y3, 'tab:green', marker = 's')
ax4.plot(x4, y4, 'tab:red', marker = 's')
plot_title1 = [g7_0p_protein, str(start) + "-" + str(end), sequence1]
plot_title2 = [g7_2p_protein, str(start) + "-" + str(end), sequence2]
plot_title3 = [g17_0p_protein, str(start) + "-" + str(end), sequence3]
plot_title4 = [g17_2p_protein, str(start) + "-" + str(end), sequence4]
ax1.set_title(" ".join(plot_title1))
ax2.set_title(" ".join(plot_title2))
ax3.set_title(" ".join(plot_title3))
ax4.set_title(" ".join(plot_title4))
ax1.set_ylabel("Relative Uptake (Da)")
ax1.set_xlabel("Exposure Time (Minutes)")
ax2.set_ylabel("Relative Uptake (Da)")
ax2.set_xlabel("Exposure Time (Minutes)")
ax3.set_ylabel("Relative Uptake (Da)")
ax3.set_xlabel("Exposure Time (Minutes)")
ax4.set_ylabel("Relative Uptake (Da)")
ax4.set_xlabel("Exposure Time (Minutes)")

if scale in ['log', 'Log']:
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    ax3.set_yscale('log')
    ax3.set_xscale('log')
    ax4.set_yscale('log')
    ax4.set_xscale('log')
elif scale in ['linear', 'Linear', 'lin', 'Lin']:
    ax1.set_yscale('linear')
    ax1.set_xscale('linear')
    ax2.set_yscale('linear')
    ax2.set_xscale('linear')
    ax3.set_yscale('linear')
    ax3.set_xscale('linear')
    ax4.set_yscale('linear')
    ax4.set_xscale('linear')
    
plt.show()
