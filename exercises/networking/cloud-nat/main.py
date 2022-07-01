import re
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'Home'

@app.route("/run-ip")
def ip():
    response = requests.get('http://checkip.dyndns.org').text
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', response)
    return f"The Cloud Run app's external IP address is: {ip[0]}\n"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")

