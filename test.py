class Livres():
    def __init__(self, titre, auteur, nbr_pages, disponible):
        self.titre = titre
        self.auteur = auteur   
        self.nbr_pages = nbr_pages
        self.disponible = bool(disponible)
    
    def reponse(self):
        print(self.titre)
        print(self.auteur)
        print(self.nbr_pages)
        print(self.disponible)


class CompteBancaire():
    def __init__(self, titulaire):
        self.__solde = 0
        self.titulaire = titulaire
    
    def deposer(self, montant):
        self.__solde += montant
        return self.__solde

    def retirer(self, montant):
        self.__solde -= montant
        return self.__solde

    def obtenir_solde(self):
        return self.__solde

class Voiture():
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.vitesse = 0

    def accelerer(self, valeur):
        self.vitesse += valeur
        return self.vitesse
    
    def ralentir(self, valeur):
        self.vitesse -= valeur
        return self.vitesse

class Etudiant():
    def __init__(self, nom, age, *classe):
        self.nom = nom
        self.age = age
        if classe != "Terminale" and not None:
            self.classe = classe 
        else:
            self.classe = "Terminale"

    def se_presenter(self):
        presentation = "Bonjour je m'appelle"
        return self.nom, self.age, self.classe

class Pile:
    def __init__(self):
        # Initialise une pile vide
        self.elements = []

    def Vide(self):
        # Renvoie True si la pile est vide, False sinon
        return len(self.elements) == 0

    def Empiler(self, element):
        # Ajoute un élément au sommet de la pile
        self.elements.append(element)

    def Depiler(self):
        # Retourne et retire l'élément en haut de la pile
        if self.Vide():
            raise IndexError("La pile est vide")
        return self.elements.pop()

# Exemple d'utilisation
pile = Pile()
pile.Empiler(10)
pile.Empiler(20)
print(pile.Depiler())  # Affiche 20
print(pile.Depiler())  # Affiche 10
# Si on tente de dépiler à nouveau, une erreur sera générée.
