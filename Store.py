# -----------------------------------------------------------
# Cette classsesert a stoquer les <tag> extraits dans la page
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------
from Titre import Titre
from Paragraph import Paragraph

class Store:
    def __init__(self):
        self.titres = {}
        self.paragrphes = {}
        self.tableaux = {}
        self.numberOfTitles = 0
        self.nombreDeParagraph = 0
        self.nombreDeTableaux = 0


    def getTitres(self):
        return self.titres

    def addTitles(self,title):
        self.titres[self.numberOfTitles]={
            Titre:title
        }
        self.incrementationNombreDeTires()
    def addParagraphs(self,paragraph):
        self.titres[self.numberOfTitles]={
            Paragraph:paragraph
        }
        self.incrementationNombreDeParagraphes()

    def addText(self, paragraph):
        self.titres[self.numberOfTitles] = {
            Paragraph: paragraph
        }
        self.incrementationNombreDeParagraphes()

    def addTableaux(self,tableaux):
        self.titres[self.numberOfTitles] = {
            Paragraph: tableaux
        }
        self.incrementationNombreDeParagraphes()

    def incrementationNombreDeTires(self):
        self.numberOfTitles=self.numberOfTitles+1

    def incrementationNombreDeParagraphes(self):
        self.nombreDeParagraph=self.nombreDeParagraph+1

    def incrementationNumbreDeTableaux(self):
        self.nombreDeTableaux=self.nombreDeTableaux+1

    def test(self):
        print(self.titres.get(0))