# Written by Cam Osterholt
# c. 07/02/2023
import csv, json, subprocess
from artist import Artist, Album, Song

'''
I hate python and their damn multiline comments. 

Here are the steps we need to consolidate the information into MongoDB

1. Sort the BB files alphabetically by artist name to bring the artist's different albums together.
2. Consolidate artist's peak information into one array. This is sorted by their ID, recieved by the spotify API.
3.
'''

# 200 FORMAT: {
    # 0 - Chart #
    # 1 - Album Name
    # 2 - Artist Name 
    # 3 - Last Week
    # 4 - Peak POS
    # 5 - Weeks on Chart
    # 6 - Chart Date
    # } 

# client_id = "3e14df7c9d0647a785aea8c5559f0927"
# client_secret = "afdaf4f47c294893a2b6a96989a47e72"

def print_last_num(num: int, arr: Artist = []) -> None:
    for i in range (-num, -1, 1):
        print(arr[i])
        
def get_test_file(filename, lines: int, arr = []):
    ## If user does not imput append it defaults to off.
    get_test_file(filename, lines, False, arr)
    
def get_test_file(filename, lines: int, append: bool, arr = []):
    mode = 'w'
    if(bool):
        mode = 'a'
    if(lines < len(arr)):
        lines = len(arr)
    filename = './MongoDB_Transfer/' + filename
    if(not filename[-4:] == '.csv'):
        filename = filename + '.csv'
    with open(filename, mode=mode) as f:
        csvwriter = csv.writer(f, delimiter=delim)
        for i in range(lines):
            csvwriter.writerow(arr[i])

def dump_to_json(input: str):
    json_filename = './MongoDB_Transfer/test.json'
    with open(json_filename, 'a') as f:
        json.dump(input, f, indent=4)

# TODO: fix, giving error when iterating through artists
def print_artists():
    for i in artists:
        print(i.__str__)
        for al in i.num_albums():
            print(i.albums[al].__str__)

# ----------Request Access Token----------
def request_access_token() -> str:
    return request_access_token(False)

def request_access_token(write_to_file: bool) -> str:
    access_token_request = 'curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=3e14df7c9d0647a785aea8c5559f0927&client_secret=afdaf4f47c294893a2b6a96989a47e72"'
    proc = subprocess.Popen(access_token_request, shell=True, stdout=subprocess.PIPE, )
    output = json.loads(proc.communicate()[0])
    sapi_access = output['access_token']
    print(f'sapi_access = {sapi_access}')
    if(write_to_file):
        with open('./MongoDB_Transfer/sapi_access.json', 'w') as f:
            json.dump(output, f, indent=4)
    return sapi_access
    
    # with open("access.json", "r") as f:
    #     data = json.load(f)
    #     return data["access_token"] # returns the access token from the json file. 

r'''Returns an object of Artist when you enter a string for an artist. 
    This references the Spotify API to get an accuritely '''
def get_artist(artist_name: str) -> Artist:
    artist_request = 'curl "https://api.spotify.com/v1/search?query=' + artist_name + '&type=artist&locale=en-US%2Cen%3Bq%3D0.5&offset=0&limit=20" -H "Authorization: Bearer ' + spotify_access_token + '"'
    proc = subprocess.Popen(artist_request, shell=True, stdout=subprocess.PIPE, )
    output = json.loads(proc.communicate()[0])
    output = output['artists']['items'][00]
    art = Artist(output['id'], output['name'])
    return art


        
    

#--------------------------------------------------------------------------------------------------#

delim = '`'
bb100_file = './MongoDB_Transfer/bb100.csv'
bb200_file = './MongoDB_Transfer/bb200.csv'
bb200 = []
artists = []

last_artist_name = str
loop_file = './MongoDB_Transfer/Test200.csv'
bb200 = []

with open(loop_file, 'r') as f:
    for line in f:
        bb200.append(line.split(delim))

'''
if the artist is the previous artist, then we check to see if the album is contained in the artist. 
    if album is contained then we update the peak pos and all relevent info.
    if album is not contained them we make a new album and get song data from spotify to add to album.
    
if the artist is not the previous artist, then we make a new artist and album with album information. 
'''

spotify_access_token = request_access_token(True)
artist_name = input("Enter arist's name: ")
artists.append(get_artist(artist_name))
print(artists[0].__str__())