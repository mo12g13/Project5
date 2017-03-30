import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
from scipy.stats import norm

# Setting of the seaborn in order to be used in plotting various data
sns.set_palette('deep', desat=.3)
sns.set_context(rc={'figure.figsize': (9, 6)})
# Reading of the data from the report.csv file. The year is in float so I have to convert to datetime
crime_data = pd.read_csv('report.csv', dtype={'report_year': datetime.datetime})


# A method that retrieve and process data for rape, violent, homicide, robberies from 1975 - 2015
# Drop all nan from the data and retrieve the violent_crime_percapita
# rapes_percapita, homicide_percapita, assult_percapita and robberies_percapita
def rape_violent_homicide_robbeies_percapita_from_1975_to_2015():
    violent_crimes =crime_data.ix[:, ['violent_crimes_percapita', 'rapes_percapita', 'homicides_percapita', 'assaults_percapita', 'robberies_percapita']]
    sns.barplot(data=violent_crimes.dropna())
    plt.title("Rape, Violent, Robberies, Homicide Percapita Crimes from 1975-2015")
    plt.ylabel("Crimes in Numbers")
    plt.xlabel("\nCrimes")
    plt.show()

# A method that process data of violence and rape crimes from 2012 - 2015 per capita.
# I am comparing the rape and violent crimes from 2012-2015 in order to see the trend of these two crimes
# Retrieve all data with the year is 2012, 2013,, 2014 and 2015. Drop all nan

def rape_and_violent_crime_percapita_from_2012_2015():
    mask_2012_2013_2014_2015 = (crime_data.report_year == '2012') | (crime_data.report_year == '2013') | (crime_data.report_year == '2014') | (crime_data.report_year == '2015')
    data = crime_data[mask_2012_2013_2014_2015]
    data = data.ix[:, ['rapes_percapita', 'violent_crimes_percapita']]
    sns.barplot(data=data.dropna())
    plt.xlabel("Name of Crime")
    plt.ylabel("Crimes in Numbers")
    plt.title('Rape and violent Crimes from 2012-2015')
    plt.show()

# A method that process data of rape crime per capita from 1975 - 2015
# Drop all nan and retrieve the data for rapes_percapita and report_year
# I want to visualize the trend of rape from 1975 - 2015
def rape_crime_per_capita_from_1975_to_2015():
    rape_crime = crime_data.ix[:, ['rapes_percapita', 'report_year']]
    sns.distplot(rape_crime.rapes_percapita.dropna(),fit=norm, kde=False, color='r', bins=25)
    plt.title("Rape Crime percapita from 1975-2015")
    plt.ylabel("Crime in Numbers")

    plt.show()

# A method that process data of violent crime from 2012 to 2015
# Trying to see the trend of violent crimes from 2012-2015. That's, I want to see if it's decreasing or increasing
# I trying to visualize the most recent trend of violent crime from 2012-2015
def violent_crime_per_capita_from_2012_to_2015():
    mask_2012_2013_2014_2015 = (crime_data.report_year == '2012') | (crime_data.report_year == '2013') | (crime_data.report_year == '2014') | (crime_data.report_year == '2015')
    violent_crimes = crime_data[mask_2012_2013_2014_2015]
    violent_crimes = violent_crimes.ix[:, ['violent_crimes_percapita', 'report_year']]
    violent_crimes = violent_crimes.set_index('report_year')
    plt.hist(violent_crimes.violent_crimes_percapita.dropna(), bins=25)
    plt.title("Violent crimes from 2012-2015")
    plt.plot()
    plt.show()

# Assault crime per capita from 1975 - 2015
# What is the trend of assault crime from 1975 -2015?
# This graph answers this question

def assault_crime_per_capita_from_1975_2015():
    data_of_assault_per_capita = crime_data.ix[:, ['assaults_percapita', 'report_year']]
    sns.distplot(data_of_assault_per_capita.assaults_percapita.dropna(), fit=norm, kde=False, color='r', bins=25)
    plt.show()

# Average rape crime per capita from 1975 - 2015
# What is the average rape crime trend per capita from 1975 - 2015? This method answers that question
def average_rape_crime_from_1975_2015():
    grouped = crime_data.groupby('report_year').mean()
    plt.plot(grouped['rapes_percapita'])
    plt.xlabel("Year from 1975 - 2015")
    plt.ylabel("Average number of crime from 1975 - 2015")
    plt.title("Average rape crime from 1975-2015")
    plt.show()


# Average assault crime per capita from 1975-2015. What is the average and trend of assault crime from 1975-2015
def average_assault_crime_from_1975_2015():
    grouped = crime_data.groupby('report_year').mean()
    plt.plot(grouped['assaults_percapita'])
    plt.xlabel('Year from 1975-2015')
    plt.ylabel('Average number of crime from 1975-2015')
    plt.title('Average assault crime from 1975-2015')
    plt.show()


if __name__=="__main__":
  average_assault_crime_from_1975_2015()


