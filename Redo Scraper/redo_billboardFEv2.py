import csv, sys

# TODO: 
# - Invalid input when put string instead of 0-2 choice.
# - Give reccomended songs for artists.
# - Find songs that have commas.
    
def sort_by_artist():
    artist_name = input("Enter Artist's Name (\'menu\' to return to menu): ")
    print('--------------------------------------------------------------------')
    if(str.lower(artist_name) == 'menu'):
        return
    
    # Billboard Top 200 Loop:
    album_arr = []
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
    
    # Billboard Hot 100 Loop:
    song_arr = []
    num_top50 = 0
    for rows in bb100:
    #if row is by an artist, only add if the sony is not yet in the array or if in the array and position is lower than previous position
        if(str.lower(rows[2]) == str.lower(artist_name)):
            in_song_arr = False
            for song_row in song_arr:
                if(str.lower(rows[1]) == str.lower(song_row[1]) and int(rows[0]) < int(album_row[0])):
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
    
    print('Searching for', artist_name + '...\n')
    
    if(len(album_arr) == 0 and len(song_arr) == 0):
        print('No Top 200 or Hot 100 results found for', artist_name, '(Make sure to check spelling)')
        print('Can', artist_name, 'be played on WUSC: YES\n')
    else:
        if(num_top40 > 1 or num_top50 > 1):
            print('Can', artist_name, 'be played on WUSC: NO\n')
        else:
            print('Can', artist_name, 'be played on WUSC: YES\n')
        print(' Number of Top 40 Albums:', num_top40, '\n Number of Top 50 Songs:', num_top50)
        if(len(album_arr) > 0 or len(song_arr) > 0):
            # TODO: make list not include albums/songs if there aren't any.
            i = input('\nWould you like to see the list (yes or no): ')
            print('--------------------------------------------------------------------')
            if (str.lower(i) == 'yes'):
                if (len(album_arr) > 0):
                    print('\nAlbums:')
                    for albums in album_arr:
                        print('   Album Name:', albums[1], '\n     Peak Position:', albums[0])
                if (len(album_arr) > 0 and len(song_arr) > 0):
                    print('\n--------------------')
                if (len(song_arr) > 0):
                    print('\nSongs:')
                    for songs in song_arr:
                        print('   Song Name:', songs[1], '\n     Peak Position:', songs[0])
            elif(str.lower(i) == 'no'):
                print('Exiting to home menu...')
            else:
                print('Invalid input, returning to home menu...')
    
    return

# ---------------------------------------------------------------------------------------------------------------- #
    
def sort_by_album():
    album_name = input("Enter Albums's Name (\'menu\' to return to menu): ")
    print('--------------------------------------------------------------------')
    if(str.lower(album_name) == 'menu'):
        return
    # format: ['Peak Position', 'Album Title', 'Artist']
    album_arr = []
    
    for rows in bb200:
        if(str.lower(rows[1]) == str.lower(album_name)):
            in_album_arr = False
            for row in album_arr:
                if(str.lower(rows[2]) == str.lower(row[2]) and int(rows[0]) < int(row[0])):
                    in_album_arr = True
                    album_arr[album_arr.index(row)] = [rows[0], rows[1], rows[2]]
                elif(str.lower(rows[2]) == str.lower(row[2])):
                    in_album_arr = True
            if(not in_album_arr):
                album_arr.append([rows[0], rows[1], rows[2]])
                
    if(len(album_arr) == 0):
        print('\nNo results found for: ', album_name)
    else:
        if(len(album_arr) == 1):
            print('1 Result found:\n')
        else:
            print(len(album_arr), 'Results found:\n')
        
        for items in album_arr:
            print(items[1], 'by', items[2])
            print('  Peak Position:', items[0])
        
    return

# ---------------------------------------------------------------------------------------------------------------- #

def sort_by_song():
    #TODO: find a way to remove features from song titles
    # Thinking: Would it be easier to ask for artist name as well? that seems too hard. I dont know.
    song_name = input("Enter Song's Name (\'menu\' to return to menu): ")
    print('--------------------------------------------------------------------')
    if(str.lower(song_name) == 'menu'):
        return
    # format: ['Peak Position', 'Album Title', 'Artist']
    song_arr = []
    
    for rows in bb100:
        if(str.lower(rows[1]) == str.lower(song_name)):
            in_song_arr = False
            for row in song_arr:
                if(str.lower(rows[2]) == str.lower(row[2]) and int(rows[0]) < int(row[0])):
                    in_song_arr = True
                    song_arr[song_arr.index(row)] = [rows[0], rows[1], rows[2]]
                elif(str.lower(rows[2]) == str.lower(row[2])):
                    in_song_arr = True
            if(not in_song_arr):
                song_arr.append([rows[0], rows[1], rows[2]])
                
    if(len(song_arr) == 0):
        print('\nNo results found for: ', song_name)
    else:
        if(len(song_arr) == 1):
            print('1 Result found:\n')
        else:
            print(len(song_arr), 'Results found:\n')
        
        for items in song_arr:
            print(items[1], 'by', items[2])
            print('  Peak Position:', items[0])
        
    return

# ---------------------------------------------------------------------------------------------------------------- #

filename200 = 'redo_bb200.csv'
bb200 = []
filename100 = 'redo_bb100.csv'
bb100 = []

with open(filename200) as file_input:
    csvreader = csv.reader(file_input, delimiter='*')
    for lines in file_input:
        line = lines.split('*')
        line[6] = line[6].strip()
        # print('line[6] =', line[6])
        bb200.append(line)
with open(filename100) as file_input:
    csvreader = csv.reader(file_input, delimiter='*')
    for lines in file_input:
        line = lines.split('*')
        line[6] = line[6].strip()
        # print('line[6] =', line[6])
        bb100.append(line)

print('**********************')
print('*                    *')
print('*     Welcome to     *')
print('*        WUSC        *')
print('*                    *')
print('**********************\n')
print('Written by Cam Osterholt c.2023') 
print('Please remembr to check your spelling!') 

a = 'bananas!'
while (a != '0'): 
    print('\nEnter from the following options\n1. Search by Artist\n2. Search by Album Name\n3. Search by Song Name\n4. Display Billboard by Week (UNDER CONSTRUCTION)\n0. Quit')
    a = input('Enter: ')
        
    if(a == '1'):
        sort_by_artist()
    elif(a == '2'):
        sort_by_album()
    elif(a == '3'):
        sort_by_song()
    elif(a == '0'):
        print('Now Exiting...')
        SystemExit
    else:
        print('Error: invalid choice')