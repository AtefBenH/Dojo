from flask import Flask
app = Flask(__name__)
app.secret_key = "NoSecretsOnGitHub"
DATABASE = "log_reg_schema"