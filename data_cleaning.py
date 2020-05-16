# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:04:52 2020

@author: Gilgamesh
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#
# TODO

# Clean and Parse
# Salary Estimate:
df = df[df['Salary Estimate']!='1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
no_kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

df['min_salary'] = no_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = no_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

# Company Name; Ratings
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)



# State field
df['job_state'] = df['Location'].apply(lambda x: x.split(', ')[-1])
df['job_state'] = df['job_state'].apply(lambda x: x.replace('United States', 'USA').replace('California', 'CA').replace('New York State', 'NY').replace('New Jersey', 'NJ').replace('Virginia','VA'))
df['some_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)

# Age of Company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

# Job Description 

# -Python
df['python_js'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#df['python_js'].value_counts()

# -R Studio
df['r_js'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
#df['r_js'].value_counts()

# -Spark
df['spark_js'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#df.spark_js.value_counts()

# -Data Mining
df['mining_js'] = df['Job Description'].apply(lambda x: 1 if 'mining' in x.lower() else 0)
#df['mining_js'].value_counts()

