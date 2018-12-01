import os,sys, spotipy, json, webbrowser, time, userProf, extras
import songStats
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
	print(songName)
	song = sp.search(songName, limit =1, offset=0,type='track',market=None)
	for stuff in song['tracks']['items']:
		return stuff['id']
    
 def playSong(sp, songID):
 




	#make this a user input
	username ='1210610133'#Jack Dempseys User id public info
	scope = 'user-library-read user-read-private user-read-playback-state\
		user-modify-playback-state playlist-modify-public playlist-modify-private'
	sp = login(username, scope)
  
  
  
if __name__ == '__main__':

    sys.exit(main(sys.argv))
