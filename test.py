# First step is to import the necessary libraries.
# Ex: import requests
# What libraries do you need to accomplish this task?

import requests, csv

# Next up we need to make the API call to retrieve the data
payload={}

# import secrets and save to payload dict
with open("test-secrets.py", "rt", newline='') as csvfile:
    kreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
    for row in kreader:
        payload[row[0]]=row[2]
    print("Secrets imported!")

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
