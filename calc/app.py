# Put your app in here.
from flask import Flask, request
from operations import add
from operations import sub
from operations import mult
from operations import div

app = Flask(__name__)

@app.route('/<operation>')
def operate(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    if operation == 'add':
        result = add(a,b)
    elif operation == 'sub':
        result = sub(a,b)
    elif operation == 'mult':
        result = mult(a,b)
    elif operation == 'div':
        result = div(a,b)
    else:
        result = 'Unknown arithmetic operation'
    return str(result)

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    operations = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }

    result = operations[operation](a,b)

    return str(result)
