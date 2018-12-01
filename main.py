import os,sys, spotipy, json, webbrowser, time
import spotipy.util as util
from json.decoder import JSONDecodeError

def login(username, scope):
	#you can import your client id, secret_id here however I have chosen to export
	#them since I this is a public github read more here:https://spotipy.readthedocs.io/en/latest/
	try:
		token = util.prompt_for_user_token(username,scope)#, client_id, client_secret, redirect_uri)
	except:#(AttributeError, JSONDecodeError):
		os.remove(f".cache-{username}")
		token = util.prompt_for_user_token(username,scope)#,client_id, client_secret, redirect_uri)

	#creates spotipy object
	#sp = spotipy.Spotify(auth=token)
	if token:
		sp = spotipy.Spotify(auth=token)
		return sp
	else:
		print( "Can't get token for", username)
		return -1

def getSongID(sp, songName):
	#print(songName)
	song = sp.search(songName, limit =1, offset=0,type='track',market=None)
	for stuff in song['tracks']['items']:
		print(stuff['name'])
		return stuff['id']

def playSong(sp, songName):
	songID = getSongID(sp, songName)
	print(songID)
	#thankyou= 'spotify:track:2rPE9A1vEgShuZxxzR2tZH'
	songID= ['spotify:track:'+songID]
	sp.start_playback(device_id=None,context_uri=None,uris=songID,offset=None)

def getRecSongs(sp, userID):
	TopTracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
	print(TopTracks[0])
	RecSongList = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=TopSongs, limit=10, country=None)





def main(args):
	#make this a user input
	username ='1210610133'#Jack Dempseys User id public info
	scope = 'user-library-read user-read-private user-read-playback-state\
		user-modify-playback-state playlist-modify-public playlist-modify-private'
	sp = login(username, scope)

	playSong(sp,'instrumental thank you next')



if __name__ == '__main__':

    sys.exit(main(sys.argv))
