#!/usr/bin/env python

from flask import request
from flask.wrappers import Response
from tinydb.queries import Query
import argparse

from model import Message, Client, DbManager, ClientQueries
from server import AppServer

debug = True
db_message = DbManager('messages')
db_client = DbManager('clients')
db_client_queries = ClientQueries(db_client)

app_server = AppServer(
    argparse.ArgumentParser(description='Hospital app', formatter_class=argparse.ArgumentDefaultsHelpFormatter),
    __name__
)
app = app_server.get_app()

@app.route('/', methods=['GET'])
def index():
	return Response({
        'messages': db_message.all(),
        'clients': db_client.all()
    })

@app.route('/hear/<host>', methods=['POST'])
def hear(host):
    message = Message.fromDict(request.json | {'host': host})

    if not db_client_queries.has(host):
        db_client.insert(Client(host))

    return db_message.insert(message)

@app.route('/declare/<covid>/<host>', methods=['GET'])
def declare(host, covid):
    client = None
    if not db_client_queries.has(host):
        client = Client(host)
        db_client.insert(client)

    if client is None:
        client = db_client_queries.find(host)

    declared = client.declare_covid(covid)

    return {"declared": declared}

@app.route('/read-messages/<host>', methods=['GET'])
def read_messages(host):

    if not db_client_queries.has(host):
        client = Client(host)
        db_client.insert(client)

    if host is not None:
        message: Query = Query();
        return db_message.search(message.host == host)

    return db_message.all()

app_server.start(debug)
