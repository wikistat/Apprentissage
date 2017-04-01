###<a href="http://www.insa-toulouse.fr/" ><img src="http://www.math.univ-toulouse.fr/~besse/Wikistat/Images/Logo_INSAvilletoulouse-RVB.png" style="float:left; max-width: 80px; display: inline" alt="INSA"/> |  [*Mathématiques Appliquées*](http://www.math.insa-toulouse.fr/fr/index.html), [`Science des Données`](http://www.math.insa-toulouse.fr/fr/enseignement.html) 

# Science des Données & Statistique

Schématiquement, la **Science des Données** est définie autour d'une *agrégation de compétences* en Informatique (langage comme [R](href="https://cran.r-project.org/) et [Python](https://www.python.org/) , gestion des données, calcul parallèle...), Statistique (exploration, estimation test, modélisation, prévision) Apprentissage Machine (prévision), Mathématiques (probabilités, optimisation, analyse fonctionnelle, graphes...). 

Son **apprentissage** est acquis par l'intermédiaire de scénarios d'analyse de données réelles, ou *tutoriel*, présentés sous forme de *calepins* ([*jupyter notebooks*](http://jupyter.org/)) en [R](href="https://cran.r-project.org/) ou [Python](https://www.python.org/).

Cette **pratique** est **indispensable** mais masque les *aspects théoriques* (mathématiques, statistiques): une *formule* est remplacée par un commande ou fonction en Python ou R, une *démonstration* par l'exécution d'exemples dans un calepin.

Pour offrir de la *profondeur*, plus de compréhension, à cette (auto)-formation, les calepins renvoient (liens hypertextes) systématiquement à des **vignettes "théoriques"**  du site [wikistat.fr](http://wikistat.fr/) exposant en détail (cours) les méthodes et algorithmes concernés.

Il ne s'agit pas simplement de pouvoir exécuter une méthode, un algorithme, il est important d'en **comprendre les propriétés**, conditions d'utilisation et limites.

# Saison 3 [*Apprentissage Machine / Statistique*](\http://wikistat.fr)

### Objectifs

Cette saison est consacrée à l'apprentissage des principales méthodes et algorihtmes d'apprentissage (supervisé) machine ou statistique listées dans les épisodes successifs.

### Prérequis
Avoir acquis les compétences des épisodes précédents ou revenir dans leurs saisons:

- [Initiation à R](https://github.com/wikistat/Intro-R)
- [Initiation à Python](https://github.com/wikistat/Intro-Python)
- Formation aux [outils Statistiques de base](https://github.com/wikistat/StatElem)
- [Exploration Statistique pour la Science des Données](https://github.com/wikistat/Exploration). Cet épisode intègre les algorithmes d'apprentissage non-supervisé (*clustering*).

### Organisation
Les **épisodes** ci-dessous sont associées à des calepins "fil rouge" ([prévision des pics d'ozone](https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone)) en R et Python. Exécuter les calepins en se référant, si nécessaire aux vignettes, (liens hypertextes) à chaque étape. 

Les [`exemples jouets`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet) servent aussi de *bac à sable* pour expérimenter chaque méthode. 

D'autres scénarios (exemples et cas d'usage ci-dessous), basés sur des jeux de données plus complets / complexes sont et seront disponibles dans ce même dépôt.

### Pour aller plus loin
Aborder la *Science des Données* avec les 

- [Technologies des grosses data](https://github.com/wikistat/Ateliers-Big-Data) (Hadoop Spark, XGBoost, Keras...)

## Épisodes 
Les [calepins]((https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone)) python et R "fil rouge", sont découpés en 4 épisodes listés ci-dessous. Le 5ème est illustré par des calepins spécifiques (à venir).

Pour chaque épisode, **suivre le cours** ou consulter les vignettes et exécuter les parties correspondantes des calepins . 

- Pic d'ozone: [calepin en R](https://github.com/wikistat/Apprentissage/blob/master/Pic-ozone/Apprent-R-Ozone.ipynb)
- Pic d'ozone: [calepin en Python](https://github.com/wikistat/Apprentissage/blob/master/Pic-ozone/Apprent-Python-Ozone.ipynb)

### Épisode 1 
- [Introduction: Apprentissage Machine pour la Science des données](http://wikistat.fr/pdf/st-m-app-intro.pdf)
- [Qualité de prévision, risque](http://wikistat.fr/pdf/st-m-app-risque-estim.pdf)
- [Rappels sur le modèle linéaire général](http://wikistat.fr/pdf/st-m-app-rlogit.pdf) (modèles gaussien et binomial)

### Épisode 2
- [Analyse discriminante, *k* plus proches voisins](http://wikistat.fr/pdf/st-m-app-add.pdf)
- [Arbres binaires de décision](http://wikistat.fr/pdf/st-m-app-cart.pdf)

### Épisode 3
- [Réseaux de neurones](http://wikistat.fr/pdf/st-m-app-rn.pdf), introduction au *deep learning*
- [Agrégation de modèles](http://wikistat.fr/pdf/st-m-app-agreg.pdf): *boosting, random forest*

### Épisode 4
- [Régression PLS](http://wikistat.fr/pdf/st-m-app-sparse-pls.pdf)
- [*Support Vector Machine*](http://wikistat.fr/pdf/st-m-app-svm.pdf)
- [Synthèse](http://wikistat.fr/pdf/st-m-app-conclusion.pdf)

### Épisodee 5 (en travaux)
- [Imputation de données manquantes](http://wikistat.fr/pdf/st-m-app-idm.pdf)
- [Détection de défaillances]() (*One class Classification, noveltry detection*) 


## Cas d'usage

- [`ExemplesJouet`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet) illustratifs sur données simulées:
	- Discrimination binaire en dimension 2: [`Nuages gaussiens`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Apprent-R-Clouds.ipynb) en R ou [`Blobs`](https://github.com/wikistat/Apprentissage/tree/master/ExemplesJouet/Apprent-Python-Blobs.ipynb) de Scikit-learn. Dessiner les frontières des classes selon les méthodes utilisées, rôle du paramètre de compexité;
	- Régression polynomiale en R, optimisation de la complexité (degré) par *Cp* de Mallows, régularisation *ridge* ou lasso.
- [`Pic d'ozone`](https://github.com/wikistat/Apprentissage/tree/master/Pic-ozone) Prévision de la concentration (régression) ou de dépassementdu seuil (discrimination binaire) légal d'ozone par la plupart des méthodes d'apprentissage. En R et en Python.
- [`Diagnostic coronarien`](https://github.com/wikistat/Apprentissage/tree/master/Diag-coro) Prévision du risque de coronopathie (discrimination binaire) par les principales méthodes d'apprentissage en R. Optimisation avec la librairie [`caret`](http://topepo.github.io/caret/index.html), introduction à l'implémentation de [`xgboost`](https://xgboost.readthedocs.io/en/latest/) en R.
- Les autres scénarios en R de [wikistat.fr](http://wikistat.fr/) seront progressivement intégrés.
