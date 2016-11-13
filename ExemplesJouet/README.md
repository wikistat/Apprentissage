###<a href="http://www.insa-toulouse.fr/" ><img src="http://www.math.univ-toulouse.fr/~besse/Wikistat/Images/Logo_INSAvilletoulouse-RVB.png" style="float:left; max-width: 80px; display: inline" alt="INSA"/> |  [*Mathématiques Appliquées*](http://www.math.insa-toulouse.fr/fr/index.html), [`Science des Données`](http://www.math.insa-toulouse.fr/fr/enseignement.html) 

# Tutoriels de Science des Données en [Python](https://www.python.org/) et [R](href="https://cran.r-project.org/)
# [Apprentissage Statistique](\http://wikistat.fr)

##  Exemples "Jouet": Discrimination et régression sur données simulées


Les méthodes de [discrimination](http://wikistat.fr/pdf/st-m-app-intro.pdf) sont  comparées sur deux jeux de données. 

- [`Apprent-R-Clouds`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Appent-R-Clouds.ipynb) Tutoriel en R. Simulations d'observations  suivant 4 gaussiennes bidimensionnelles et séparées en 2 classes. L'objectif est de mettre en évidence le rôle des paramètres de complexité de différentes méthodes (régression logistique, k-nn, réseaux de neurones, arbre de décision, *bagging*, svm) et de comparer les formes spécifiques des frontières estimées par chacune d'elle.
- [Apprent-Python-Blobs](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Apprent-Python-Blobs.ipynb) mêmes objectifs en Python avec des données fictives bidimensionnelles dont la simulation est une fonction de Scikit-learn. 

Stratégie similaire en régression:

- [`Apprent-R-RegPoly`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Apprent-R-RegPoly.ipynb) Tutoriel en R. La régression polynomiale edt optimisée (degré du polynôme) par différentes stratégies: sélection de variables par *Cp* de mallows, régularisations *l1* (*lasso*) et *l2* (*ridge*).
