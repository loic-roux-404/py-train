# Rendu covid

## Mise en place de l'environnement
voir sujet ou la [documentation flask](https://flask.palletsprojects.com/en/1.1.x/installation/) pour les différences de système d'exploitation…
1. Créer un fork pour votre groupe…
2. Cloner votre projet
3. Installer virtualenv (si pas encore fait)
4. Créer un environnement avec la commande
``python3 -m venv venv-TPSID`` (avec “venv-TPSID” le nom de votre environnement)
5. Activer l'environnement
``source venv-TPSID/bin/activate`` (Linux/Mac)
``venv-TPSID\Scripts\activate`` (Windows)
6. ``python -m pip install -r requirements.txt``

# Tests

- Lancer le serveur de l'hôpital : `./hospital.py`
- Lancer un client : `./client.py --port 8081`

### Urls Hôpital

> Pour les méthodes GET on peut utiliser chrome

`localhost:8080`, méthode GET pour voir toutes les données de l'hôpital

Exemple : http://localhost:8080

### Urls Client

`http://localhost:8081/declare/<covid>`, méthode GET avec un paramètre `<covid>`

Exemple : http://localhost:8081/declare-change/false

`localhost:8081/read-messages`, méthode GET, Voir les messages du client

Exemple : http://localhost:8081/read-messages

`localhost:8081/read-cases`, méthode GET : pour lister les cas de covid et leur date de début

Exemple : http://localhost:8081/read-cases

`localhost:8081/say`, méthode : POST

Exemple avec la commande curl :
```
curl --request POST 'localhost:8081/say' \
--header 'Content-Type: application/json' \
--data-raw '{"txt": "coucou"}'
```
