import requests, csv
from bs4 import BeautifulSoup
from datetime import date

def replace_apostrophe(a):
    if '`' in a:
        return str.replace(a, '`', '\'')
    else:
        return a
    
def get_start_date():
    with open(filename, "r") as f:
        csvfile = f.read().split(delim)
        print(csvfile[-1])
        return date.fromisoformat(csvfile[-1])

def write_title_ln():
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=delim)
        csvwriter.writerow(['Chart #', 'Album Title', 'Artist', 'Last Week', 'Peak Position', 'Weeks On Chart', 'Source Chart Date'])

delim= '`'
filename = './Redo_Scraper/redo_bb200.csv'

today = date.today()
start_date = get_start_date()
week_increment = date.day(7)
length = int((today - start_date) / week_increment)

print(format_date = (start_date + (week_increment * 0)))

with open(filename, 'rb') as inp, open(filename, 'wb') as out:
    csvwriter = csv.writer(out)
    for row in csv.reader(inp):
        csvwriter.writerow(row)

for x in range(length):

    format_date = (start_date + (week_increment * x)) # TODO: format date correctly. 

    bb200_URL = "https://www.billboard.com/charts/billboard-200/" + format_date + "/"
    r = requests.get(bb200_URL)

    if r.status_code != 200:
        print('Error: site not reached', '\nNow Exiting...')
        SystemExit
        

    # print("Status code:", r.status_code)

    soup = BeautifulSoup(r.content, 'html.parser')
    raw_albums = soup.find_all('ul', class_="o-chart-results-list-row")

    billboard_arr = []

    for album_element in raw_albums:
        element_arr = []
        
        element_arr.append(replace_apostrophe(album_element.find("span", class_="c-label").text.strip())) # chart number
        element_arr.append(replace_apostrophe(album_element.find("h3", class_="c-title").text.strip())) # album name
        
        album_text = album_element.find('ul', class_="lrv-a-unstyle-list") 
        element_arr.append(replace_apostrophe(album_text.find('span', class_="c-label").text.strip())) # artist name
        
        li_list = album_text.find_all('li', class_="o-chart-results-list__item")
        element_arr.append(replace_apostrophe(li_list[3].find('span', class_="c-label").text.strip())) # last week
        element_arr.append(replace_apostrophe(li_list[4].find('span', class_="c-label").text.strip())) # peak position
        element_arr.append(replace_apostrophe(li_list[5].find('span', class_="c-label").text.strip())) # weeks on chart
        
        element_arr.append(format_date)
        
        billboard_arr.append(element_arr)

    with open(filename, 'a') as csvfile:
        print('Now writing', format_date)
        csvwriter = csv.writer(csvfile, delimiter=delim)
        
        csvwriter.writerows(billboard_arr)