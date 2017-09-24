import audiodome
import os
import time


def main():

    if os.getenv('DOWNLOAD_URL') is not None:
        drop_file_location = '/data/drop_file.zip'
        url = os.getenv('DOWNLOAD_URL')
        audiodome.Downloader.url_to_file(url, drop_file_location)
        print("Download Attempting...")
        time.sleep(120)

    else:
        print("Download attempt failed!")
        time.sleep(120)

    audiodome.Utility.unzip_file_to_path(drop_file_location, "/data/music/")
    print("Attempted to unzip! Bash to check!")
    time.sleep(120)


if __name__ == "__main__":
    main()
