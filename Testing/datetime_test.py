import requests, csv
from bs4 import BeautifulSoup
from datetime import date

# FORMAT: {
    # 0 - Chart #
    # 1 - Album Name
    # 2 - Artist Name 
    # 3 - Last Week
    # 4 - Peak POS
    # 5 - Weeks on Chart
    # 6 - Chart Date
    # } 

filename = './Testing/test.csv'
delim = '`'

# with open(filename, 'r') as bb_file:
    
#     reader = csv.reader(bb_file, delimiter=delim)
#     for line in reader:
#         chart_date = date.fromisoformat(line[6])
#         print(chart_date)

with open(filename, "r") as f:
        csvfile = f.read().split(delim)
        print(csvfile[-1])