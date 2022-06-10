from flask import Flask, request
# create flask app
from compiler import RPN
app = Flask(__name__)


@app.route('/compile')
def foo():
    code = request.args.get('code')
    print(code)
    r = RPN(code, {})
    return {'assembly': r.compileToAssembly({'+': 'ADD', '-': 'SUB', '*': 'MULT',
                                             '/': 'DIV', '^': 'EXP', '%': 'MOD', '=': 'STR'}, 0)}


if __name__ == '__main__':
    app.run(debug=True)
