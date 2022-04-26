import csv

import requests
from bs4 import BeautifulSoup


class MorseGenerator:
    
    def __init__(self, filename:str='table.csv'):
        self.filename = filename
        self.html = self.__get_html()
        self.morse_data = self.__explore_data()
        self.__write_to_csv()

    def __get_html(self) -> str:
        """Sends a get request to morsecode.world to retrieve the morse code table HTML page as text.

        Returns:
            str: morsecode.world morse code table HTML page in text format.
        """
        with requests.Session() as s:
            res = s.get('https://morsecode.world/international/morse2.html')
            res.raise_for_status()

        return res.text

    def __explore_data(self) -> list:
        """Fetches the morse code data from the retrieved HTML page.

        Returns:
            list: List of relevant morse letter / code pairs. Example: [{'letter': 'A', 'code': '.-'},...]
        """
        morse_pairs = []
        soup = BeautifulSoup(self.html, 'html.parser')

        for table in soup.find_all('table'):
            if table.find('th', string='Morse'):
                for row in table.find_all('tr'):
                    if row.find(class_='morse'):
                        data = row.find_all('td')
                        morse_pairs.append({
                            'letter': data[0].span.text,
                            'code': data[1].text
                        })

        return morse_pairs

    def __write_to_csv(self):
        """Writes the retrieved morse code data into a .CSV file.
        """
        with open(file=self.filename, mode='w', newline='') as morse_csv:
            morse_writer = csv.writer(morse_csv, delimiter=',')
            for morse_pair in self.morse_data:
                morse_writer.writerow([morse_pair['letter'], morse_pair['code']])

