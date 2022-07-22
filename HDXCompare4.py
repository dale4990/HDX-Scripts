import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

inhib1 = input("\nFirst inhbitor to plot? ")
inhib2 = input("\nSecond inhbitor to plot? ")
inhib3 = input("\nThird inhbitor to plot? ")
inhib4 = input("\nFourth inhbitor to plot? ")

#Replace csv names for rawdata here

def select_inhib(inhib, rawdata, protein, df):
    if inhib in ['Apo', 'apo']:
        rawdata = pd.read_csv('Apo-NP.csv')
        protein = 'Apo-NP'
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G1-0P','g1-0P','1-0P,''G1-0p','g1-0p','1-0p','g10p','1-0']:
        rawdata = pd.read_csv('G1-0P.csv')
        protein = 'G1-0P'
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G2-0P','g2-0P','2-0P,''G2-0p','g2-0p','2-0p','g20p','2-0']:
        rawdata = pd.read_csv('G2-0P.csv')
        protein = 'G2-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G3-0P','g3-0P','3-0P,''G3-0p','g3-0p','3-0p','g30p','3-0']:
        rawdata = pd.read_csv('G3-0P.csv')
        protein = 'G3-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G6-0P','g6-0P','6-0P','G6-0p','g6-0p','6-0p','g60p','6-0']:
        rawdata = pd.read_csv('G6-0P.csv')
        protein = 'G6-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G7-0P','g7-0P','7-0P','G7-0p','g7-0p','7-0p','g70p','7-0']:
        rawdata = pd.read_csv('G7-0P.csv')
        protein = 'G7-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G8-0P','g8-0P','8-0P','G8-0p','g8-0p','8-0p','g80p','8-0']:
        rawdata = pd.read_csv('G8-0P.csv')
        protein = 'G8-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G9-0P','g9-0P','9-0P''G9-0p','g9-0p','9-0p','g90p','9-0']:
        rawdata = pd.read_csv('G9-0P.csv')
        protein = 'G9-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G10-0P','g10-0P','10-0P','G10-0p','g10-0p','10-0p','g100p','10-0']:
        rawdata = pd.read_csv('G10-0P.csv')
        protein = 'G10-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G11-0P','g11-0P','11-0P','G11-0p','g11-0p','11-0p','g110p','11-0']:
        rawdata = pd.read_csv('G11-0P.csv')
        protein = 'G11-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G12-0P','g12-0P','12-0P','G12-0p','g12-0p','12-0p','g120p','12-0']:
        rawdata = pd.read_csv('G12-0P.csv')
        protein = 'G12-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G13-0P','g13-0P','13-0P','G13-0p','g13-0p','13-0p','g130p','13-0']:
        rawdata = pd.read_csv('G13-0P.csv')
        protein = 'G13-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G14-0P','g14-0P','14-0P','G14-0p','g14-0p','14-0p','g140p','14-0']:
        rawdata = pd.read_csv('G14-0P.csv')
        protein = 'G14-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G15-0P','g15-0P','15-0P','G15-0p','g15-0p','15-0p','g150p','15-0']:
        rawdata = pd.read_csv('G15-0P.csv')
        protein = 'G15-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G16-0P','g16-0P','16-0P','G16-0p','g16-0p','16-0p','g160p','16-0']:
        rawdata = pd.read_csv('G16-0P.csv')
        protein = 'G16-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df
            
    elif inhib in ['G17-0P','g17-0P','17-0P','G17-0p','g17-0p','17-0p','g170p','17-0']:
        rawdata = pd.read_csv('G17-0P.csv')
        protein = 'G17-0P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G18-0P','g18-0P','18-0P','G18-0p','g18-0p','18-0p','g180p','18-0']:
        rawdata = pd.read_csv('G18-0P.csv')
        protein = 'G19-0P'    
        df = pd.DataFrame(rawdata)  
        return rawdata, protein, df   

    elif inhib in ['G19-0P','g19-0P','19-0P','G19-0p','g19-0p','19-0p','g190p','19-0']:
        rawdata = pd.read_csv('G19-0P.csv')
        protein = 'G19-0P'  
        df = pd.DataFrame(rawdata)

    elif inhib in ['G1-2P','g1-2P','1-2P,''G1-2p','g1-2p','1-2p','g12p','1-2']:
        rawdata = pd.read_csv('G1-2P.csv')
        protein = 'G1-2P'
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G2-2P','g2-2P','2-2P,''G2-2p','g2-2p','2-2p','g22p','2-2']:
        rawdata = pd.read_csv('G2-2P.csv')
        protein = 'G2-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G3-2P','g3-2P','3-2P,''G3-2p','g3-2p','3-2p','g32p','3-2']:
        rawdata = pd.read_csv('G3-2P.csv')
        protein = 'G3-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G6-2P','g6-2P','6-2P','G6-2p','g6-2p','6-2p','g62p','6-2']:
        rawdata = pd.read_csv('G6-2P.csv')
        protein = 'G6-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G7-2P','g7-2P','7-2P','G7-2p','g7-2p','7-2p','g72p','7-2']:
        rawdata = pd.read_csv('G7-2P.csv')
        protein = 'G7-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G8-2P','g8-2P','8-2P','G8-2p','g8-2p','8-2p','g82p','8-2']:
        rawdata = pd.read_csv('G8-2P.csv')
        protein = 'G8-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G9-2P','g9-2P','9-2P''G9-2p','g9-2p','9-2p','g92p','9-2']:
        rawdata = pd.read_csv('G9-2P.csv')
        protein = 'G9-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G10-2P','g10-2P','10-2P','G10-2p','g10-2p','10-2p','g102p','10-2']:
        rawdata = pd.read_csv('G10-2P.csv')
        protein = 'G10-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df
        
    elif inhib in ['G11-2P','g11-2P','11-2P','G11-2p','g11-2p','11-2p','g112p','11-2']:
        rawdata = pd.read_csv('G11-2P.csv')
        protein = 'G11-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G12-2P','g12-2P','12-2P','G12-2p','g12-2p','12-2p','g122p','12-2']:
        rawdata = pd.read_csv('G12-2P.csv')
        protein = 'G12-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G13-2P','g13-2P','13-2P','G13-2p','g13-2p','13-2p','g132p','13-2']:
        rawdata = pd.read_csv('G13-2P.csv')
        protein = 'G13-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G14-2P','g14-2P','14-2P','G14-2p','g14-2p','14-2p','g142p','14-2']:
        rawdata = pd.read_csv('G14-2P.csv')
        protein = 'G14-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G15-2P','g15-2P','15-2P','G15-2p','g15-2p','15-2p','g152p','15-2']:
        rawdata = pd.read_csv('G15-2P.csv')
        protein = 'G15-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G16-2P','g16-2P','16-2P','G16-2p','g16-2p','16-2p','g162p','16-2']:
        rawdata = pd.read_csv('G16-2P.csv')
        protein = 'G16-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df
            
    elif inhib in ['G17-2P','g17-2P','17-2P','G17-2p','g17-2p','17-2p','g172p','17-2']:
        rawdata = pd.read_csv('G17-2P.csv')
        protein = 'G17-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

    elif inhib in ['G18-2P','g18-2P','18-2P','G18-2p','g18-2p','18-2p','g182p','18-2']:
        rawdata = pd.read_csv('G18-2P.csv')
        protein = 'G18-2P'    
        df = pd.DataFrame(rawdata)   
        return rawdata, protein, df  

    elif inhib in ['G19-2P','g19-2P','19-2P','G19-2p','g19-2p','19-2p','g192p','19-2']:
        rawdata = pd.read_csv('G19-2P.csv')
        protein = 'G19-2P' 
        df = pd.DataFrame(rawdata)
        return rawdata, protein, df

rawdata1 = None
rawdata2 = None
rawdata3 = None
rawdata4 = None

protein1 = None
protein2 = None
protein3 = None
protein4 = None

df1 = None
df2 = None
df3 = None
df4 = None

dt1 = select_inhib(inhib1, rawdata1, protein1, df1)
dt2 = select_inhib(inhib2, rawdata2, protein2, df2)
dt3 = select_inhib(inhib3, rawdata3, protein3, df3)
dt4 = select_inhib(inhib4, rawdata4, protein4, df4)

#dt[0] = rawdata, dt[1] = protein, dt[2] = dataframe

start = int(input("\nInput start residue: "))
end = int(input("\nInput end residue: "))
state = input("\nG or Apo? ")
scale = input("\nLog or linear scale? ")

def set_subrange(protein, df, subrange):
    sub_0p = '0p'
    sub_0P = '0P'
    sub_2p = '2p'
    sub_2P = '2P'

    if state in ['Apo', 'apo', 'a', 'A']:
    #edge case for G7-2P 
        if protein == 'G7-2P':
            stateG7_2P_Apo = '2P-Apo'
            subrange = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == stateG7_2P_Apo)]
            return subrange
        elif (sub_0p in protein) or (sub_0P in protein):
            state_Apo_0P = 'Apo-0P'
            subrange = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == state_Apo_0P)]
            return subrange
        elif ((sub_2p in protein) or (sub_2P in protein)) and (protein != 'G7-2P'):
            state_Apo_2P = 'Apo-2P'
            subrange = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == state_Apo_2P)]
            return subrange
    elif state in ['G', 'g']:
    #edge case for G7-2P again
        if protein == 'G7-2P':
            stateG7_2P = '2P-G7'
            subrange = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == stateG7_2P)]
            return subrange
        elif (sub_0p in protein) or (sub_0P in protein):
            state_0P = protein
            subrange = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == state_0P)]
            return subrange
        elif ((sub_2p in protein) or (sub_2P in protein)) and (protein != 'G7-2P'):
            state_2P = protein
            subrange = df[(df['Start'] == start) & (df['End'] == end) & (df['State'] == state_2P)]   
            return subrange 

sub_range1 = None
sub_range2 = None
sub_range3 = None
sub_range4 = None

sr1 = set_subrange(dt1[1], dt1[2], sub_range1)
sr2 = set_subrange(dt2[1], dt2[2], sub_range2)
sr3 = set_subrange(dt3[1], dt3[2], sub_range3)
sr4 = set_subrange(dt4[1], dt4[2], sub_range4)

sequence1 = sr1['Sequence'].values[0]
sequence2 = sr2['Sequence'].values[0]
sequence3 = sr3['Sequence'].values[0]
sequence4 = sr4['Sequence'].values[0]

x1 = sr1.iloc[:,9]
y1 = sr1.iloc[:,14]
x2 = sr2.iloc[:,9]
y2 = sr2.iloc[:,14]
x3 = sr3.iloc[:,9]
y3 = sr3.iloc[:,14]
x4 = sr4.iloc[:,9]
y4 = sr4.iloc[:,14]

fig = plt.figure(figsize = (15,8))
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)
ax1.plot(x1, y1, marker = 's')
ax2.plot(x2, y2, 'tab:orange', marker = 's')
ax3.plot(x3, y3, 'tab:green', marker = 's')
ax4.plot(x4, y4, 'tab:red', marker = 's')
plot_title1 = [dt1[1], str(start) + "-" + str(end), sequence1]
plot_title2 = [dt2[1], str(start) + "-" + str(end), sequence2]
plot_title3 = [dt3[1], str(start) + "-" + str(end), sequence3]
plot_title4 = [dt4[1], str(start) + "-" + str(end), sequence4]
ax1.set_title(" ".join(plot_title1))
ax2.set_title(" ".join(plot_title2))
ax3.set_title(" ".join(plot_title3))
ax4.set_title(" ".join(plot_title4))
ax1.set_ylabel("Relative Uptake (Da)")
#ax1.set_xlabel("Exposure Time (Minutes)")
ax2.set_ylabel("Relative Uptake (Da)")
#ax2.set_xlabel("Exposure Time (Minutes)")
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

