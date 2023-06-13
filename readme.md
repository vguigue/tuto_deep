# Tutoriel pytroch

Introduction aux techniques de deep learning et formation à pytorch et à la logique modulaire.

Ces tutoriels sont directement inspirés de la documentation officielle pytorch, qui est très bien faite: [lien](https://pytorch.org/tutorials/)

En alternative à ce git: parmi les plus jolis cours sur pytorch: [lien](https://uvadlc-notebooks.readthedocs.io/en/latest/)

# 1. Prise en main de pytorch

* Notebook 0: Nouvelle structure de données (tensor) [pour ceux qui ne connaissent pas numpy]
* Notebook 1_1: Tensor, plus d'opérateurs, quelques petits exercices
* Notebook 1_2: Définition du gradient et différentiation automatique
    * Graphe de calcul, gradient et propagation de l'erreur
    * Optimisation 
    * Application sur le cas de la régression logistique
* Notebook 1_3: Construction d'un réseau de neurone simple
    * Checkpointing
    * Tensorboard
* Notebook 1_4: Outils connexes et modules avancés 
    * Chaine d'apprentissage standard
    * Régularisation


**En version colab** pour ceux qui ont des problèmes d'installation:
* Notebook 0: [lien](https://drive.google.com/file/d/1swmO4WyCXb2TZB_MFHY1kj7ZFOwdFA0R/view?usp=sharing)
* Notebook 1_1: [lien](https://drive.google.com/file/d/1e80ZbY2F-NQWDwLNhetTJPQtA9J8Ghzr/view?usp=share_link)
* Notebook 1_2: [lien](https://drive.google.com/file/d/12THYwuPXH-nzsXP63dJOcQhbD8m6so4Q/view?usp=share_link)
* Notebook 1_3: [lien](https://drive.google.com/file/d/1158XtT32ODqgwMSnh0JLrBn1L3ImzJfl/view?usp=share_link)
* Notebook 1_4: [lien](https://drive.google.com/file/d/1RmoMbB9NRDLhIj7dQXc9aSl3H1pMj36w/view?usp=share_link)

# 2. Architecture à convolution et récurrentes

* Notebook 0: qu'est ce qu'une convolution, comment paramétrer le module, comment jouer avec?
* Notebook 1: première(s) architecture(s) à convolution
   * Cas MNIST: récupération des données
* Notebook 2: introspection des modèles et interprétation post-hoc

# 3. Apprentissage de représentation

Apprendre des représentations continues (et optimisables) pour tous les *objets* qui nous intéressent, en particulier les objets discrets (mots, utilisateurs, produits)

* Notebook 1: Système de recommandation
* Notebook 2: Apprentissage de représentation des mots

# 4. Architectures récurrentes

Idéales pour traiter des séquences et en particulier des séquences de longueurs variables d'un exemple à l'autre.

* Notebook 1: Représentation d'une chaine de caractères


