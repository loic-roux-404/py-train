import matplotlib.pyplot as plt # Génération de graphiques
import numpy as np # librairie mathématique

class Voiture():
    # Definition avec typage des propriéte de base de la classe
    vitesse: int = 0
    prix: int = 0
    puissance: int = 0

    # constructeur
    def __init__(self, prix, puissance, vitesse):
         self.vitesse = vitesse
         self.prix = prix
         self.puissance = puissance

    # Getters
    def getPrix(self) -> int:
          return self.prix

    def getVitesse(self) -> int:
          return self.vitesse

    def getPuissance(self)-> int:
          return self.puissance

class Pijo(Voiture):
    def __init__(self, prix, puissance, vitesse):
        super(Pijo, self).__init__(prix, puissance, vitesse)

class Rino(Voiture):
    def __init__(self, prix, puissance, vitesse):
        super(Rino, self).__init__(prix, puissance, vitesse)

class Bem(Voiture):
    def __init__(self, prix, puissance, vitesse):
        super(Bem, self).__init__(prix, puissance, vitesse)

# Creation de la classe enfant qui se construit en utilisant le parent
class Hodi(Voiture):
    def __init__(self, prix, puissance, vitesse):
        super(Hodi, self).__init__(prix, puissance, vitesse)

x = np.linspace(-30,30,1000)

# Fonction pour créer un graphe à partir d'une voiture
def graphe(voiture: Voiture) -> None:

    yh = np.sqrt(((x**2)/4) - 1)

    ### RuntimeWarning: invalid value encountered in sqrt x == 0 --> A commenter

    plt.axhline(y = 0, color = 'black')
    plt.axvline(x =0, color = 'black')

    # axe
    plt.plot(x, voiture.getPrix(),"blue")
    plt.plot(x, voiture.getPuissance(),"green")

    plt.plot(yh, voiture.getVitesse(),"turquoise")

    # plt.savefig('hyperbole.png', bbox_inches='tight')

    # Afficher le plot
    plt.show()


graphe(Hodi(20, 100, 80))
