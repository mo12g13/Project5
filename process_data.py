import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
from scipy.stats import norm

# Setting of the seaborn to be used in plotting various data
sns.set_palette('deep', desat=.3)
sns.set_context(rc={'figure.figsize': (9, 5)})
crime_data = pd.read_csv('report.csv', dtype={'report_year': datetime.datetime})


# A method that retrieve and process data for rape, violent, homicide, robberies from 1975 - 2015
def rape_violent_homicide_robbeies_percapita_from_1975_to_2015():
    violent_crimes =crime_data.ix[:, ['violent_crimes_percapita', 'rapes_percapita', 'homicides_percapita', 'assaults_percapita', 'robberies_percapita']]
    ax = sns.barplot(data=violent_crimes.dropna())
    plt.title("Rape, Violent, Robberies, Homicide Percapita Crimes from 1975-2015")
    plt.show()

# A method that process data of violence crime from 2012 - 2015


def rape_and_violent_crime_from_2012_2015():
    mask_2012_2013_2014_2015 = (crime_data.report_year == '2012') | (crime_data.report_year == '2013') | (crime_data.report_year == '2014') | (crime_data.report_year == '2015')
    data = crime_data[mask_2012_2013_2014_2015]
    data = data.ix[:, ['rapes_percapita', 'violent_crimes_percapita']]
    sns.barplot(data=data.dropna())
    plt.xlabel("Name of Crime")
    plt.ylabel("Number In Crimes")
    plt.title('Rape Crimes from 2012-2015')
    plt.show()

# A method that process data rape crime of capita from 1975 - 2015


def rape_crime_per_capita_from_1975_to_2015():
    rape_crime = crime_data.ix[:, ['rapes_percapita', 'report_year']]
    sns.distplot(rape_crime.rapes_percapita.dropna(),fit=norm, kde=False, color='r', bins=25)
    plt.title("Rape Crime percapita from 1975-2015")
    plt.show()

# A method that process data of violent crime from 2012 to 2015
def violent_crime_from_2012_to_2015():
    mask_2012_2013_2014_2015 = (crime_data.report_year == '2012') | (crime_data.report_year == '2013') | (crime_data.report_year == '2014') | (crime_data.report_year == '2015')
    violent_crimes = crime_data[mask_2012_2013_2014_2015]
    violent_crimes = violent_crimes.ix[:, ['violent_crimes_percapita', 'report_year']]
    violent_crimes = violent_crimes.set_index('report_year')
    plt.hist(violent_crimes.violent_crimes_percapita.dropna(), bins=25)
    plt.title("Violent crimes from 2012-2015")
    plt.plot()
    plt.show()


