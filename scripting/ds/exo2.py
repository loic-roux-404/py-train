# Code special pour certains editeur de code
# -*- coding: utf-8 -*-
# Chaine de caractère multiligne
"""
Created on Tue Apr 27 16:12:19 2021

@author: bebo
"""
# import des librairies
import numpy as np # librairie mathématique
import matplotlib.pyplot as plt # Génération de graphiques

x=np.linspace(-30,30,1000)

###### hyperbole  (x^2 /a^2) - (y^2 / b^2)= 1 a= 2 b =1
######       (x^2 /2^2) -  (y^2 /1^2 )  =1
######       y = sqrt( ( x^2 /4) - 1)

yh = np.sqrt(((x**2)/4) - 1) # ne pas utiliser math.sqrt !!!!

### RuntimeWarning: invalid value encountered in sqrt x == 0 --> A commenter

plt.axhline(y = 0, color = 'black')
plt.axvline(x =0, color = 'black')

# axe 
plt.plot(x, yh,"blue")
plt.plot(x,-yh,"green")

plt.plot(yh,x,"turquoise")
plt.plot(-yh,x,"pink")

# plt.savefig('hyperbole.png', bbox_inches='tight')

# Afficher le plot
plt.show()
