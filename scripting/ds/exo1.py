# Chaine de caractère multiligne
# format pydocs
"""
Created on Tue Apr 27 17:16:31 2021

@author: bebo
"""

# import des librairies
import time # manipulation de temps
import numpy as np # librairie mathématique
import matplotlib.pyplot as plt # Génération de graphiques


# x^2 + y^2 = z^2 tg^2 (angle)
# Boucle avec 100 itétation, i vaut l'index l'itétation courante
for i in range(100) :
    theta = np.linspace(-4 * np.pi, 4 * np.pi, i) # création du  cadre du graphique et de graduations
    z = np.linspace(-2, 0, i)  # Création du tableau de l'axe z entre -2 et 2

    r = z**2 + 1 # radius
    x = r * np.sin(theta)  # Création du tableau de l'axe x
    y = r * np.cos(theta)  # Création du tableau de l'axe y

    # Tracé du résultat en 3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')  # Affichage en 3D
    ax.plot(x, y, z)  # Tracé de la courbe 3D

    plt.title("Courbe 3D") # Nommer le graphique

    # Label des axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Ajustement auto des plots
    plt.tight_layout()

    plt.show() # Afficher le graphique
    # attendre 0.10 seconde avant la prochaine itétation
    time.sleep(0.10)
