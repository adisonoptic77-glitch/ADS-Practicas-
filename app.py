print("Hola mi nombre es adison")
print("naci el 24 de agosto de 2007")
print("calle capitan antonio fernandez becerra, san diego")
print("18")
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/saludo", methods=["GET"])
def home():
    return jsonify({"mensaje": "API funcionando"})


if __name__ == "__main__":
    app.run(debug=True)
    