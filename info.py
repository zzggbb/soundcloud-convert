import soundcloud
import requests
import json

with open('client.ini') as f:
	client_info = json.load(f)

CLIENT = soundcloud.Client(client_id=client_info['id'])

def resolve(url):
	x = 'http://api.soundcloud.com/resolve.json?url={0}&client_id={1}'.format(url,client_info['id'])
	return {'json': requests.get(x).json(), 'response_url': x}

def info(url):

	try:
		if resolve(url)['json']['kind'] == 'track':
			track = resolve(url)['json']
			return [[{'id': str(track['id']),'title': track['title'],'artist': track['user']['username'],'stream_url': CLIENT.get(track['stream_url'], allow_redirects=False).location, 'raw_url': resolve(url)['response_url']}], 'Song' ]

		elif resolve(url)['json']['kind'] == 'playlist':
			playlist = resolve(url)['json']
			return [[({'id': str(track['id']),'title': track['title'],'artist': track['user']['username'],'stream_url': CLIENT.get(track['stream_url'], allow_redirects=False).location, 'raw_url': resolve(url)['response_url']}) for track in playlist['tracks']], 'Set']

		elif (resolve(url)['json'])['kind'] == 'user':
			favorites = requests.get('http://api.soundcloud.com/users/{0}/favorites.json?client_id={1}'.format( resolve(url)['json']['id'], client_info['id'] )).json()
			return [[({'id': str(track['id']),'title': track['title'],'artist': track['user']['username'],'stream_url': CLIENT.get(track['stream_url'], allow_redirects=False).location, 'raw_url': resolve(url)['response_url']}) for track in favorites], 'User']

	except KeyError:
		return False