
def log(text, typeT="LOG"):
	print("[{}] {}".format(typeT, text))

import tempfile
import urllib.request

def temp_file(url):
    # Create a temporary file to store the downloaded content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Download the file from the URL and write it to the temporary file
        with urllib.request.urlopen(url) as response:
            temp_file.write(response.read())
    
    # The path to the temporary file is available as temp_file.name
    return temp_file.name