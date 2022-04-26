import json
from os.path import exists

import requests
from bs4 import BeautifulSoup


class MorseLoader:
    
    def __init__(self, file:str='morse.json'):
        """Initializes the morse code table.
        If JSON does not exist: generates a JSON file with the letters as keys and the corresponding morse codes as values.
        If JSON does exist: loads the JSON file.

        Args:
            file (str, optional): Name for JSON file. Defaults to 'morse.json'.
        """
        if not exists(file):
            morse_html = get_html()
            morse_pairs = explore_data(html=morse_html)
            with open(file, mode='w') as morse_dict:
                morse_dict.write(json.dumps(morse_pairs))
        with open(file) as morse_dict:
            self.data = json.loads(morse_dict.read())

def get_html() -> str:
    """Sends a get request to morsecode.world to retrieve the morse code table HTML page as text.

    Returns:
        str: morsecode.world morse code table HTML page in text format.
    """
    with requests.Session() as s:
        res = s.get('https://morsecode.world/international/morse2.html')
        res.raise_for_status()

    return res.text

def explore_data(html:str) -> dict:
    """Fetches the morse code data from the retrieved HTML page.

    Args:
        html (str): HTML data in plain text format.

    Returns:
        dict: Dictionary where key is the letter and value is the morse code. Example: {'A': '.-', 'B': '-...', ...}
    """
    morse_dict = {}
    soup = BeautifulSoup(html, 'html.parser')

    for table in soup.find_all('table'):
        if table.find('th', string='Morse'):
            for row in table.find_all('tr'):
                if row.find(class_='morse'):
                    data = row.find_all('td')
                    morse_dict[data[0].span.text] = data[1].text

    return morse_dict
