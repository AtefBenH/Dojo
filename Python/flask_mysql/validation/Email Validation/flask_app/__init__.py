from flask import Flask
app = Flask(__name__)
app.secret_key = "NoSecretsOnGitHub"
DATABASE = "email_schema"