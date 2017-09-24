import requests


class Downloader(object):
    @classmethod
    def url_to_file(cls, url, file_path):
        '''Download a file  from URL to a path on disk.

        Args:
            url(str): Source file URL.
            file_path(str): Path to local destination file.

        '''
        with open(file_path, 'wb') as out_file:
            r = requests.get(url)
            out_file.write(r.content)
        return
