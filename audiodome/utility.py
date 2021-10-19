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

        player = vlc.MediaPlayer()
        media = vlc.media_new(audio_to_play)
        player.set(media)
        print("Playing %s" % audio_to_play)
        player.play()


        def check_if_playing():
            if player.is_playing() == 1:
                print("%s is still playing..." % song)
                time.sleep(3)
                check_if_playing()
            else:
                print("%s is done playing!" % song)
                pass

        for song in audio_to_play:
            player = vlc.MediaPlayer(os.path.join("../data/music/", song))
            player.play()
            print("Playing %s" % song)
            time.sleep(1)
            check_if_playing()

        print("All Audio in List is done playing!")
