from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running on Vercel!"

def handler(request, context):
    return app(request.environ, lambda status, headers: None)