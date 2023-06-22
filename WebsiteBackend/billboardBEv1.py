#Written by Cam Osterholt c. 2023

import csv, sys, os, json
import urllib.parse

# TODO: 
# - Invalid input when put string instead of 0-2 choice.
# - Give reccomended songs for artists.
# - Find songs that have commas.
    
def sort_by_artist():
    print('--------------------------------------------------------------------')
    if(str.lower(artist_name) == 'menu'):
        return
    
    # Billboard Top 200 Loop:
    num_top40 = 0
    for rows in bb200:
    #if row is by an artist, only add if the album is not yet in the array or if in the array and position is lower than previous position
        if(str.lower(rows[2]) == str.lower(artist_name)):
            in_album_arr = False
            for album_row in album_arr:
                if(str.lower(rows[1]) == str.lower(album_row[1]) and int(rows[0]) < int(album_row[0])):
                    in_album_arr = True
                    if (int(album_row[0]) > 40 and int(rows[0]) < 41): 
                        num_top40 += 1
                    # Below can be changed to add more information in the future.
                    album_arr[album_arr.index(album_row)] = [rows[0], rows[1]]
                elif(str.lower(rows[1]) == str.lower(album_row[1])):
                    in_album_arr = True
            # print('DEBUG: in_album_arr =', in_album_arr)
            if(not in_album_arr):
                if(int(rows[0]) < 40): 
                    num_top40 += 1
                # print('DEBUG: rows[0] =', rows[0], 'and rows[1] =', rows[1])
                album_arr.append([rows[0], rows[1]])
    if (len(album_arr) == 0):
        print("No Exact Album Matches Found.\nNow Searching for Partial Matches:")
        num_top40 = 0
        for rows in bb200:
        #if row is by an artist, only add if the album is not yet in the array or if in the array and position is lower than previous position
            if(str.lower(rows[2]).__contains__(str.lower(artist_name))):
                in_album_arr = False
                for album_row in album_arr:
                    if(str.lower(rows[1]).__contains__(str.lower(album_row[1])) and int(rows[0]) < int(album_row[0])):
                        in_album_arr = True
                        if (int(album_row[0]) > 40 and int(rows[0]) < 41): 
                            num_top40 += 1
                        # Below can be changed to add more information in the future.
                        album_arr[album_arr.index(album_row)] = [rows[0], rows[1]]
                    elif(str.lower(rows[1]).__contains__(str.lower(album_row[1]))):
                        in_album_arr = True
                # print('DEBUG: in_album_arr =', in_album_arr)
                if(not in_album_arr):
                    if(int(rows[0]) < 40): 
                        num_top40 += 1
                    # print('DEBUG: rows[0] =', rows[0], 'and rows[1] =', rows[1])
                    album_arr.append([rows[0], rows[1]])
    
    # Billboard Hot 100 Loop:
    song_arr = []
    num_top50 = 0
    for rows in bb100:
    #if row is by an artist, only add if the sony is not yet in the array or if in the array and position is lower than previous position
        if(str.lower(rows[2]) == str.lower(artist_name)):
            in_song_arr = False
            for song_row in song_arr:
                if(str.lower(rows[1]) == str.lower(song_row[1]) and int(rows[0]) < int(song_row[0])):
                    in_song_arr = True
                    if (int(song_row[0]) > 50 and int(rows[0]) < 51): 
                        num_top50 += 1
                    # Below can be changed to add more information in the future.
                    song_arr[song_arr.index(song_row)] = [rows[0], rows[1]]
                elif(str.lower(rows[1]) == str.lower(song_row[1])):
                    in_song_arr = True
            if(not in_song_arr):
                if(int(rows[0]) < 50): 
                    num_top50 += 1
                song_arr.append([rows[0], rows[1]])

# ----------Request Access Token----------
def request_access_token():
    client_id = "3e14df7c9d0647a785aea8c5559f0927"
    client_secret = "afdaf4f47c294893a2b6a96989a47e72"

    access_token_request = "curl -X POST \"https://accounts.spotify.com/api/token\" -H \"Content-Type: application/x-www-form-urlencoded\" -d \"grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret+ "\" > access.json 2> /dev/null" #TODO: Find a way to not have stderr go to a file.
    os.system(access_token_request)
    
    with open("access.json", "r") as f:
        data = json.load(f)
        return data["access_token"] # returns the access token from the json file. 
    
# ----------Add Artist to Queue----------
def get_artist_id():
    artist_search_query = "curl \"https://api.spotify.com/v1/search?query=" + urllib.parse.quote_plus(artist_name) + "&type=artist&locale=en-US%2Cen%3Bq%3D0.5&offset=0&limit=20\" -H \"Authorization: Bearer  " + spotify_access_token + "\" > artists.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
    with open('artists.json', 'r') as f:
        data = json.load(f)
        return data['artists']['items'][0]['id']

# ----------Returns an Artist's Albums----------
def get_albums():
    #TODO: 
    artist_search_query = "curl \"https://api.spotify.com/v1/artists/" + artist_id + "/albums?offset=0&limit=50&include_groups=album&locale=en-US,en;q=0.5\" -H \"Authorization: Bearer  " + spotify_access_token + "\" > albums.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.

# ----------Creates Final Array----------
def get_ret_array():
    # we will go through each album and create a return array. 
    # format: {album_name, peak_position, image_url}
    
    #this adds all spotify albums to the final array. it is now 1 dimentional.
    for item in spotify_albums:
        final_arr.append([item])

    # It loops through the albums in the return array and finds if their name is
    # equal to a album that charted. 
    for album in final_arr:
        for item in album_arr:
            if(album == item[1]):
                album.append(item[0])
        
    # cleans up the albums that did not chart.             
    for album in final_arr:
        if(album.len == 1):
            album.append("N/A")
    

    with open('albums.json', 'r') as f:
        data = json.load(f)
        #for item in data['']:

    return final_arr

# ---------------------------------------------------------------------------------------------------------------- #

os.system("rm -f *.json")

delime = '`'

filename200 = 'bb200_FE2.csv'
bb200 = []
filename100 = 'bb100_FE2.csv'
bb100 = []
album_arr = []
final_arr = []

with open(filename200) as file_input:
    csvreader = csv.reader(file_input, delimiter=delime)
    for lines in file_input:
        line = lines.split('`')
        line[6] = line[6].strip()
        bb200.append(line)
with open(filename100) as file_input:
    csvreader = csv.reader(file_input, delimiter=delime)
    for lines in file_input:
        line = lines.split('`')
        line[6] = line[6].strip()
        bb100.append(line)

print('**********************')
print('*                    *')
print('*     Welcome to     *')
print('*        WUSC        *')
print('*                    *')
print('**********************\n')
print('Written by Cam Osterholt c.2023') 
print('Please remembr to check your spelling!') 

artist_name = input("Enter artist's name from file: ")
spotify_access_token = request_access_token()
artist_id = get_artist_id()

# At this point we have the access token for PATH requests and the ID for all other requests. 



# os.system(python remove.py)