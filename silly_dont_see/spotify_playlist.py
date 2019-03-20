# A dictionary template for each song
# {
#   'title' : 'song-name',
#   'artist' : ['list-of-artist(s)'],
#   'album' : 'album-name',
#   'data-added' : 'date',
#   'track-time' : 'time'
# }

# A dictionary template for playlist :
# {
#   'name' : 'play-list-name',
#   'creator' : 'crator-name',
#   'list' : list-of-songs,
#   'number_of_songs' : number_of_songs,
#   'total-time' : total_time_of_all_songs_together
# }


def get_total_time(songs):
    total_min = 0
    total_sec = 0
    for song in songs:
        m, s = song['track-time'].split('.')
        print(f'm = {m}, s = {s}')

        total_sec += int(s)
        total_min += int(m)

    total_min = (total_min * 60 + total_sec) // 60
    total_sec = total_sec % 60
    return f'{total_min}.{total_sec}'


# Song 1
song_1 = {
    'title': 'Assasin\'s Creed Odyssey',
    'artist': 'Shawn',
    'album': 'The Flight',
    'date-added': '16-03-2019',
    'track-time': '3.40'
}

# Song 2
song_2 = {
    'title': 'Legend Of The Eagle Bearer',
    'artist': 'Mike',
    'album': 'The Flight',
    'date-added': '16-03-2019',
    'track-time': '3.53'
}

# Song 3
song_3 = {
    'title': 'Years Of Training',
    'artist': 'Mike',
    'album': 'The Flight',
    'date-added': '16-03-2019',
    'track-time': '3.40'
}


playlist = {
    'name': 'Assasin\'s Creed',
    'creator': 'm_zaink'
}

playlist['song-list'] = [song_1, song_2, song_3]

playlist['number_of_songs'] = len(playlist['song-list'])

playlist['total-time'] = get_total_time(playlist['song-list'])


print(playlist)
