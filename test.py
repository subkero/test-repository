# First step is to import the necessary libraries.
# Ex: import requests
# What libraries do you need to accomplish this task?

import requests, csv


# Next up we need to make the API call to retrieve the data

payload={'appKey':"93b8237f9d7f487c8e08d08fbef51400eb4d1073e9d549b9bc2821bdf13c73d2",
'apiKey':"783ff6a8d19744f6a05a7e61e7bbf9b21db3b39f44e74146b338bde4b2a15aa2",
'macAddress':"C0:21:0D:1F:04:EC",
'urlBase':"https://api.ambientweather.net/v1/devices/"}

#extract correct url

payload['applicationKey'] = payload.pop('appKey')
url=payload['urlBase']+payload['macAddress']

r=requests.get(url,params=payload) # get request

# store data
temp_data=r.json()


# Once we have the data, we need to get it in the format we want
# Think about the end product, we need a CSV file that clearly displays the data to the user

# align formatted column names with obtained fieldnames
column_names=['Temperature (F)', 'Humidity (%)','Wind Speed (mph)',
              'Wind Gust (mph)','Daily Rainfall Totals (in)',
              'Monthly Rainfall Totals (in)','Yearly Rainfall Totals (in)',
              'UV Radiation Index','Date/Time']

dict_keys=['tempf', 'humidity',
           'windspeedmph', 'windgustmph','dailyrainin',
           'monthlyrainin', 'yearlyrainin', 
           'uv', 'date']

# make a nested table of column names aligned with values. First row headers.
data_nestList=[column_names]

for j in range(len(temp_data)):       # No. of records
    l=[]
    for x in range(len(dict_keys)):   # One for each field
        if x==0:
            # goldilocks condition
            if temp_data[j][dict_keys[x]]< 65:
                l.append("Too cold")
            elif temp_data[j][dict_keys[x]]>80:
                l.append("Too hot")
            else:
                l.append("Goldilocks")

        else:                         # record corresponding value
            l.append(temp_data[j][dict_keys[x]])


    data_nestList.append(l)


# Once we have the data where we want it, we need to write the CSV file

# helper function
def write_csv_file(nested_table, file_name, file_delimiter):
    """
    Given a nested list table, writes the data into a
    CSV file with the name file_name
    """
    
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=file_delimiter)
        for row in nested_table:
            csv_writer.writerow(row)
    print("File successfully made!")
    
write_csv_file(data_nestList,'Library_weather.csv',',') # call function
