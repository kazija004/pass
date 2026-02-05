from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello it Kazija doing the PaaS Practical Session!"

if __name__ == "__main__":
    app.run()

