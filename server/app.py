from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print to console
    return param

# Count route
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param))
    return numbers + '\n'  

# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h1>Error: Division by zero!</h1>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Error: Invalid operation!</h1>'
    
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
