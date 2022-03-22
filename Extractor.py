# -----------------------------------------------------------
# Cette classse sert a extraire differentes <tag> de la page
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------
import requests
import requests_cache
from bs4 import BeautifulSoup

from Paragraph import Paragraph
from Store import Store
from Titre import Titre

class Extractor:
    def __init__(self,url):
        self.url=url
        self.store=Store()
        self.nombreDeElmentsCaptures=0

    def incrementation(self):
        self.nombreDeElmentsCaptures=self.nombreDeElmentsCaptures+1


    def extract_Title_H1(self):
        page = self.url
        page = requests.get(page).text
        soup = BeautifulSoup(page, 'html.parser')
        h1=soup.h1
        self.incrementation()
        titre=Titre(self.nombreDeElmentsCaptures,h1.text.strip(),"h1")
        self.store.addTitles(titre)

    def extract_Title_H2(self):
        page = self.url
        page = requests.get(page).text
        soup = BeautifulSoup(page, 'html.parser')
        h1 = soup.h2
        self.incrementation()
        titre = Titre(self.nombreDeElmentsCaptures, h1.text.strip(), "h2")
        self.store.addTitles(titre)

    def extract_Paragraphs(self):
        page = self.url
        page = requests.get(page).text
        soup = BeautifulSoup(page, 'html.parser')
        section = soup.find(class_='mw-parser-output').find_all('p')
        p = [ele for ele in section]
        print(p[0].text.strip())
        paragraph=Paragraph(self.nombreDeElmentsCaptures,p[0].text.strip())
        self.store.addParagraphs(paragraph)
       # self.store.addParagraphs()

    def extractTaleaux(self):
        page = self.url
        page = requests.get(page).text
        soup = BeautifulSoup(page, 'html.parser')
        tableaux = soup.findAll('table',limit=2)
        row = [ele for ele in tableaux]
        for element in row:
            cols = [element.text.strip().replace("\n", "").split(' ') for ele in element]
            cols = list(filter(None, cols))
            cols[0] = [i for i in cols[0] if i != '']
            print(cols[0])
            self.store.addTableaux(cols[0])
            #print(len(tableaux))







