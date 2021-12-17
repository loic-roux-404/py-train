from argparse import ArgumentParser
from flask import Flask

# Module pour simplifier la création du serveur flask en fonction
# des paramètres du argument parser
class AppServer():
    def __init__(self, parser: ArgumentParser, name) -> None:

        parser.add_argument('--port', type=int, default=8080, help='Port to use')

        self.args = parser.parse_args()
        self.app = Flask(name)
        self.name = name
    # Récupérer l'appli flask
    def get_app(self) -> Flask:
        return self.app
    # Lancer le serveur
    def start(self, debug = False):
        if self.name == "__main__":
            self.app.run(host="0.0.0.0", port=self.args.port, debug=debug)

            return self.app
    # Méthode pour interargir avec l'argument parser et récupérer des variables
    def get_param(self, name: str):
        if hasattr(self.args, name):
            return getattr(self.args, name)
        else:
            print("missing param %s" % name)
            return ""
