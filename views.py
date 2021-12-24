from models import User
from utils import template_pattern
from flask import redirect, url_for, request, render_template, escape, render_template_string

base_variables = {
    "page": {
        "base_title": "Maktab - Flask",
        "lang": 'en-US',
        "title": 'Maktab 64'
    },

    "links": ["index", "about", "hello", "request_info"]
}


def index():
    data = base_variables
    data['page']['title'] = "Index page !"
    return render_template("index.html", data=data)


def about():
    data = base_variables
    data['page']['title'] = "About page !"
    return render_template("about.html", data=data)


def say_hello():
    from datetime import datetime as dt
    now = dt.now()
    # return render_template("hi.html", datetime=now, name=name)
    import random

    data = base_variables
    data['page']['title'] = "Hello page !"
    data["datetime"] = now
    data["name"] = request.args.get('name', 'Akbar')
    data["number"] = random.randint(-9999, -1)

    return render_template("hi.html", data=data)


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
        # return {k: vars(user_list[k]) for k in user_list}
        return render_template("users.html", users=user_list.values() if user_list else False)

    elif request.method == "POST":
        request_json = request.json
        user = User(request_json.get("name"), request_json.get('family'))
        return {"Created !": str(user)}, 201


def get_user(user_id):
    user_dict = User.__users__
    return vars(user_dict[user_id])
