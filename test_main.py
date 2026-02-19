import pytest
from utils.files import Open

FILE_PATH = "./products.csv"
FAKE_FILE_PATH = "./non_existent_file.csv"

#testing the Open function with a real file path
def test_Open():
    def testing_function(filename, filepath, reader, root):
        return True
    result = Open(FILE_PATH,None, testing_function)
    assert result == True

#testing the Open function with a non-existent file path
def test_Open_FileNotFound():
    with pytest.raises(FileNotFoundError):
        Open(FAKE_FILE_PATH, None)


