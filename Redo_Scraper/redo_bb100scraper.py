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

def replace_apostrophe(a):
    b = 'bananas'
    if '`' in a:
        b = str.replace(a, '`', '\'')
    else:
        return a
    return b

# TODO: current error is comparing file's date to current day. 
def get_start_date():
    with open(filename, 'r', newline = '') as bbFile:
        sd = "1960-01-01"
        reader = csv.reader(bbFile, delimiter=delime)
        for line in reader:
            try:
                if date.fromisoformat(line[line.__len__() - 1]) > date.today():
                    sd = line[line.__len__() - 1]
            except: 
                print("Date:", line[line.__len__() - 1], "is invalid.")
        return sd

delime= '`'

# TODO: adds the title a million times. website error code exit

filename = './Redo Scraper/redo_bb100.csv'

# with open(filename, 'rb') as inp, open(filename, 'wb') as out:
#     csvwriter = csv.writer(out)
#     for row in csv.reader(inp):
#         csvwriter.writerow(row)

today = date.today()
start_date = get_start_date()
week_increment = datetime.timedelta(days = 7)
length = int((today - start_date) / week_increment)

# with open(filename, 'a') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=delime)
#         csvwriter.writerow(['Chart #', 'Song Title', 'Artist', 'Last Week', 'Peak Position', 'Weeks On Chart', 'Source Chart Date'])

for x in range(length):

    format_date = (start_date + (week_increment * x)).strftime("%Y-%m-%d")

    bb100_URL = "https://www.billboard.com/charts/hot-100/" + format_date + "/"
    r = requests.get(bb100_URL)

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
        