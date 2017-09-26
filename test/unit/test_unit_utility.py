import imp
import os
modulename = 'audiodome'
modulepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
file, pathname, description = imp.find_module(modulename, [modulepath])
audiodome = imp.load_module(modulename, file, pathname, description)

# We keep our test files in the fixture directory.
fixture_path = os.path.join(modulepath, "test/fixture/")


class TestUnitUtility:
    def get_file_contents(self, file_path):
        with open(file_path, 'r') as in_file:
            contents = in_file.read()
        return contents

    def test_utility_b64_to_file(self):
        # This is the file that will be (re)created wvery time we run this test
        drop_file_location = os.path.join(fixture_path, "b64tst.local")
        # This is the file with base64-encoded contents
        b64_input_file = os.path.join(fixture_path, "b64_tst_fixture.json.b64")
        # This is the file that contains the unencoded content, for comparison
        b64_compare_file = os.path.join(fixture_path, "b64_tst_fixture.json")
        # Base64 input data from file
        b64_data = self.get_file_contents(b64_input_file)
        # Unencoded comparison data
        expanded_data = self.get_file_contents(b64_compare_file)
        utility_obj = audiodome.Utility
        utility_obj.b64_to_file(b64_data, drop_file_location)
        # Make sure that the just-written file contents equal the test data
        assert self.get_file_contents(drop_file_location) == expanded_data

    def test_unit_utility_unzip_to_path(self):
        # Control file
        control_file = os.path.join(fixture_path, "unzipped.txt")
        # Test output file location (expected, anyway)
        test_output_file = os.path.join(fixture_path, "unzipped.txt.local")
        # Zipfile to deflate
        zip_infile = os.path.join(fixture_path, "tstfile.zip")
        # Give us a Utility object to work with
        utility_obj = audiodome.Utility
        # Unzip the file to the fixture directory
        utility_obj.unzip_file_to_path(zip_infile, fixture_path)
        control_file_contents = self.get_file_contents(control_file)
        test_extracted_contents = self.get_file_contents(test_output_file)
        assert test_extracted_contents == control_file_contents

    def test_playlist_generator(self):
        # Control list
        control_list = ("04 All of Us.mp3", "05 Come and Find Me.mp3",
                                            "06 Searching.mp3")
        test_env_var_file = os.path.join(fixture_path, "tst_playlist.txt")
        tested_list = test_env_var_file.list
        assert control_list == tested_list
