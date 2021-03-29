import pandas as pd
import argparse
# covid_cases is of type DataFrame
# covid_days is the DataFrame that stores data for only days and months with covid cases depending on location
covid_cases = pd.read_csv('owid-covid-data.csv', encoding = 'ISO-8859-1')
covid_cases['year'] = pd.DatetimeIndex(covid_cases['date']).year
covid_cases['month'] = pd.DatetimeIndex(covid_cases['date']).month
covid_cases = covid_cases.loc[covid_cases['year']==2020]
covid_cases = (covid_cases.loc[:,['location','month','total_cases','new_cases','total_deaths','new_deaths']])
covid_days = covid_cases[(covid_cases['total_cases']>0)] 
covid_days=covid_days.loc[covid_days['location']!='World']
new_cases = covid_days.groupby(['location','month'])['new_cases'].sum()
new_deaths = covid_days.groupby(['location','month'])['new_deaths'].sum()
covid_days = covid_days.drop(['new_cases','new_deaths'],1)
grouped_covid = covid_days.groupby(['location','month']).tail(1)
grouped_covid = grouped_covid.merge(new_cases, on = ['location', 'month']).merge(new_deaths, on = ['location', 'month'])
grouped_covid = grouped_covid[['location','month','total_cases','new_cases','total_deaths','new_deaths']]
print(grouped_covid)


case_fatality_rate = (grouped_covid['total_deaths']/grouped_covid['total_cases'])*100
grouped_covid.insert(2,'case_fatality_rate',case_fatality_rate, allow_duplicates = False)
grouped_covid = grouped_covid.loc[grouped_covid['case_fatality_rate']>0]
print(grouped_covid.head())

grouped_covid.to_csv(r'owid-covid-data-2020-monthly.csv', index = False)