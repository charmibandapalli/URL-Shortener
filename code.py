from flask import Flask, request, redirect
import random, string

app = Flask(__name__)
urls = {}

def generate_short():
    return ''.join(random.choices(string.ascii_letters, k=6))

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.json["url"]
    short = generate_short()
    urls[short] = long_url
    return {"short_url": f"http://localhost:5000/{short}"}

@app.route("/<short>")
def redirect_url(short):
    return redirect(urls.get(short, "/"))

if __name__ == "__main__":
    app.run(debug=True)
