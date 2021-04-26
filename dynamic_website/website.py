from flask import Flask
from flask import render_template

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

# Enable to using images in the directory /static/images
app.add_url_rule('/images/<path:filename>', endpoint='images')


@app.route('/')
def index():
    return render_template('index.html', page_title="Português Acústico")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
