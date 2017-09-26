import audiodome
import os
import time


def main():

    local_audio = './01ANightOfDizzySpells.ogg'
    music_path = "/data/"
    if os.getenv('DOWNLOAD_URL') is not None:
        drop_file_location = '/data/drop_file.zip'
        url = os.getenv('DOWNLOAD_URL')
        audiodome.Downloader.url_to_file(url, drop_file_location)
        if os.path.exists(drop_file_location):
            audiodome.Utility.unzip_file_to_path(drop_file_location,
                                                 music_path)
            print("30 seconds before attempting to build playlist.")
            time.sleep(30)
            remote_audio_file = open("../data/playlist.txt")
            remote_audio = remote_audio_file.read_lines()
            audiodome.Utility.vlc_play_file(remote_audio)
    else:
        print("No download URL. Playing local file...")
        audiodome.Utility.vlc_play_file(local_audio)


if __name__ == "__main__":
    main()
