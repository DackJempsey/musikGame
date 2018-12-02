import os,sys, spotipy,time


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


def inputAns(sp, PLid):
	#songLen = getsongLength(songID)
	#points=10
	#sleepTime = songLen/10

	#start playing playlist
	#sp.start_playback(device_id = None, context_uri = None, uris = None, offset = None)
	
	totalScore = 0 # Score starts at 0


	#start play playlist here
	playPLSong(sp, PLid)
	for i in range(1, 6): #Play first five songs of playlist


		songName = sp.currently_playing(market = None) # getting song ID
		songName = songName['item']['name']
		print("SONG: ",songName)
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


		sp.next_track(device_id = None) #after correctly guessing or 30 seconds move to next song

		#sp.pause_playback(device_id=None)
		print('you have '+ str(totalScore) +' points')
