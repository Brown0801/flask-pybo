from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Oh yeh'



app.run(port=5001, debug=True)