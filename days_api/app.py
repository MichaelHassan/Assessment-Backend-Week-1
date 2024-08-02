"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)

app_history = []

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return {"message": "Welcome to the Days API."}


@app.route("/scrape", methods=["GET", "POST"])
def scrape():


pass


if __name__ == "__main__":
    app.run(port=8080, debug=True)
