def replace_apostrophe(a):
    b = 'bananas'
    if '`' in a:
        b = str.replace(a, '`', '\'')
    else:
        return a
    return b

import requests, csv, datetime, time
from bs4 import BeautifulSoup

delime= '`'

# TODO: adds the title a million times. website error code exit

start_time = time.time()
filename = 'redo_bb200.csv'

with open(filename, 'rb') as inp, open(filename, 'wb') as out:
    csvwriter = csv.writer(out)
    for row in csv.reader(inp):
        csvwriter.writerow(row)

today = datetime.datetime.now()
start_date = datetime.datetime(1963, 8, 17)
week_increment = datetime.timedelta(days = 7)
length = int((today - start_date) / week_increment)

with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=delime)
        csvwriter.writerow(['Chart #', 'Album Title', 'Artist', 'Last Week', 'Peak Position', 'Weeks On Chart', 'Source Chart Date'])

for x in range(length):

    format_date = (start_date + (week_increment * x)).strftime("%Y-%m-%d")

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
        csvwriter = csv.writer(csvfile, delimiter=delime)
        
        csvwriter.writerows(billboard_arr)
        
print('To write the file it took:', str(time.time() - start_time), 'seconds')