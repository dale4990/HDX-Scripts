"""
Created on Thurs Jul 7 2021

@author: daniellee

Script to graph peptides based on the residue range

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

inhib = input("Plot G7-0P, G7-2P, G17-0P, G17-2P?")

if inhib in ['G7-0P','g7-0P','7-0P','G7-0p','g7-0p','7-0p','g70p','7-0']:
    raw_data = pd.read_csv('HDX_WT_G7_0P_FT_DL_Final_Data_Cluster.csv')
    protein = 'G7-0P'
elif inhib in ['G7-2P','g7-2P','7-2P','G7-2p','g7-2p','7-2p','g72p','7-2']:
    raw_data = pd.read_csv('HDX_WT_G7_2P_FT_DL_Final_Data_Cluster.csv')
    protein = 'G7-2P'
elif inhib in ['G17-0P','g17-0P','17-0P','G17-0p','g17-0p','17-0p','g170p','17-0']:
    raw_data = pd.read_csv('HDX_WT_G17_0P_FT_DL_Final_Data_Cluster.csv')
    protein = 'G17-0P'
elif inhib in ['G17-2P','g17-2P','17-2P','G17-2p','g17-2p','17-2p','g172p','17-2']:
    raw_data = pd.read_csv('HDX_WT_G17_2P_FT_DL_Final_Data_Cluster.csv')
    protein = 'G17-2P'

df = pd.DataFrame(raw_data)

start = int(input("\nInput start residue: "))
end = int(input("\nInput end residue: "))
state = input("\nG or Apo? ")
scale = input("\nLog or linear scale? ")

if state in ['Apo', 'apo', 'a', 'A']:
    state = 'Apo-0P'
elif (state in ['G', 'g']) & (protein == 'G7-0P'):
    state = 'G7-0P'
elif (state in ['G', 'g']) & (protein == 'G7-2P'):
    state = '2P-G7'
elif (state in ['G', 'g']) & (protein == 'G17-0P'):
    state = 'G17-0P'
elif (state in ['G', 'g']) & (protein == 'G17-2P'):
    state = 'G17-2P'

sub_range = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == state)]
x = sub_range.iloc[:,9]
y = sub_range.iloc[:,14]
sequence = sub_range['Sequence'].values[3]
#print(sequence)

plt.figure(figsize = (10,6))
plt.plot(x, y, marker = 's', markerfacecolor = 'r')
plot_title = [protein, str(start) + "-" + str(end), sequence]
plt.title(" ".join(plot_title))
plt.ylabel("Relative Uptake (Da)")
plt.xlabel("Exposure Time (Minutes)")

if scale in ['log', 'Log']:
    plt.yscale('log')
    plt.xscale('log')
elif scale in ['linear', 'Linear', 'lin', 'Lin']:
    plt.yscale('linear')
    plt.xscale('linear')
    

plt.show()
