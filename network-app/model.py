from datetime import date, datetime
import json
from tinydb import TinyDB, Query

# Intérargir avec la base de donnée json tinydb en isolant la gestion
# en fonction de l'entité
# Les méthodes de bases sont copiées pour simplifier l'utilisation
class DbManager():
    ERR_EMPTY_DB = {"error": "Empty db"}
    def __init__(self, dbName: str) -> None:
        self.db = TinyDB("db/%s.json" % dbName)

    def insert(self, entity: 'entity'):
        return {'status': self.db.insert(entity.toDict())}

    def update(self, entity: 'entity', query: Query):
        return {'status': self.db.update(entity.toDict(), query)}

    def search(self, q: Query):
        return {'data': self.db.search(q)}

    def all(self):
        return {'data': self.db.all() or self.ERR_EMPTY_DB}

class entity():
    # taken from https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
    # Pour convertir l'entité au format json afin de pouvoir le communiquer facilement
    # Entre les deux serveurs
    def toJSON(self):
        return  json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )
    # Convertir l'entité en dict python
    def toDict(self):
        return self.__dict__

class Client(entity):
    QUANRANTINE_DURATION = 10
    def __init__(self, host, messages: 'list[Message]' = []) -> None:
        self.host = host
        self.messages = messages
        self.covid_date_start = None

    def add_message(self, m: 'Message'):
        self.messages.append(m)

    def declare_covid(self, covid):
        covid = json.loads(covid.lower())

        if not self.covid_date_start and covid:
            self.covid_date_start = date.today().strftime("%d%m%Y")
            return covid

        if not covid:
            self.covid_date_start = None

        self.expired_covid()

        return covid

    def expired_covid(self):
        covid_date = datetime.strptime(self.covid_date_start, '%d%m%Y')
        if abs(covid_date - date.today()).days >= self.QUANRANTINE_DURATION:
            self.covid_date_start = None

    @staticmethod
    def fromDict(d: dict):
        obj_messages: list[Message] = []

        for _, msg in d['messages']:
            obj_messages.append(Message.fromDict(msg))

        return Client(d['host'], obj_messages)

# Ajouter des requètes pour chercher des informations
# particulières en base de données sur la partie client
class ClientQueries():
    def __init__(self, en: DbManager):
        self.manager = en

    def has(self, host) -> bool:
        c = Query()
        return len(self.manager.search(c.host == host)['data']) > 0

    def find(self, host) -> Client:
        c = Query()
        d = self.manager.search(c.host == host)['data']
        d = d[0] if len(d) > 0 else None

        if d == None:
            return {}

        return Client.fromDict(d)


class Message(entity):
    def __init__(self, txt: str, clientHost: str) -> None:
        self.txt = txt
        self.host = clientHost

    @staticmethod
    def fromDict(d: dict):
        print(d)
        return Message(d['txt'], d['host'])
