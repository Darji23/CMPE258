from flask import Flask, render_template, request, jsonify
import math
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    try:
        # Sanitize: only allow safe characters
        if not re.match(r'^[\d\s\+\-\*\/\.\(\)\%\^]+$', expression):
            return jsonify({'result': 'Error', 'error': True})
        
        # Replace ^ with ** for exponentiation
        expression = expression.replace('^', '**')
        # Replace % with /100 for percentage
        expression = re.sub(r'(\d+(?:\.\d+)?)\s*%', r'(\1/100)', expression)
        
        result = eval(expression, {"__builtins__": {}}, {
            'sqrt': math.sqrt, 'pi': math.pi, 'e': math.e,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'log': math.log10, 'ln': math.log, 'abs': abs
        })
        
        # Format result
        if isinstance(result, float):
            if result == int(result) and abs(result) < 1e15:
                result = int(result)
            else:
                result = round(result, 10)
                result = f"{result:.10g}"
        
        return jsonify({'result': str(result), 'error': False})
    
    except ZeroDivisionError:
        return jsonify({'result': '∞', 'error': True})
    except Exception as e:
        return jsonify({'result': 'Error', 'error': True})

if __name__ == '__main__':
    app.run(debug=True, port=5050)