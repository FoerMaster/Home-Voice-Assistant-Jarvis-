import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read,user-read-playback-state, user-modify-playback-state"

#YOUR SPOTIFY APP

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = '',
                                                          client_secret = '',
                                                          redirect_uri = 'http://google.com/',
                                                          scope = scope))
device = "0";

def login():
    sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = '',
                                                          client_secret = '',
                                                          redirect_uri = 'http://google.com/',
                                                          scope = scope))

    device = sp.devices()['devices'][0]['id']

def pause():
    try:
        device = sp.devices()['devices'][0]['id']
        sp.pause_playback(device)
    except:
        pass

def play(song=""):
    device = sp.devices()['devices'][0]['id']
    if len(song) <= 0:
        results = sp.search(q='Highway to Hell', type='track')
        items = results['tracks']['items']
        if len(items) > 0:
            track = items[0]
            sp.start_playback(device,None,[track['uri']])
    else:
        results = sp.search(q=song, type='track')
        items = results['tracks']['items']
        if len(items) > 0:
            track = items[0]
            sp.start_playback(device, None, [track['uri']])
