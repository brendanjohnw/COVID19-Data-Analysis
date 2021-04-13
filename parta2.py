import pandas as pd
import argparse
import matplotlib.pyplot as plt
from numpy import arange
##

grouped_covid = pd.read_csv("owid-covid-data-2020-monthly.csv",encoding = "ISO-8859-1")
loc_cfr_nc = grouped_covid[['location','case_fatality_rate','new_cases']]
loc_cfr_nc = loc_cfr_nc.loc[loc_cfr_nc['location']!='World']
my_plot = plt.scatter(loc_cfr_nc.iloc[:,2],loc_cfr_nc.iloc[:,1],s = 10,
                     facecolors = 'none', edgecolors = 'r')
plt.xticks(rotation = 45)
plt.xlabel("new cases")
plt.ylabel("case fatality rate (CFR)")
plt.title("case fatality rate and new cases by location")
plt.grid(True)
plt.savefig('scatter-a.png')
plt.show()

 


my_plot = plt.scatter(loc_cfr_nc.iloc[:,2],loc_cfr_nc.iloc[:,1],s = 10,
                     facecolors = 'none', edgecolors = 'r')
plt.xscale('log')
plt.xlim(1)
plt.ylim(0,30)
plt.xticks(rotation = 45)
plt.xlabel("new cases")
plt.ylabel("case fatality rate (CFR)")
plt.title("case fatality rate and new cases by location (log scale)")
plt.grid(True)
plt.savefig('scatter-b.png')
plt.show()

