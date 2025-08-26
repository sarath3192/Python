from word_extractor import BaseExtractor
if __name__ == "__main__":
    # URL with a huge word list
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    
    # Small local word list
    array = ['one', 'two', 'three', 'four', 'five']
    
    # Initialize BaseExtractor object
    extractor = BaseExtractor()
    
    # Call both functions
    extractor.parse_url(url)   # This will use more memory
    extractor.parse_list(array)