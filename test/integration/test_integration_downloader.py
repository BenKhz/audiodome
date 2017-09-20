import imp
import os
modulename = 'audiodome'
modulepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
file, pathname, description = imp.find_module(modulename, [modulepath])
audiodome = imp.load_module(modulename, file, pathname, description)

# We keep our test files in the fixture directory.
fixture_path = os.path.join(modulepath, "test/fixture/")


class TestIntegrationDownloader:
    def test_integration_downloader_url_to_file(self):
        # We are going to download a test fixture from Github.
        url = "https://github.com/BenKhz/audiodome/raw/master/test/fixture/tstfile.zip"  # NOQA
        # This is the local path we put the file contents into
        local_path = os.path.join(fixture_path, "tstfile.zip.local")
        # This is the same file, we already have on disk
        control_path = os.path.join(fixture_path, "tstfile.zip")
        # Tell the downloader to get the file and save it on disk
        audiodome.Downloader.url_to_file(url, local_path)
        # Get the size of the control file and the test file
        control_file_size = os.path.getsize(control_path)
        test_file_size = os.path.getsize(local_path)
        assert control_file_size == test_file_size
