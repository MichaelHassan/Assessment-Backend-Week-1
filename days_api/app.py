"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)

app_history = []

app = Flask(__name__)


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


@app.route("/between", methods=["POST"])
def between():
    add_to_history(request)
    data = request.json
    if data.get("first") and data.get("last"):

        try:
            first = convert_to_datetime(request.json["first"])
            last = convert_to_datetime(request.json["last"])
            result = get_days_between(first, last)
        except TypeError:
            return {"error": "Unable to convert value to datetime."}, 400
        except ValueError:
            return {"error": "Unable to convert value to datetime."}, 400

        return {"days": result}, 200

    return {"error": "Missing required data."}, 400


@app.route("/weekday", methods=["POST"])
def weekday():
    add_to_history(request)
    data = request.json
    if data.get("date"):

        try:
            day = convert_to_datetime(request.json["date"])
            result = get_day_of_week_on(day)
        except TypeError:
            return {"error": "Unable to convert value to datetime."}, 400
        except ValueError:
            return {"error": "Unable to convert value to datetime."}, 400

        return {"weekday": result}, 200

    return {"error": "Missing required data."}, 400


@app.route("/history", methods=["GET", "DELETE"])
def history():
    add_to_history(request)

    if request.method == "GET":

        args = request.args.to_dict()

        if args.get("number"):

            if args.get("number").isdigit() and int(args.get("number")) > 0 and int(args.get("number")) < 21:
                number = int(args.get("number"))
            else:
                return {"error": "Number must be an integer between 1 and 20."}, 400

        else:
            number = 5

        return list(reversed(app_history))[:number], 200

    if request.method == "DELETE":
        app_history.clear()
        return {"status": "History cleared"}, 200


@app.route("/current_age", methods=["GET"])
def current_age():

    add_to_history(request)

    args = request.args.to_dict()

    if args.get("date"):

        try:
            date_str = args.get("date")

            day = convert_to_datetime(
                f"{date_str[8:]}.{date_str[5:7]}.{date_str[:4]}")

            age = get_current_age(day)

        except:
            return {"error": "Value for data parameter is invalid."}, 400

        return {"current_age": age}, 200

    else:
        return {"error": "Date parameter is required."}, 400


if __name__ == "__main__":
    app.run(port=8080, debug=True)
