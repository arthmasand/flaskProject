from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
