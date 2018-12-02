import os,sys, spotipy,time
from difflib import SequenceMatcher

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def getsongLength(sp, songID):#gets length of the song
	info = sp.audio_features(songID)
	length = info[0]['duration_ms']
	length = length *100 #change to seconds
	return length #in seconds
	
def playPLSong(sp, IDpl):
	#print(songID)
	#thankyou= 'spotify:track:2rPE9A1vEgShuZxxzR2tZH'
	IDpl= 'spotify:playlist:'+IDpl
	print(IDpl)
	sp.start_playback(device_id=None,context_uri=IDpl)


def inputSong(sp, PLid):
	#songLen = getsongLength(songID)
	#points=10
	#sleepTime = songLen/10

	#start playing playlist
	#sp.start_playback(device_id = None, context_uri = None, uris = None, offset = None)
	
	totalScore = 0 # Score starts at 0


	#start play playlist here
	playPLSong(sp, PLid)
	for i in range(1, 6): #Play first five songs of playlist

		time.sleep(1)
		songName = sp.currently_playing(market = None) # getting song ID
		songName = songName['item']['name']
		#print("SONG: ", songName)
		ans = 'not a song'
		currentSongScore = 120

		start_time = time.time() # Only get 30 seconds to guess song
		while(ans != songName and ((time.time() - start_time) < 30) and (currentSongScore>0)):
			ans = input("Guess what song is playing: ")

			print(str(currentSongScore)+'possible points')
			
			currentSongScore-=20 #Every wrong guess decreases score by 20

			if ans == songName:
				print('Nice job! You guessed the song right.')
				totalScore += currentSongScore; #if guessed correctly, add score to total
				break
			else:
				print("That guess was incorrect.")

		if(currentSongScore == 0):
			print("You have run out of guesses for that song... correct answer was: ", songName)

		sp.next_track(device_id = None) #after correctly guessing or 30 seconds move to next song

		#sp.pause_playback(device_id=None)
		print('you have '+ str(totalScore) +' points')

	print('You finished with a final score of ', totalScore,' out of 500')

def inputArtist(sp, PLid):
	totalScore = 0 # Score starts at 0


	#start play playlist here
	playPLSong(sp, PLid)
	for i in range(1, 6): #Play first five songs of playlist

		time.sleep(1)
		songName = sp.currently_playing(market = None) # getting song ID
		artistName = songName['item']['artists'][0]['name']
		print(artistName)
		#for item in artistName:
		#	print(item,'\n')
		
		#print("SONG: ", songName)
		ans = 'not a song'
		currentSongScore = 120

		start_time = time.time() # Only get 30 seconds to guess song
		while(ans != artistName and ((time.time() - start_time) < 30) and (currentSongScore>0)):
			ans = input("Guess the artist of this song: ")
	
			print(str(currentSongScore)+'possible points')
			
			currentSongScore-=20 #Every wrong guess decreases score by 20
			simScore = similar(ans.lower(), artistName.lower())
			if simScore>=.8:
				print('Nice job! You guessed the artist right.')
				totalScore += currentSongScore; #if guessed correctly, add score to total
				break
			else:
				if(ans.lower() = 'quit'):
					return -1
				input("That guess was incorrect")

		if(currentSongScore == 0):
			print("You have run out of guesses for that artist... correct answer was: ", artistName)
		sp.next_track(device_id = None) #after correctly guessing or 30 seconds move to next song

		#sp.pause_playback(device_id=None)
		print('you have '+ str(totalScore) +' points')
	
	print('You finished with a final score of ', totalScore,' out of 500')
