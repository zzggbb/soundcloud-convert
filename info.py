import soundcloud
import requests
import json

with open('client.ini') as f:
	client_info = json.load(f)

CLIENT_ID = client_info['client_id']
CLIENT_SECRET = client_info['client_secret']

client = soundcloud.Client(client_id=CLIENT_ID)

url = raw_input("Give a track's url: ")
r = requests.get('http://api.soundcloud.com/resolve.json?url=%s&client_id=%s' % (url, CLIENT_ID))

# general information
id = r.json()['id']
title = r.json()['title']
artist = r.json()['user']['username']

# time information
hours = (r.json()['duration']) / 3600000
minutes = (r.json()['duration']) / 60000
seconds = int((((r.json()['duration']) / 60000.0) % 1) * 60)
length = "%s : %s : %s" % (hours, minutes, seconds)

# technical information
stream_url = client.get(client.get('/tracks/' + str(id)).stream_url, allow_redirects=False).location
json = r.json()