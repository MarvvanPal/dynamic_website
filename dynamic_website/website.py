from flask import Flask
from flask import render_template

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

# Enable to using images in the directory /static/images
app.add_url_rule('/images/<path:filename>', endpoint='images')

# Enable to using documents in the directory /static/documents
app.add_url_rule('/images/<path:filename>', endpoint='documents')


@app.route('/')
def index():
    return render_template('index.html', page_title="Português Acústico - Home")


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', page_title="Português Acústico - About us")


@app.route('/series')
def series():
    return render_template('series.html', page_title="Português Acústico - Series")


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title="Português Acústico - Contact")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
