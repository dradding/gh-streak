from flask import Flask
from bs4 import BeautifulSoup

import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<username>')
def catch_all(username):
    r  = requests.get("http://www.github.com/" + username)
    data = r.text
    soup = BeautifulSoup(data)
    total = soup.find_all(class_="contrib-number")[2].text
    return username + " has a streak of " + total

if __name__ == "__main__":
    app.run()
