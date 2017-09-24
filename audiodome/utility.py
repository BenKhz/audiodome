import base64
import zipfile


class Utility(object):
    @classmethod
    def b64_to_file(cls, b64_data, file_path):
        with open(file_path, 'w') as out_file:
            out_file.write(base64.b64decode(b64_data))
        return

    @classmethod
    def unzip_file_to_path(cls, zip_infile, out_dir):
        with zipfile.ZipFile(zip_infile, 'r') as zip_ref:
            zip_ref.extractall(out_dir)
