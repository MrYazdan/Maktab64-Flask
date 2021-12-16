from flask import Flask
from views import index, about, say_hello, sum_func, power_func, redirect_func

# Configure flask app name
app = Flask(__name__)

# Configure app route
app.add_url_rule('/', 'index', index)
app.add_url_rule('/about', 'about', about)
app.add_url_rule('/hello/<name>', 'hello', say_hello)
app.add_url_rule('/sum/', 'sum', sum_func, defaults={'number1': 10, 'number2': 12})
app.add_url_rule('/sum/<int:number1>+<int:number2>', 'sum', sum_func)
app.add_url_rule('/power/<int:number1>/', 'power', power_func, defaults={'number2': 2})
app.add_url_rule('/power/<int:number1>/<int:number2>', 'power', power_func)
app.add_url_rule('/r/<path:link>', 'redirecter', redirect_func)

if __name__ == "__main__":
    app.run()
