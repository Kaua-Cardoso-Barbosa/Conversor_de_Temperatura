from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/temperatura', methods=['POST'])
def temperatura():
    try:
        celsius = float(request.form['celsius'])
        kelvin = celsius + 273
        fahrenheit = celsius * (9 / 5) + 32
        print(fahrenheit, kelvin)
        return render_template('index.html', kelvin=kelvin, fahrenheit=fahrenheit )
    except Exception as e:
        total = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html', kelvin=kelvin, fahrenheit=fahrenheit )
if __name__=='__main__' :
    app.run(debug=True)