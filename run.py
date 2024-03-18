from flask import Flask, render_template
app = Flask(__name__,
            static_folder = "frontend/dist/assets",
            template_folder = "frontend/dist")
@app.route('/', defaults={'path': ''})
@app.route('/home')
def catch_all(path):
    return render_template("index.html")