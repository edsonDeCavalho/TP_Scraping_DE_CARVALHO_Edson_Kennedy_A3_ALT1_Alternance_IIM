# -----------------------------------------------------------
# Cette class represente un titre
# email edson-kennedy.de_carvalho_pedro@edu.devinci.fr
# -----------------------------------------------------------
class Titre:

   def __init__(self,ordreDansLaPage,valeur,type):
        self.ordreDansLaPage=ordreDansLaPage
        self.valeur=valeur
        self.type=type

   def getString(self):
       return self.valeur
