import os

from flask import Flask, render_template

app = Flask(__name__)
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


@app.get("/")
def home():
    return render_template("index.html", api_base_url=API_BASE_URL)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
