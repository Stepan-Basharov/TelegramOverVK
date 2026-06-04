from flask import Flask
import json

app = Flask(__name__)

def run_cycle():
    print("Cycle triggered!")


@app.route("/", methods=["GET", "POST"])
def handle():
    run_cycle()
    return "OK"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1984)
