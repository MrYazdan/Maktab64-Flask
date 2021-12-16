from models import User
from utils import template_pattern
from flask import redirect, url_for, request


def index():
    return template_pattern("Hello Maktab 64!!!")


def about():
    return template_pattern("About Page ~", "orangered")


def say_hello(name):
    from datetime import datetime as dt
    now = dt.now()
    return template_pattern(f"Say hello from Flask to {name} at {now}", "green")


def sum_func(number1, number2):
    return template_pattern(f"{number1} + {number2} = {number1 + number2}", "cyan")


def power_func(number1, number2):
    return template_pattern(f"{number1} ** {number2} = {number1 ** number2}", "purple")


def redirect_func(link):
    # return redirect(link)
    print(url_for(link))
    return redirect(url_for(link))


def printer_func(text):
    return template_pattern(f"Method : {request.method}<br>Print <b>{text}</b>",
                            "orange" if request.method == "GET" else "cyan")


def requests_func():
    return f"""<pre>
        Request : {request}
        Method : {request.method}
        Url : {request.url}
        Args : {request.args}
    </pre>"""


def users():
    if request.method == "GET":
        user_list = User.__users__
        return {k: vars(user_list[k]) for k in user_list}

    elif request.method == "POST":
        request_json = request.json
        user = User(request_json.get("name"), request_json.get('family'))
        return {"Created 201": str(user)}


def get_user(user_id):
    user_dict = User.__users__
    return vars(user_dict[user_id])
