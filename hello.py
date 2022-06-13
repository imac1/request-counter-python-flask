from crypt import methods
from distutils.log import debug
from itertools import count
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
methods_counts = {
    "GET": 0,
    "POST": 0,
    "UPDATE": 0,
    "DELETE": 0
}

@app.route('/')
def main_page(): 
    global methods_counts
    return render_template('index.html', methods_counts=methods_counts)


@app.route('/statistics')
def statistics_page():
    global methods_counts
    return render_template('statistics.html', methods_counts=methods_counts)

@app.route('/request-counter', methods=['POST'])
def post_counter():
    global methods_counts
    methods_counts["POST"] += 1
    return redirect('/')


@app.route('/request-counter', methods=['GET'])
def get_counter():
    global methods_counts
    methods_counts["GET"] += 1
    return redirect('/')

@app.route('/request-counter', methods=['UPDATE'])
def put_counter():
    global methods_counts
    methods_counts["UPDATE"] += 1
    return redirect('/')

@app.route('/request-counter', methods=['DELETE'])
def delete_counter():
    global methods_counts
    methods_counts["DELETE"] += 1
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True, port=5000)
