import audiodome
import os


def main():

    audio_to_play = os.getenv('AUDIO_SRC', './01ANightOfDizzySpells.ogg')
    music_path = "/data/"
    if os.getenv('DOWNLOAD_URL') is not None:
        drop_file_location = '/data/drop_file.zip'
        url = os.getenv('DOWNLOAD_URL')
        audiodome.Downloader.url_to_file(url, drop_file_location)
        if os.path.exists(drop_file_location):
            audiodome.Utility.unzip_file_to_path(drop_file_location,
                                                 music_path)
        else:
            os.wait(30)
            print("Waiting for download to finish.")
    else:
        print("Environment Var is NONE. Playing local file...")

    audiodome.Utility.vlc_play_file(audio_to_play)


if __name__ == "__main__":
    main()