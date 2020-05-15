# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:06:59 2020

@author: Gilgamesh
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Gilgamesh/Documents/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)