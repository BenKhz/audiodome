# audiodome

Set the `AUDIO_SRC` environment variable to
`http://ice2.somafm.com/defcon-64-aac` or another similarly-encoded stream.

It may work with a URL to a playlist file.

Simple Notes:
    Download vs Stream?
    Download:
    using urllib to access URL and download.
        urllib.request.urlretrieve("URL", "Saved FilePath")
    Possible to use pip install pydrive and use that to download?

Stream:
   Use headless VLC player to connect to an icecast? Do I need control?

pip install dbus-python #dependency for vlc.ctrl

pip install vlc.ctrl #to control VLC through Dbus
