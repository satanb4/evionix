from flask import Flask
from config import Config

app = Flask(__name__,static_url_path="/static")

from app import routes