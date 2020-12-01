# Author-Patrick Rainsberry
# Description-Chuck Norris Jokes using the Requests Package

import adsk.core, adsk.fusion, adsk.cam, traceback

import os
import sys


def remove_from_path(name):
    if name in sys.path:
        sys.path.remove(name)
        remove_from_path(name)


app_path = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_path, 'lib'))
import requests
remove_from_path(os.path.join(app_path, 'lib'))

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        r = requests.get('https://api.chucknorris.io/jokes/random')
        r_json = r.json()
        joke = r_json['value']
        ui.messageBox(joke)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
