import os,sys, spotipy,time


def getsongLength(sp, songID):#gets length of the song
	info = sp.audio_features(songID)
	length = info[0]['duration_ms']
	length = length *100 #change to seconds
	return length #in seconds

def inputAns(sp, songID):
	ans = 'not a song'
	songLen = getsongLength(songID)
	points=10
	sleepTime = songLen/10
	#play song here
	while(ans != songName or points==0):
		ans = input("Guess what song is playing: ")
		print(points+'possible points')
		time.sleep(sleepTime)
		points-=1


	sp.pause_playback(device_id=None)
	print('you have '+points+' points')
