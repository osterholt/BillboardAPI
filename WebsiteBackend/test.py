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
def get_artist_id():
    artist_name = input('Enter an Artist\'s name or Spotify link: ')
    # Spotify Link Format: https://open.spotify.com/artist/ARTIST_ID
    if (artist_name.__contains__('https://open.spotify.com/artist/') and artist_name.__len__() == 58):
        print('You did it kanye')
        return artist_name[32:]
    else:
        artist_search_query = "curl \"https://api.spotify.com/v1/search?query=" + urllib.parse.quote_plus(artist_name) + "&type=artist&locale=en-US%2Cen%3Bq%3D0.5&offset=0&limit=20\" -H \"Authorization: Bearer  " + access_token + "\" > artists.json 2> /dev/null"
        os.system(artist_search_query) # overrides artists.json to add package.
    
    with open('artists.json', 'r') as f:
        data = json.load(f)
        return data['artists']['items'][0]['id']

# ----------Creates json File for the Artist's Albums----------
def get_albums():
    # FORMAT: {[album_name], [album_ID], [album_cover_img_url], [release_date], [peak_position]}
    album_file_name = "albums.json"
    billboard_200_file_name = "bb200_FE2.csv"
    delim = '`'
    
    artist_search_query = "curl \"https://api.spotify.com/v1/artists/" + artist_id + "/albums?offset=0&limit=50&include_groups=album&locale=en-US,en;q=0.5\" -H \"Authorization: Bearer  " + access_token + "\" > " + album_file_name + " 2> /dev/null"
    os.system(artist_search_query) # overrides artists.json to add package.
    
    with open(album_file_name) as f:
        data = json.load(f)
        for album in data["items"]:
            append = True
            for item in albums:
                if(album['name'] == item[0]):
                    append = False
            if(append):
                albums.append([album['name'], album['id'], album['images'][1]['url'], album['release_date'], 201])
                
    with open(billboard_200_file_name, 'r') as bb:
        # BB200 FORMAT: {[Chart #], [Album Title], [Artist], [Last Week], [Peak Position], [Weeks On Chart], [Source Chart Date]}
        csvreader = csv.reader(bb, delimiter=delim)
        for lines in bb:
            line = lines.split(delim)
            # artist name is index 2
            if(line[2].lower() == artist_name.lower()):
                #this chart is by the artist so now we need to find the index in albums
                # line[1] = album title
                for album in albums:
                    if(album[0].lower() == line[1].lower()):
                        # The album title for this specific album fits the charted instance. 
                        if(int(line[0]) < int(album[4])):
                            album[4] = line[0]
                            
    return albums 
                    
def get_songs():
    # FORMAT: {[album_name], [album_ID], [album_cover_img_url], [release_date], [peak_position], {[songs], [peak_positon]} }
    # FORMAT: { 0: [album_name], 1: [album_ID], 2: [album_cover_img_url], 3: [release_date], 4: [peak_position], 5: {[songs], [peak_positon]} }
    billboard_100_file_name = "bb100_FE2.csv"
    delim = '`'
    for album in albums:
        song_file_name = album[1] + "_songs.json"
        album.append([])
    
        album_search_query = "curl \"https://api.spotify.com/v1/albums/" + album[1] + "/tracks\" -H \"Authorization: Bearer  " + access_token + "\" > " + song_file_name + " 2> /dev/null"
        os.system(album_search_query) # overrides artists.json to add package.
        with open(song_file_name) as f:
            data = json.load(f)
            for item in data['items']:
                album[5].append([item['name'], 201]) 
    
    with open(billboard_100_file_name, 'r') as bb:
        # FORMAT: { [Chart #], [Song Title], [Artist], [Last Week], [Peak Position], [Weeks On Chart], [Source Chart Date] }
        for lines in bb:
            line = lines.split(delim)
            if(line[2].lower() == artist_name.lower()) :
                for album in albums:
                    for song in album[5]:
                        if(line[1].lower() == song[0].lower() and int(line[0]) < int(song[1])):
                            song[1] = line[0]                        
    return albums
            
def print_albums():
    # FORMAT: { 0: [album_name], 1: [album_ID], 2: [album_cover_img_url], 3: [release_date], 4: [peak_position], 5: {[songs], [peak_positon]} }
    for album in albums:
        if(album[4] == 201):
            album[4] = 'N/A'
        print("Peak: " + str(album[4]) + " | " + album[0] + "  |  Released: " + album[3])
        for song in album[5]:
            if(song[1] == 201):
                song[1] == 'N/A'
            print("    Peak #: " + str(song[1]) +"  |  Song: " + song[0])
        

#----------------------------------------------------------------------------------------------------------------------------

os.system("python remove.py")

print('**********************')
print('*                    *')
print('*     Welcome to     *')
print('*        WUSC        *')
print('*                    *')
print('**********************\n')
print('Written by Cam Osterholt c.2023') 
print('Please remembr to check your spelling!') 

# artist_name = input("Enter artist's name from file: ")
artist_name = ''
access_token = request_access_token()
artist_id = get_artist_id()

albums = []
albums = get_albums()
# print(albums)
albums = get_songs()
print_albums()

os.system("python remove.py")