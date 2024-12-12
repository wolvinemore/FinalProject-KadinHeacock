# imports
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Saves the graphs to the Charts file
if not os.path.exists("Charts"):
    os.mkdir("Charts")

# Reading the .csv file
data = pd.read_csv( filepath_or_buffer= 'WLD_RTP_details_2023-10-02.csv', index_col=0, parse_dates=True)

country = [""]

df = pd.DataFrame(data)

# Used to grab the 2 columns needed for the graph
def col():

    for col in df.columns:
        series = df[col]

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': '118.25.6.39',
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': 'YOUR_OWN_API_KEY'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)


# Formatted output
decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))