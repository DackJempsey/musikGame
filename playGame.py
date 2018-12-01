import os,sys, spotipy,time


def getsongLength(sp, songID):#gets length of the song
	info = sp.audio_features(songID)
	length = info[0]['duration_ms']
	length = length *100 #change to seconds
	return length #in seconds

def inputAns(sp, PLid):
	#songLen = getsongLength(songID)
	#points=10
	#sleepTime = songLen/10

	#start playing playlist
	sp.start_playback(device_id = None, context_uri = None, uris = None, offset = None)
	
	totalScore = 0 # Score starts at 0



	#start play playlist here
	for i in range(1, 6): #Play first five songs of playlist

		ans = 'not a song'

		songName = sp.currently_Playing(market = None) # getting song ID

		currentSongScore = 120

		start_time = time.time() # Only get 30 seconds to guess song
		while(ans != songName and ((time.time() - start_time) < 30) and (currentSongScore>0)):
			ans = input("Guess what song is playing: ")
			print(points+'possible points')
			time.sleep(sleepTime)
			points-=20 #Every wrong guess decreases score by 20

		if ans == songName:
			print('Nice job! You guessed the song right.')
			totalScore += currentSongScore; #if guessed correctly, add score to total


		sp.next_track(device_id = none) #after correctly guessing or 30 seconds move to next song

		#sp.pause_playback(device_id=None)
		print('you have '+ totalScore +' points')
