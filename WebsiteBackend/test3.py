import csv, sys, os, json
import urllib.parse # Turns strings into URL formatting

#TODO: For Artist JOJI the () are getting in the way.

# FORMAT: {[album_name], [album_ID], [album_cover_img_url], [release_date], [peak_position], {[songs], [peak_positon]} }

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


# ----------Creates json File for the Artist's Albums----------
def get_albums():
    # FORMAT: {[album_name], [album_ID], [album_cover_img_url], [release_date], [peak_position]}
    album_file_name = "albums.json"
    billboard_200_file_name = "bb200_FE2.csv"
    delim = '`'
    
    artist_search_query = "curl \"https://api.spotify.com/v1/artists/" + artist_id + "/albums?offset=0&limit=50&include_groups=album&locale=en-US,en;q=0.5\" -H \"Authorization: Bearer  " + access_token + "\" > " + album_file_name + " 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
    

#----------------------------------------------------------------------------------------------------------------------------

# os.system("python remove.py")

print('**********************')
print('*                    *')
print('*     Welcome to     *')
print('*        WUSC        *')
print('*                    *')
print('**********************\n')
print('Written by Cam Osterholt c.2023') 
print('Please remembr to check your spelling!') 

# artist_name = input("Enter artist's name from file: ")

access_token = request_access_token()
artist_id = '3MZsBdqDrRTJihTHQrO6Dq'

get_albums()

# os.system("python remove.py")