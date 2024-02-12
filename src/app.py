from flask import Flask , render_template , url_for , request
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert' , methods=["POST"])
def form():
    if request.method == "POST":
        url = request.form['url']
        option = request.form['option']

        output = MediaConvertor.Download(url , option , debug=False)
        return render_template('index.html' , value=output)
        
    
if __name__ == "__main__":
    app.run(debug=True)