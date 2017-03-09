###<a href="http://www.insa-toulouse.fr/" ><img src="http://www.math.univ-toulouse.fr/~besse/Wikistat/Images/Logo_INSAvilletoulouse-RVB.png" style="float:left; max-width: 80px; display: inline" alt="INSA"/> |  [*Mathématiques Appliquées*](http://www.math.insa-toulouse.fr/fr/index.html), [`Science des Données`](http://www.math.insa-toulouse.fr/fr/enseignement.html) 

# Tutoriels de *Science des Données* en [Python](https://www.python.org/) et [R](https://cran.r-project.org/)

# [Apprentissage Statistique / Machine](\http://wikistat.fr)

### Objectifs

L'objectif de ces tutoriels, présentés sous forme de calepins ([*jupyter notebooks*](http://jupyter.org/)) codés en R ou Python, est d'introduire, par la pratique, les méthodes et techniques de la statistique ou de la *Sciences des données*. Des sénarios détaillent des exemples ou cas d'usage  d'analyses de données "réelles".  Ce dépôt est consacré à l'apprentissage statistique / machine.  

Par ailleurs, les méthodes utilisées  sont exposées dans les vignettes de [wikistat](http://wikistat.fr/).

### Prérequis
Avoir acquis les compétences des épisodes précédents ou revenir dans leurs saisons:

- [Initiation à R](https://github.com/wikistat/Intro-R)
- [Initiation à Python](https://github.com/wikistat/Intro-Python)
- Formation aux [outils Statistiques de base](https://github.com/wikistat/StatElem)
- [Exploration Statistique pour la Science des Données](https://github.com/wikistat/Exploration). Cet épisode intègre les algorithmes d'apprentissage non-supervisé (*clustering*).

### Organisation
Les épisodes ou **séances** ci-dessous sont associées à des calepins "fil rouge" ([prévision des pics d'ozone](https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone)) en R et Python. Exécuter les calepins en se référant, si nécessaire aux vignettes, (liens hypertextes) à chaque étape. 

Les [`exemples jouets`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet) servent aussi de *bac à sable* pour expérimenter chaque méthode. 

D'autres scénarios (exemples et cas d'usage ci-dessous), basés sur des jeux de données plus complets / complexes sont et seront disponibles dans ce même dépôt.

### Pour aller plus loin
Aborder la *Science des Données* avec les 

- [Technologies des grosses data](https://github.com/wikistat/Ateliers-Big-Data) (Hadoop Spark, XGBoost, Keras...)

## Liste des épisodes / séances 
Les [calepins]((https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone)) python et R, sont découpés en 4 séances listées ci-dessous. La 5ème est illustrée par des calepins spécifiques (à venir).

Pour chaque séance, **suivre le cours** ou consulter les vignettes puis exécuter les parties des calepins correspondants. 

- Pic d'ozone: [calepin en R](https://github.com/wikistat/Apprentissage/blob/master/Pic-ozone/Apprent-R-Ozone.ipynb)
- pic d'ozone: [calepin en Python](https://github.com/wikistat/Apprentissage/blob/master/Pic-ozone/Apprent-Python-Ozone.ipynb)

### Séance 1 
- [Introduction: Apprentissage Machine pour la Science des données](http://wikistat.fr/pdf/st-m-app-intro.pdf)
- [Qualité de prévision, risque](http://wikistat.fr/pdf/st-m-app-risque-estim.pdf)
- [Rappels sur le modèle linéaire général](http://wikistat.fr/pdf/st-m-app-rlogit.pdf) (modèles gaussien et binomial)

### Séance 2
- [Analyse discriminante, *k* plus proches voisins](http://wikistat.fr/pdf/st-m-app-add.pdf)
- [Arbres binaires de décision](http://wikistat.fr/pdf/st-m-app-cart.pdf)

### Séance 3
- [Réseaux de neurones](http://wikistat.fr/pdf/st-m-app-rn.pdf), introduction au *deep learning*
- [Agrégation de modèles](http://wikistat.fr/pdf/st-m-app-agreg.pdf): *boosting, random forest*

### Séance 4
- [Régression PLS](http://wikistat.fr/pdf/st-m-app-sparse-pls.pdf)
- [*Support Vector Machine*](http://wikistat.fr/pdf/st-m-app-svm.pdf)
- [Synthèse](http://wikistat.fr/pdf/st-m-app-conclusion.pdf)

### Séance 5 (en travaux)
- [Imputation de données manquantes](http://wikistat.fr/pdf/st-m-app-idm.pdf)
- [Détection de défaillances]()(*One class Classification, noveltry detection*) 


## Exemples et cas d'usage

- [`ExemplesJouet`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet) illustratifs sur données simulées:
	- Discrimination binaire en dimension 2: [`Nuages gaussiens`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Apprent-R-Clouds.ipynb) en R ou [`Blobs`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Apprent-Python-Blobs.ipynb) de Scikit-learn. Dessiner les frontières des classes selon les méthodes utilisées, rôle du paramètre de compexité;
	- Régression polynomiale en R, optimisation de la complexité (degré) par *Cp* de Mallows, régularisation *ridge* ou lasso.
- [`Pic d'ozone`](https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone) Prévision de la concentration (régression) ou de dépassementdu seuil (discrimination binaire) légal d'ozone par la plupart des méthodes d'apprentissage. En R et en Python.
- [`Diagnostic coronarien`](https://github.com/wikistat/Apprentissage/tree/master/Diag-coro) Prévision du risque de coronopathie (discrimination binaire) par les principales méthodes d'apprentissage en R. Optimisation avec la librairie [`caret`](http://topepo.github.io/caret/index.html), introduction à l'implémentation de [`xgboost`](https://xgboost.readthedocs.io/en/latest/) en R.
- Les autres scénarios en R de [wikistat.fr](http://wikistat.fr/) seront progressivement intégrés.
