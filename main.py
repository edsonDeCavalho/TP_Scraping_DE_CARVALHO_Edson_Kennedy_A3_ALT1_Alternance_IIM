# -----------------------------------------------------------
# Dans ce fichier en lance le script
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('td_project_cache')

from Titre import Titre
from Extractor import Extractor



if __name__ == "__main__":
    extractor=Extractor("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    extractor.extract_Title_H1()
    extractor.extract_Title_H2()
    extractor.extract_Paragraphs()
    extractor.extractTaleaux()

