from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/colour-codes')
def get_colour_codes():
   colours = [1111,2222,3333,4444]
   return str(colours)

@app.route('/ranjit')
def noob():
   return 'I love you'

# This is for debugging purposes.
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
