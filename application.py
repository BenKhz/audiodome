import base64
import os
import time
import vlc
import httplib2
from oath2client.file import Storage
from apiclient import discovery
from apiclient import errors
# from apiclient import http


def main():
    # This is a string that represents the audio to be played.  If the
    # AUDIO_SRC environment variable is not set, it defaults to the song that
    # comes embedded in the docker image.

    audio_to_play = os.getenv('AUDIO_SRC', './01ANightOfDizzySpells.ogg')
    gdrive_credential_file = "/tmp/resin/gdrive.json"
    music_path = "/data/"

    if os.getenv('GOOGLE_DRIVE_CREDENTIALS') is not None:
        place_drive_credentials(gdrive_credential_file)
        storage = Storage(gdrive_credential_file)
        google_creds = storage.get()

    if os.getenv('GOOGLE_DRIVE_ID') is not None:
        download_from_google_drive(music_path, google_creds)

    player = vlc.MediaPlayer(audio_to_play)
    print("Playing %s" % audio_to_play)
    player.play()
    time.sleep(2)

    while player.is_playing():
        print("%s is still playing..." % audio_to_play)
        time.sleep(60)

    print("%s is done playing!" % audio_to_play)


def download_from_google_drive(music_path, google_creds):
    http = httplib2.Http()
    http = google_creds.authorize(http)
    drive_service = discovery.build('drive', 'v2', http=http)
    file_id = os.getenv('GOOGLE_FILE_ID')
    drop_file_location = os.path.join(music_path, "google_drop_file.zip")
    with open(drop_file_location, 'w') as drop_file:
        request = drive_service.files().get_media(fileId=file_id)
        media_request = http.MediaIoBaseDownload(drop_file, request)
        while True:
            try:
                download_progress, done = media_request.next_chunk()
            except errors.HttpError, error:
                print 'An error occurred: %s' % error
                return
            if download_progress:
                print 'Download Progress: %d%%' % int(download_progress.progress() * 100)  # NOQA
            if done:
                print 'Download Complete'
                return


def place_drive_credentials(gdrive_credential_file):
    b64_creds = os.getenv('GOOGLE_DRIVE_CREDENTIALS')
    with open(gdrive_credential_file, 'w') as cred_file:
        raw_creds = base64.b64decode(b64_creds)
        cred_file.write(raw_creds)
    return


if __name__ == "__main__":
    main()
