#!/usr/bin/env python

# Imports
import ConfigParser
from modules.bottle import Bottle, template

# Config
config = ConfigParser.ConfigParser()
config.read("app.cfg")
catchall = config.getboolean('bottle', 'catchall')

# App
app = Bottle(catchall)

@app.get('/hello/<name>')
def index(name='World'):
  return template('<b>Hello {{name}}</b>!', name=name)
