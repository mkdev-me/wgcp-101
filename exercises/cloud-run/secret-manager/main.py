import os
import re
from flask import Flask
from google.cloud import secretmanager

app = Flask(__name__)

@app.route("/")
def home():
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/77372655291/secrets/cloudrun/versions/1"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
