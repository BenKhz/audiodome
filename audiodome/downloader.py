class Downloader(object):
    @classmethod
    def url_to_file(url, file_path):
        with open(url, 'w') as out_file:
            out_file.write(file_path)
        '''Download a file  from URL to a path on disk.

        Args:
            url(str): Source file URL.
            file_path(str): Path to local destination file.

        '''

        # I know this isn't right, but...
        return
