#Written by Cam Osterholt c. 2023

import csv, sys, os, json
import urllib.parse # Turns strings into URL formatting

# TODO: 
# - Invalid input when put string instead of 0-2 choice.
# - Give reccomended songs for artists.

# TO RETURN:
# 1. Artist Name
# 2. Artist ID
# 3. Number of top 40 albums
    

def sort_artist_album_chart_info():
    #TODO: In this we will open the billboard bb200_BE2.csv file.
    
    # FORMAT: {[album_name], [album_ID], [album_cover_img_url], [release_date], [peak_position]}
    
    # Goes through each line to determine if the artist's name is there. 
    # if the name is there it checks if it exists in the album folder given by spotify. 
    # if it is found then it checks if it has charted higher. if true modifies the peak pos value. 
    print("DEBUG: ")

# ----------Request Access Token----------
def request_access_token():
    client_id = "3e14df7c9d0647a785aea8c5559f0927"
    client_secret = "afdaf4f47c294893a2b6a96989a47e72"

    access_token_request = "curl -X POST \"https://accounts.spotify.com/api/token\" -H \"Content-Type: application/x-www-form-urlencoded\" -d \"grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret+ "\" > access.json 2> /dev/null" #TODO: Find a way to not have stderr go to a file.
    os.system(access_token_request)
    
    with open("access.json", "r") as f:
        data = json.load(f)
        return data["access_token"] # returns the access token from the json file. 
    
# ----------Returns the Artist's Spotify ID----------
def get_artist_id():
    artist_search_query = "curl \"https://api.spotify.com/v1/search?query=" + urllib.parse.quote_plus(artist_name) + "&type=artist&locale=en-US%2Cen%3Bq%3D0.5&offset=0&limit=20\" -H \"Authorization: Bearer  " + spotify_access_token + "\" > artists.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
    with open('artists.json', 'r') as f:
        data = json.load(f)
        return data['artists']['items'][0]['id']

# ----------Creates json File for the Artist's Albums----------
def get_albums():
    #TODO: make output file modular
    artist_search_query = "curl \"https://api.spotify.com/v1/artists/" + artist_id + "/albums?offset=0&limit=50&include_groups=album&locale=en-US,en;q=0.5\" -H \"Authorization: Bearer  " + spotify_access_token + "\" > albums.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.

# ---------------------------------------------------------------------------------------------------------------- #

os.system("rm -f *.json")

delime = '`'

filename200 = 'bb200_FE2.csv'
bb200 = []
filename100 = 'bb100_FE2.csv'
bb100 = []
album_arr = []
final_arr = []

#with open(filename200) as file_input:
#    csvreader = csv.reader(file_input, delimiter=delime)
#    for lines in file_input:
#        line = lines.split('`')
#        line[6] = line[6].strip()
#        bb200.append(line)
#with open(filename100) as file_input:
#    csvreader = csv.reader(file_input, delimiter=delime)
#    for lines in file_input:
#        line = lines.split('`')
#        line[6] = line[6].strip()
#        bb100.append(line)

print('**********************')
print('*                    *')
print('*     Welcome to     *')
print('*        WUSC        *')
print('*                    *')
print('**********************\n')
print('Written by Cam Osterholt c.2023') 
print('Please remembr to check your spelling!') 

artist_name = input("Enter artist's name or spotify URL: ") # TODO: implement spotify URL parsing
spotify_access_token = request_access_token()
artist_id = get_artist_id()

# At this point we have the access token for PATH requests and the ID for all other requests. 



os.system('python remove.py')