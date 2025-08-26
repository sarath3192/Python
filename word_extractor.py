from memory_profiler import profile
import requests

class BaseExtractor:
    # Function to write words from a list into a file
    @profile  # This decorator will monitor memory usage
    def parse_list(self, array):
        with open('words.txt', 'w') as f:
            for word in array:
                f.writelines(word + "\n")

    # Function to fetch data from a URL and save it
    @profile
    def parse_url(self, url):
        response = requests.get(url).text
        with open('url.txt', 'w') as f:
            f.writelines(response)