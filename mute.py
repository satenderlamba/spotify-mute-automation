from SwSpotify import spotify 
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time
import datetime

def main():

	try:
		TrackName = spotify.song()

	except: 
		print('Spotify paused.' + " " + str(datetime.datetime.now()))


	IsVolume = CheckVolume()            

	try: 
		if IsVolume == True:
			if TrackName == 'Advertisement':
				MuteSpotify(True)

			

		else:
			if not TrackName == 'Advertisement':
				MuteSpotify(False)

	except:
		pass


#main ends here



def MuteSpotify(mute):                                                        #function to mute/unmute
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session._ctl.QueryInterface(ISimpleAudioVolume)
		if session.Process and session.Process.name() == 'Spotify.exe':
			if mute:
				volume.SetMasterVolume(0, None)  # mute
				print('Ad detected and muted' + " " + str(datetime.datetime.now())) 

			else:
				volume.SetMasterVolume(1, None)  # unmute
				print('Ad over, resuming playback' + " " + str(datetime.datetime.now()))




def CheckVolume():                                        #function to check volume
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session._ctl.QueryInterface(ISimpleAudioVolume)
		if session.Process and session.Process.name() == "Spotify.exe":
			return bool(volume.GetMasterVolume())




if __name__	== '__main__':    # keep looping over main
	try:
		while(True):
			main()
			time.sleep(0.1)
	except KeyboardInterrupt:
		pass