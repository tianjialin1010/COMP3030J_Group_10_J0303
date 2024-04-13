from backend.App import createApp
from flask import render_template

app = createApp('development')

if __name__ == "__main__":
    app.run(debug=True)

