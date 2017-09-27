import base64
import zipfile
import vlc
import time
import os


class Utility(object):
    @classmethod
    def b64_to_file(cls, b64_data, file_path):
        with open(file_path, 'w') as out_file:
            out_file.write(base64.b64decode(b64_data))
        return

    @classmethod
    def unzip_file_to_path(cls, zip_infile, out_dir):
        with zipfile.ZipFile(zip_infile, 'r') as zip_ref:
            zip_ref.extractall(out_dir)
            print ("Zip extracted!")
        return

    @classmethod
    def vlc_play_file(cls, audio_to_play):
        for song in audio_to_play:
            player = vlc.MediaPlayer(os.path.join("../data/music/", song))
            print("Playing %s" % song)
            player.play()
            time.sleep(2)

        while player.is_playing():
            print("%s is still playing..." % song)
            time.sleep(60)

        print("%s is done playing!" % song)
