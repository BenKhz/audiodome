# AudioDome


## Requirements

* Accounts:
  * Resin.io
* Hardware:
  * Raspberry Pi 2 or 3
  * Speakers for the Resin-managed Pis

## Usage

1. Create a Resin application for AudioDome
1. Clone down this repository and add the Resin.io app as a git remote.
1. Configure your environment variables according to your use case (see table
  below and the Implementation Notes section).
1. Push this repository to your Resin.io app
1. Image one or more Raspberry Pis for your Resin.io app

| Environment Variable     | Purpose                                          |
|--------------------------|--------------------------------------------------|
| AUDIO_SRC                | Path or URL for audio file to be played          |
| GOOGLE_DRIVE_CREDENTIALS | Base64-encoded Google Drive OAuth credentials    |
| GOOGLE_FILE_ID           | ID of file to be downloaded from Google Drive    |


### Implementation Notes

The `GOOGLE_FILE_ID` and `GOOGLE_DRIVE_CREDENTIALS` environment variables are
optional!  If they're not set, you should set `AUDIO_SRC` to a URL.  
`http://ice2.somafm.com/defcon-64-aac` works well for this.  If you do not set
the `AUDIO_SRC` environment variable, the device will play an audio file that's
embedded in the image itself.

If you want to use Google Drive to deliver media for your AudioDome devices,
you should follow one of these use cases:

1. The Google Drive file is a zip file containing one audio file, which is
 referenced (at its expanded location) by the `AUDIO_SRC` environment variable.
1. The Google Drive file is a zip file containing a number of audio files and
  a playlist file.  The playlist file is referenced with the `AUDIO_SRC`
  environment variable.
1. The Google Drive file is a zip file containing a playlist file, which
  references URLs that are supported by VLC.
