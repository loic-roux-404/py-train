#!/usr/bin/env python
import argparse
from flask import request
import requests
from server import AppServer

args_parser = argparse.ArgumentParser(
    description='Client app',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

args_parser.add_argument('--hospital', type=str, default="localhost:8080", help='hospital server to use')

app_server = AppServer(args_parser, __name__)
app = app_server.get_app()

hospital_host = "http://%s" % (app_server.get_param('hospital'))

def hospital_get_request(route = "/", params = {}):
    print(requests.get('%s/%s/%s' % (hospital_host, route, request.host), params=params))
    return requests.get('%s/%s/%s' % (hospital_host, route, request.host), params=params).json()

def hospital_post_request(route, json: dict):
    return requests.post('%s/%s/%s' % (hospital_host, route, request.host), json=json).json()

@app.route('/say', methods=['POST'])
def say():
    if 'txt' not in request.json:
        return {"error": "Missing 'txt' of message"}

    return hospital_post_request('/hear', json=request.json)

@app.route('/declare-change/<covid>', methods=['GET'])
def declare_change_hospital(covid = None):
	return hospital_get_request('declare/%s' % covid or False)

@app.route('/read-messages', methods=['GET'])
def read_messages():
	return hospital_get_request('read-messages')

app_server.start(True)
