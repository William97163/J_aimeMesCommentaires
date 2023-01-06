Guide d'installation
====================

Procédure de mise à jour GitLab
-------------------------------

1. - Clone du projet :
Allez dans un dossier où vous voulez cloner le projet Faites un "git bash" here puis un 
"git clone https://gitlab.com/simplonclermontia3/vivelescollegues_william"

2. - Utilisation de l'application :
Ouvrez votre ide(ex : visual studio code) puis ouvrez le dossier créé "vivelescollegues_laurence" Parcourez le dossier 
"add_new_employees" puis lancez le script python "main.py" Remplissez les champs affichés et 
selectionnez un poste Appuyer sur enregistrer et votre employé sera ajouter localement à votre fichier employes.csv

3. - Création de branches :
Sur le terminal git, créez une branche à l'aide de git branch faites un git checkout 
pour vous positionner dessus faites un git add ., un git commit -m "votre message" puis un git push

4. - Merge request :
Retournez sur le proget git(GitLab) Allez dans l'onglet "Merge requests" 
Cliquez sur "New merge request" puis selectionnez votre branche pour la mettre dans la branche principale (main) 
Cliquez ensuite sur "Compare branches and continue" Décrivez les changments effectués dans 
"Description" Dans l'onglet Assignee, selectionnez un des 2 maintainers (Laurence Andraud ou William Carindo) 
Pour finir appuyer sur "Create merge request"

Et voila, vous n'avez plus qu'à attendre la validation du maintainer !!


liste de librairies à installer :
---------------------------------

1. Pandas

Pandas est une librairie python qui permet de manipuler facilement des données à analyser :

* manipuler des tableaux de données avec des étiquettes de variables (colonnes) et d'individus (lignes).
* ces tableaux sont appelés DataFrames, similaires aux dataframes sous R.
* on peut facilement lire et écrire ces dataframes à partir ou vers un fichier tabulé.
* on peut faciler tracer des graphes à partir de ces DataFrames grâce à matplotlib.

Voici la commande à effectuer pour installer cette librairie :

>>> pip install pandas

Si vous disposez d'un mac alors entrez la commande suivante : 

>>> pip3 install pandas

2. Tkinter 

Tkinter (Tk interface) est un module intégré à la bibliothèque standard de Python, permettant de créer des interfaces graphiques :

* des fenêtres,
* des widgets (boutons, zones de texte, cases à cocher, …),
* des évènements (clavier, souris, …).

Voici la commande à effectuer pour installer cette librairie :

>>> pip install tkinter 

Si vous disposez d'un mac alors entrez la commande suivante : 

>>> pip3 install tkinter