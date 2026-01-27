from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps CI/CD on AWS is LIVE 🚀 and after day 3, it is pushed to docker automatically"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
