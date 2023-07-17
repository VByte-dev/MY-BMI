from flask import Flask, render_template, request

app = Flask(__name__)

#---BMI Calculate---#
def bmiC(a, b):
    r = a / (b**2)
    return r

v = 0
value = ''
@app.route('/', methods=['POST', 'GET'])
def homePage():
    global v, value  # Declare the variables as global
    
    if request.method == 'POST':
        h = request.form.get('height')
        w = request.form.get('weight')
        
        try:
            h = float(h)
            w = float(w)
            v = bmiC(w, h)
            value = f'Your BMI is {v:.2f}'
            print(value)
        except ValueError:
            value = 'Oops, Something went Wrong!'
    
    return render_template('homePage.html', v=value)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
