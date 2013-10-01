import soundcloud
import requests
import json

with open('client.ini') as f:
	client_info = json.load(f)

CLIENT_ID = client_info['client_id']
CLIENT_SECRET = client_info['client_secret']
CLIENT = soundcloud.Client(client_id=CLIENT_ID)

def info(input_url):
	try:
		check = requests.get('http://api.soundcloud.com/resolve.json?url=%s&client_id=%s' % (input_url, CLIENT_ID)).json()

		if check['kind'] == 'track':
			track = CLIENT.get('/tracks/' + str(check['id']))
			return [{'id':str(track.id),'title': track.title,'artist': track.user['username'],'url': CLIENT.get(track.stream_url, allow_redirects=False).location}]

		elif check['kind'] == 'playlist':
			playlist = CLIENT.get('/playlists/' + str(check['id']))
			return [({'id': str(track['id']),'title': track['title'],'artist': track['user']['username'],'url': CLIENT.get(track['stream_url'], allow_redirects=False).location}) for track in playlist.tracks]

		return False

	except KeyError:
		return False