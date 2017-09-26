import audiodome
import os


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
            remote_audio = "./data/playlist.txt".list
            audiodome.Utility.vlc_play_file(remote_audio)
    else:
        print("No download URL. Playing local file...")
        audiodome.Utility.vlc_play_file(local_audio)


if __name__ == "__main__":
    main()
