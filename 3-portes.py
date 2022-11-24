"""
On a 3 portes dont une avec un trésor.

Nous devons établir les étapes suivantes :
1. Choisir une porte
2. Indication d'une porte vide autre que notre choix
3. 2 stratégies :
  1. Changer de choix
  2. Garder le choix

Faire une simulation et donner le pourcentage de réussite pour chaque stratégie afin de connaitre la stratégie la plus fiable.
"""

from random import randint, choice

def simul1(porte,choix,indication):
  for elt in porte.items():
    if elt[0] != choix and elt[0] != indication:
      choix = elt[0]
  return(porte[choix])

def simul2(porte,choix):
  return(porte[choix])

strat1 = 0
strat2 = 0

for i in range(1000):
  portes = {
      1: False,
      2: False,
      3: False
  }
  portes[randint(1,3)] = True
  choix = randint(1,3)
  portes_vide = []
  for elt in portes.items():
    if elt[1] != True and elt[0] != choix:
      portes_vide.append(elt[0])
  indication = choice(portes_vide)
  if simul1(portes,choix,indication):
    strat1 += 1
  if simul2(portes,choix):
    strat2 += 1

print(f"Pour 1000 simulations, la stratégie 1 fonctionne à {round(strat1/1000*100,2)}% en moyenne et la stratégie 2 fonctionne à {round(strat2/1000*100,2)}% en moyenne")