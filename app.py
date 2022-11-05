from evaluation import calculator
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate():
    expression = request.form.get("exp")
    result = calculator(expression)
    return render_template('index.html', result=str(result))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)