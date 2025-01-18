#import libraries
from flask import Flask, render_template, request
import math
import base64
from flask_frozen import Freezer


# Create flask instance
app = Flask(__name__)
freezer = Freezer(app)

# home page
@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('index.html')

# encode data
@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        data = request.form['data']
        encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return render_template('index.html', encoded_data=encoded_data)

# decode data
@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        data = request.form['data']
        decoded_data = base64.b64decode(data).decode()
    return render_template('index.html', decoded_data=decoded_data)

# about page
@app.route('/about')
def about():
    return render_template('about.html')
    
# run the app
if __name__ == '__main__':
    # app.run(debug=True)
    freezer.freeze()
