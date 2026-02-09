from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('Another Day Of Sun', 3.48), ('Black Swan', 3.18), ('Aaya Mausam Dosti Ka', 6.46), ('A Lovely Night', 4.00), ('Antakshari', 9.08), ('Ashes On Fire', 4.35)]

def longer_than_five_minutes(song):
    return song[1] > 5.00
long_songs = filter(longer_than_five_minutes, playlist)

def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100
    total_seconds = (minutes * 60) + seconds
    return total_seconds
duration = map(minutes_to_seconds, playlist)

# print(f'Playlist: {playlist}')
# print(f'Songs longer than 5 minutes {list(long_songs)}')
print(f'Total duration in seconds: {list(duration)}')