# BACKEND_ECOMMERCE
--------------------------------Installation de PiP-----------------------------
Sous Linux : apt-get install python-pip          puis pip -V pour verifier.
Sous windows (Necessite python :https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe) puis Telecharge https://bootstrap.pypa.io/get-pip.py ça et lance la commande : python get-pip.py                     puis pip -V pour verifier.
Sous mac : brew install python-pip (ou python ou pip)
--------------------------------------------------------------------------------

Virtualenv , il permet de se creer un terminal virtuel ne disposant uniquement des versions des dependances qui sont utiles au projet, pratique quand on a besoin de version depréciées, celà permet de ne pas toucher à sa version de python installée par exemple sur sa propre machine si nous avons besoin d'une version ulterieure.
(au taff je peux pas utiliser npm donc pas de front pour moi sur mon temps de travail) 

dans un terminal : pip install virtualenv Django Django-rest-framework Django-cors-headers djoser pillow stripe npm

Maintenant on va créer l'environnement virtuel qu'il faudra relancer à chaque fois que l'on ferme le terminal(d'où un script au demarrage du serveur)
(A mon sens il est facultatif sur une machine qui n'a pas besoin d'autres versions des paquets, la preuve je ne m'en sers pas sous mac et je fais tourner le projet)

----------------CREATE VENV---------------- 
virtualenv virtualenv_name
virtualenv -p /usr/bin/python3 virtualenv_name (avec version de python spécifique)
--------------------------------------------- 

----------------activate VENV ---------------- 
source virtualenv_name/bin/activate
----------------------------------------------- 
deactivate (pour desactiver)

Pour lancer le serveur backend Django : il faut faire un cd dans le dossier backend (là ou il y un fichier manage.py) et faire : python3 manage.py runserver

Si tout se passse bien tu peux alors acceder au backend base article sur un navigateur au 127.0.0.1/8000/admin

#FRONTEND_ECOMMERCE

Npm install axios
Npm install bulma

Lancement sur serveur frontend : il faut faire un cd au préalable dans le dossier front end et lancer :
npm run serve

Si tout se passe bien la page 127.0.0.1 dans un navigateur doit alors te donner le front end de la boutique en fonction de la branche que tu as demandé, 
--------------------------------------------------

