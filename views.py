from models import User
from utils import template_pattern
from flask import redirect, url_for, request, render_template, escape, render_template_string

base_variables = {
    "page": {
        "base_title": "Maktab - Flask",
        "lang": 'en-US',
        "title": 'Maktab 64'
    },

    "links": ["home", "about", "contact", "posts", "new_post"]
}

posts = [
    {"id": 1, "title": "Akbar",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 2, "title": "mahdi",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 3, "title": "reza",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 4, "title": "alireza",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 5, "title": "mohammad",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 6, "title": "heidar",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 7, "title": "kian",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 8, "title": "javad",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 9, "title": "shayan",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 10, "title": "mobin",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 11, "title": "Joomoong",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 12, "title": "Sohrab",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 13, "title": "Yazdan",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 14, "title": "Hosein",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 15, "title": "Amir Ali",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},
    {"id": 16, "title": "NarenJ",
     "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus cumque harum labore magni minima quia quod reprehenderit veritatis voluptatibus? Accusamus aliquam cumque eius expedita fugit hic id modi quam rerum."},

]


def index():
    data = base_variables
    data['page']['title'] = "Index page !"
    return render_template("index.html", data=data)


def post_list():
    data = base_variables
    data['page']['title'] = "Posts"
    return render_template("list_view.html", data=data, posts=posts)


def create_post():
    data = base_variables
    data['page']['title'] = "New post"

    if request.method == "GET":
        # form view !
        return render_template("create_view.html", data=data)

    elif request.method == "POST":
        # add new post : --> Flush
        post = {
            "id": len(posts) + 1,
            "title": escape(request.form.get('title')),
            "content": escape(request.form.get('content')),
        }
        posts.append(post)
        return "Post created !", 201

    return "Forbidden Request 403", 403


def post_detail(post_id: int):
    post = posts[post_id - 1]
    data = base_variables
    data['page']['title'] = post['title']
    return render_template("detail_view.html", data=data, post=post)


def about():
    data = base_variables
    data['page']['title'] = "About page !"
    return render_template("about.html", data=data)


def contact_us():
    data = base_variables
    data['page']['title'] = "Contact-us page !"
    return render_template("contact-us.html", data=data)


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
