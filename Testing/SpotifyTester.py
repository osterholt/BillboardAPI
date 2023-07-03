# Written by Cam Osterholt c. 04/10/2023

# TODO: find a way to bipass csv editing.
#       figure out how to only work at status 200

# Goal is to successfully get a request for: Joji
# Joji has 4 Albums:
#   1. In Tongues (2018)
#   2. BALLANDS 1 (2018)
#   3. Nectar (2020)
#   4. SMITHEREENS (2022)

# Helpful Links and Commands:
#   os.system(ARGS) - ARGS outputs to command line. 
#   sys.argv[1:] - All the flags inputted with python filename 

import sys, os, json

os.system("echo \"Hello World\"") #TODO: Remove but I like it now.


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
    artist_name = input("Enter the name of the artist: ")
    artist_search_query = "curl \"https://api.spotify.com/v1/search?query=" + artist_name + "&type=artist&locale=en-US%2Cen%3Bq%3D0.5&offset=0&limit=20\" -H \"Authorization: Bearer  " + spotify_access_token + "\" > artists.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
    with open('artists.json', 'r') as f:
        data = json.load(f)
        return data['artists']['items'][0]['id']
    
def get_albums():
    #TODO: 
    artist_search_query = "curl \"https://api.spotify.com/v1/artists/" + artist_id + "/albums?offset=0&limit=50&include_groups=album&locale=en-US,en;q=0.5\" -H \"Authorization: Bearer  " + spotify_access_token + "\" > albums.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
        
spotify_access_token = request_access_token() # gets access token for all requests. Must be called before artist_id.
artist_id = get_artist_id()
get_albums()





