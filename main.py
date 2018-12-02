import os,sys,spotipy, json, webbrowser, time
import playGame
import spotipy.util as util
from json.decoder import JSONDecodeError

def login(username, scope):
	#you can import your client id, secret_id here however I have chosen to export
	#them since I this is a public github read more here:https://spotipy.readthedocs.io/en/latest/
	try:
		token = util.prompt_for_user_token(username,scope)#, client_id, client_secret, redirect_uri)
	except:#(AttributeError, JSONDecodeError):
		os.remove(f",cache-{username}")
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
	#print(songID)
	#thankyou= 'spotify:track:2rPE9A1vEgShuZxxzR2tZH'
	songID= ['spotify:track:'+songID]
	dev = sp.devices()
	sp.start_playback(device_id=dev[0],context_uri=None,uris=songID,offset=None)
	
def playPLSong(sp, IDpl):
	#print(songID)
	#thankyou= 'spotify:track:2rPE9A1vEgShuZxxzR2tZH'
	IDpl= 'spotify:playlist:'+IDpl
	print(IDpl)
	sp.start_playback(device_id=None,context_uri=IDpl)

def getRecSongs(sp, userID,isInstrument):
	TopTracks = sp.current_user_top_tracks(time_range='medium_term',limit=5,offset=0)
	tracks = []
	for item in TopTracks['items']:
		tracks.append(item['id'])
		
	
	#test = []
	#test.append('5nVK2UTeK0vJYePgxOjFPz')
	#test.append('0E0JKMR4uiCZhpI3brAoxI')
	if(~isInstrument):
		RecSongList = sp.recommendations(seed_artist=None , seed_genres=None , seed_tracks=tracks, limit=10, country=None,popularity=90)
	else:
		RecSongList = sp.recommendations(seed_artist=None , seed_genres=None , seed_tracks=tracks, limit=10, \
		country=None,popularity=90, instrumentalness= .9)
	
	ret=[]
	for item in RecSongList['tracks']:
		ret.append('spotify:track:'+item['id'])
	print(ret)
	return (ret)

def createPlaylist(sp,user):
	PLname = input("Enter playlist name you wish to create: ")
	print("creating Playlist "+PLname+ " now")

	Info = sp.user_playlist_create(user, PLname, public=False)
	PLid = Info['id']
	songList = getRecSongs(sp,user,isInstrument=False)
	sp.user_playlist_replace_tracks(user,PLid,songList)
	return PLid

def deletePlaylist(sp,PLid,username):
	sp.user_playlist_unfollow(username, PLid)


def main(args):
	#make this a user input
	#jackusername ='1210610133'#Jack Dempseys User id public info
	username = input("User ID: " )
	scope = 'user-library-read user-read-private user-read-playback-state\
		user-modify-playback-state playlist-modify-public playlist-modify-private\
		user-top-read, user-read-recently-played, streaming'
	sp = login(username, scope)

	#playSong(sp,'instrumental thank you next')
	#getRecSongs(sp, username)
	PLid = createPlaylist(sp, username)
	#playPLSong(sp, PLid)
	playGame.inputAns(sp,PLid)



	ans = input("Do you want to keep a playlist of Answers? (yes/no)")
	if(ans == "yes"):
		print("ok")
	else:
		deletePlaylist(sp, PLid,username)


if __name__ == '__main__':

    sys.exit(main(sys.argv))
