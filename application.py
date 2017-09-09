import os
import time
import vlc

def main():
    # This is a string that represents the audio to be played.  If the
    # AUDIO_SRC environment variable is not set, it defaults to the song that
    # comes embedded in the docker image.

    audio_to_play = os.getenv('AUDIO_SRC', './01ANightOfDizzySpells.ogg')
    gdrive_credential_file = "/tmp/resin/gdrive.json"

    if os.getenv('GOOGLE_DRIVE_CREDENTIALS'):
        place_drive_credentials(gdrive_credential_file)

    if os.getenv('GOOGLE_DRIVE_URL'):
        download_from_google_drive()

    player = vlc.MediaPlayer(audio_to_play)
    print("Playing %s" % audio_to_play)
    player.play()
    time.sleep(2)

    while player.is_playing():
        print("%s is still playing..." % audio_to_play)
        time.sleep(60)

    print("%s is done playing!" % audio_to_play)

def download_from_google_drive():
    return
def place_drive_credentials(gdrive_credential_file):
    return


if __name__ == "__main__":
    main()
