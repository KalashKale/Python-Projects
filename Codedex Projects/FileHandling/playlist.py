liked_songs = {
    'Black Swan': 'BTS',
    'Sparkle': 'RADWIMPS',
    'Believer':'Imagine Dragons',
    'Celeb':'PSY',
    'T-KT': 'Hiroyuki Sawano',
    'ME': 'Taylor Swift',
    'Count On Me': 'Bruno Mars'
}

def write_liked_songs_to_file(liked_songs, filename):
    with open(filename, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in liked_songs.items():
            file.write(f'{song} by {artist}\n')

write_liked_songs_to_file(liked_songs, 'playlist.txt')

