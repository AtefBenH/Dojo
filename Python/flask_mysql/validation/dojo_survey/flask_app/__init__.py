from flask import Flask, session, redirect, render_template, request
app = Flask(__name__)
app.secret_key = "NoSecretsOnGitHub"