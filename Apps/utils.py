import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'1/<div\b[^>]>(.?)<\/div>/','',text )
    # Remove HTML tags
    text = re.sub(r'^http[s]?:\\/\\/(?: www\\.)?[- a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[- a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$', '', text)
    # Replaces multiple spaces with a single spaces
    text = re.sub(r'/\s\s+/g, ', '',text)
    # Replace extra white spaces
    text = re.sub(r'\s+', '',text)
