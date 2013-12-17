import soundcloud
import requests
import json

with open('client.ini') as f:
    client_info = json.load(f)

CLIENT_ID = client_info['id']
CLIENT = soundcloud.Client(client_id=CLIENT_ID)
MAIN_API = 'http://api.soundcloud.com'
USER_API = '/users/{0}/favorites.json?client_id={1}'
RESOLVE_API = '/resolve.json?url={0}&client_id={1}'

class Track:
    def __init__(self,id,title,artist,stream):
        self.id = id
        self.title = title
        self.artist = artist
        self.stream = stream

def resolve(url):
    x = MAIN_API + RESOLVE_API.format(url,CLIENT_ID)
    return {'json': requests.get(x).json(), 'response_url': x}

def info(url):
    try:
        song_json = resolve(url)['json']
        response_type = song_json['kind']
    except KeyError: # invalid URL
        return False

    # no better way, can't use list index method because it will raise an error
    if response_type == 'user':
        tracks = requests.get(MAIN_API + USER_API.format(song_json['id'], CLIENT_ID)).json()
    if response_type == 'playlist':
        tracks = song_json['tracks']
    if response_type == 'track':
        tracks = [song_json]

    response = []
    for track in tracks:
        # append song data fields
        id = str(track['id'])
        title = track['title']
        artist = track['user']['username']
        try:
            stream = [True, CLIENT.get(track['stream'], allow_redirects=False).location]
        except:
            stream = [False, "Stream URL not available"]
            pass

        response.append(Track(id,title,artist,stream))

    return [response, response_type]

