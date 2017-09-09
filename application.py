import os
import time
import vlc


# This is a string that represents the audio to be played.  If the
# AUDIO_SRC environment variable is not set, it defaults to the song that
# comes embedded in the docker image.

audio_to_play = os.getenv('AUDIO_SRC', './01ANightOfDizzySpells.ogg')

if os.getenv('GOOGLE_DRIVE-URL'):
    download_from_google_drive()
    

player = vlc.MediaPlayer(audio_to_play)
print("Playing %s" % audio_to_play)
player.play()
time.sleep(2)

while player.is_playing():
    print("%s is still playing..." % audio_to_play)
    time.sleep(60)

print("%s is done playing!" % audio_to_play)
