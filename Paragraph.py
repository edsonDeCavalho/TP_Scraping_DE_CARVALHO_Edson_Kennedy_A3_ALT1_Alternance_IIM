# -----------------------------------------------------------
# Cette class represente un paragraph
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------

class Paragraph:

   def __init__(self,ordreDansLaPage,valeur):
        self.ordreDansLaPage=ordreDansLaPage
        self.valeur=valeur

   def getString(self):
       return self.valeur