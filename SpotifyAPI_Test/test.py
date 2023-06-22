import os, sys, json

client_id = "3e14df7c9d0647a785aea8c5559f0927"
client_secret = "afdaf4f47c294893a2b6a96989a47e72"

access_token_request = "curl -X POST \"https://accounts.spotify.com/api/token\" -H \"Content-Type: application/x-www-form-urlencoded\" -d \"grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret+ "\" > access.json 2> /dev/null" #TODO: Find a way to not have stderr go to a file.
access_token = ""
# os.system(access_token_request)

with open('albums.json', 'r') as f:
    data = json.load(f)
    albums = []
    for item in data['items']:
        if (albums.__len__ == 0):
            albums.append(item)
        else:
            append = True
            for album in albums:
                if(item['name'] == album):
                    append = False
            if(append):
                albums.append(item['name'])
    
    
    
    
    
    
    
    
    
    
        
print(albums)