import os
import re
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    hostname = "10.32.10.3"
    response = os.system("curl --connect-timeout 4 " + hostname)
    if response == 0:
      return f"can connect"
    else:
      return f"CAN'T connect"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")

