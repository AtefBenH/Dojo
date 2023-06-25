from flask import Flask
import uuid

app = Flask(__name__)

app.secret_key = uuid.uuid4().hex