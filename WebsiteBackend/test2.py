import json, os
import urllib.parse # Turns strings into URL formatting

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
def get_artist_id():
    artist_search_query = "curl \"https://api.spotify.com/v1/search?query=" + urllib.parse.quote_plus(artist_name) + "&type=artist&locale=en-US%2Cen%3Bq%3D0.5&offset=0&limit=20\" -H \"Authorization: Bearer  " + access_token + "\" > artists.json 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
    with open('artists.json', 'r') as f:
        data = json.load(f)
        return data['artists']['items'][0]['id']
    
    
test_str = 'https://open.spotify.com/artist/3MZsBdqDrRTJihTHQrO6Dq'
test_str = test_str[32:]
print(test_str)
print(test_str.__len__())

