from flask import redirect, url_for


def template_pattern(text, color="red"):
    return f"<center><h1 style=\"color:{color}\">{text}</h1></center>"


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
