# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N0gPsJF9bhDycC-EF8XYPnzCBkmx0x5e
"""

import pandas as pd
df = pd.read_csv('Air_Traffic_Passenger_Statistics.csv')
df.drop(columns=['Operating Airline','Operating Airline IATA Code','Published Airline','Published Airline IATA Code','GEO Region','Activity Type Code','Price Category Code','Terminal','Boarding Area'],inplace=True)
df.head()

df1=df.groupby(['Activity Period','GEO Summary'],as_index=False)['Passenger Count'].sum()
df1['Activity Period'] = pd.to_datetime((df1['Activity Period']), format='%Y%m')

import plotly.express as px
fig = px.line(df1, x="Activity Period", y="Passenger Count", color='GEO Summary')
fig.show()

import json
data = df1.to_dict('records')
with open('/content/Air_Traffic_Passenger_Statistics'+'.json', 'w', encoding='utf-8') as f:
            json.dump(df1.to_json(orient="records"), f, ensure_ascii=False, indent=4)