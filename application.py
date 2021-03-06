import audiodome
import os
import sys
import time
import vlc
import httplib2
# from oauth2client.file import Storage
from apiclient import discovery
from apiclient import errors
# from apiclient import http


def main():
    # This is a string that represents the audio to be played.  If the
    # AUDIO_SRC environment variable is not set, it defaults to the song that
    # comes embedded in the docker image.
    audio_to_play = os.getenv('AUDIO_SRC', './01ANightOfDizzySpells.ogg')
    # This is the file we will write the Google API credentials into.
#    gdrive_credential_file = "/tmp/resin/gdrive.json"
    # This is where the music files get written to.
    music_path = "/data/"
# b64 encoding section collapsed line 23-50
    '''if os.getenv('GOOGLE_DRIVE_CREDENTIALS') is not None:
        b64_creds = os.getenv('GOOGLE_DRIVE_CREDENTIALS')
        audiodome.Utility.b64_to_file(b64_creds, gdrive_credential_file)
# Declared google_creds empty so storage put and get knows its real.
        google_creds = "empty"
        storage = Storage(gdrive_credential_file)
        storage.put(google_creds)
        google_creds = storage.get()

    if os.getenv('GOOGLE_FILE_ID') is not None:
        download_from_google_drive(music_path, google_creds)
    '''

    if os.getenv('DOWNLOAD_URL') is not None:
        drop_file_location = '/data/drop_file.zip'
        url = os.getenv('DOWNLOAD_URL')
        audiodome.Downloader.url_to_file(url, drop_file_location)
        if os.path.exists(drop_file_location):
            audiodome.Utility.unzip_file_to_path(drop_file_location,
                                                 music_path)
        else:
            os.wait(30)
            print("Waiting for download to finish")

    player = vlc.MediaPlayer(audio_to_play)
    print("Playing %s" % audio_to_play)
    player.play()
    time.sleep(2)

    while player.is_playing():
        print("%s is still playing..." % audio_to_play)
        time.sleep(60)

    print("%s is done playing!" % audio_to_play)


def download_from_google_drive(music_path, google_creds):
    '''Download and expand file from Google Drive.

    Args:
        music_path(str): This is the base path for working with the music
            download.
        google_creds(oauth2client.file.Storage): This is an object containing
            The credentials to be used for Google Drive.
    '''
    http = httplib2.Http()
    http = google_creds.authorize(http)
    # The prior line isn't great form, as it re-declares the smae variable as
    # something of a different type.  We'll leave it for now, and refactor
    # later.
    drive_service = discovery.build('drive', 'v2', http=http)
    file_id = os.getenv('GOOGLE_FILE_ID')
    drop_file_location = os.path.join(music_path, "google_drop_file.zip")
    with open(drop_file_location, 'w') as drop_file:
        drive_files = drive_service.files()
        request = drive_files.get_media(fileId=file_id)
        media_request = http.MediaIoBaseDownload(drop_file, request)
        while True:
            try:
                download_progress, done = media_request.next_chunk()
            except errors.HttpError, error:
                print('An error occurred: %s' % error)
                sys.exit(2)  # If this happens, we exit in a ball of fire.
            if download_progress:
                prg = int(download_progress.progress() * 100)
                print('Download Progress: %d%%' % prg)
            if done:
                print('Download Complete')
                break
        audiodome.Utility.unzip_file_to_path(drop_file_location, "/data")


if __name__ == "__main__":
    main()
