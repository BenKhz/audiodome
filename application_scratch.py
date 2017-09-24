import audiodome
import os
import time
import vlc


def main():

    audio_to_play = os.getenv('AUDIO_SRC', './01ANightOfDizzySpells.ogg')
    music_path = "/data/"

    if os.getenv('DOWNLOAD_URL') is not None:
        drop_file_location = '/data/drop_file.zip'
        url = os.getenv('DOWNLOAD_URL')
        audiodome.Downloader.url_to_file(url, drop_file_location)
        print("Download Attempting...")
        time.sleep(120)

    else:
        print("Download attempt failed!")
        time.sleep(120)

    audiodome.Utility.unzip_file_to_path(drop_file_location, music_path)
    print("Attempted to unzip!")
    time.sleep(120)

    '''player = vlc.MediaPlayer(audio_to_play)
    print("Playing %s" % audio_to_play)
    player.play()
    time.sleep(2)

    while player.is_playing():
        print("%s is still playing..." % audio_to_play)
        time.sleep(60)

    print("%s is done playing!" % audio_to_play)'''


if __name__ == "__main__":
    main()
