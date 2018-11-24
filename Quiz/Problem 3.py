def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    
    playlist = []
    remainSpace = max_size
    # start with the first song in the given song list. If the first song doesn't fit on disk, return an empty list. 
    if songs[0][2] <= max_size:
        playlist.append(songs[0][0])
        remainSpace -=songs[0][2]
        # sort the songslist
        songsList = sorted(songs, key = lambda x :x[2])
        # remove the first song in songs
        songsList.remove(songs[0])
    
        for song in songsList:
            if song[2] <=remainSpace:
                playlist.append(song[0])
                remainSpace -=song[2]
            else:
                break
    # if the first song in songs dose not fit the disk, return empty list
    else:
        playlist = []        
        
    return playlist


