from flask import Flask , request
from rich import Console
App = Flask(__name__)

console = Console()

@App.route('/' , methods=['POST' , 'GET'])
def form():
    ...
        
if __name__ == "__main__":
    App.run(debug=True)