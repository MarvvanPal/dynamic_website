from flask import Flask, request
from flask import render_template

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")

# Enable to using images in the directory /static/images
app.add_url_rule('/images/<path:filename>', endpoint='images')

# Enable to using documents in the directory /static/documents
app.add_url_rule('/documents/<path:filename>', endpoint='documents')


@app.route('/')
def index():
    return render_template('index.html', page_title="Português Acústico - Home")


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', page_title="Português Acústico - About us")


@app.route('/series')
def series():
    return render_template('series.html', page_title="Português Acústico - Series")

@app.route('/solo_activities')
def solo_activities():
    return render_template('solo_activities.html', page_title="Português Acústico - Solo-Activities")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        tac = request.form.get('tac')
        if tac == "on":
            tac = "yes"
        else:
            tac = "no"
        return render_template('contact_form_sent.html', page_title="Português Acústico - Contact", name=name, email=email, subject=subject, message=message, tac=tac)

    # otherwise handle the GET request
    return render_template('contact_form_receive.html', page_title="Português Acústico - Contact")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
