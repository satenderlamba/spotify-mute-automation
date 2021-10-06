from SwSpotify import spotify 
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from youtube_search import YoutubeSearch  #getting sreach urls


def main():
	try:
		TrackName = spotify.song()

	except: 
		print('Spotify paused.' + " " + str(datetime.datetime.now()))


	IsVolume = CheckVolume()            
	TrackName = 'Advertisement'
	try: 
		if IsVolume == True:
			if TrackName == 'Advertisement':
				MuteSpotify(True)
				PlayYoutube()


			

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




def PlayYoutube():
	print('calling youtube successful' + " " + str(datetime.datetime.now()))
	id = YoutubeSearch(str('redecorate 21 pilots'), max_results = 1).to_dict()[0]['id']
	driver = webdriver.Chrome()                                         # open browser

	wait = WebDriverWait(driver, 3)
	presence = EC.presence_of_element_located
	visible = EC.visibility_of_element_located
	
	# Navigate to url after appending video id to watch link
	driver.get('https://www.youtube.com/watch?v={}'.format(str(id)))

	# play the video
	wait.until(visible((By.ID, "video-title")))
	driver.find_element_by_id("video-title").click()
	


#def PauseYoutube():
#	driver.execute_script('document.getElementsByTagName("video")[0].pause()')


#def PlayYoutube():
#	driver.execute_script('document.getElementsByTagName("video")[0].play()')

# .


if __name__	== '__main__':    # keep looping over main
	try:
		while(True):
			main()
			time.sleep(0.1)
	except KeyboardInterrupt:
		pass 
