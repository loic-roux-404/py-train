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

`say`: (Ajouter un message)

```
curl --request POST 'localhost:8081/say' \
--header 'Content-Type: application/json' \
--data-raw '{"txt": "coucou"}'
```

`declare`= localhost:8081/declare-change/false

`read-messages` = localhost:8081/read-message
