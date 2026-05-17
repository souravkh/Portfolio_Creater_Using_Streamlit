import json
from pathlib import Path


class JsonImporter:
    """
    JsonImporter is a utility class responsible for loading JSON data from a file.

    It provides a static method `load_data_from_file(file_path)` which validates the input file path,
    checks if the file exists, and then reads and parses the JSON content.

    If the file path is invalid or the file does not exist, it raises appropriate exceptions
    (ValueError or FileNotFoundError). The method returns the JSON content as a Python object
    such as a dictionary or list.
    """ 

    @staticmethod
    def load_data_from_file(file_path):
        """
        This function `load_data_from_file(file_path)` loads JSON data from a given file path.

        It first validates the input to ensure the file path is not null, empty, or whitespace.
        Then it checks whether the file exists at the specified location and raises a FileNotFoundError if it does not exist.

        If the file is valid, it opens the file in read mode with UTF-8 encoding, parses the JSON content, and returns it as a Python object (such as a dictionary or list).
        """
        if not file_path or file_path.strip() == "":
            raise ValueError("File path is not valid")

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return data