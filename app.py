from flask import Flask
from datetime import datetime, UTC

app = Flask(__name__)

@app.route("/")
def hello_world():
    return("<p>Hello, World!</p>"
    "<a href='/goodbye'>Goodbye</a><br>"
    "<a href='/customer'>Csustomer data</a>")

@app.route("/goodbye")
def goodbye_world():
    return "<p>Goodbye World :(</p>"

@app.route("/customer")
def sample_data():
    dt = datetime(2026, 11, 13, 12, 47, 30, tzinfo=UTC)
    return {
        "customer_id" : 123456,
        "customer_first_name" : "John",
        "customer_last_name" : "Jones",
        "last_updated" : dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "account_status" : "Open",
        "customer_phone" : "5558675309",
        "customer_email" : "JJones@notreal.com"
    }