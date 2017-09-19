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
