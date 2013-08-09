from flask import Flask, flash, redirect, request, render_template, url_for
from flask_otpauth import OtpAuth


SECRET = 'secret'


app = Flask(__name__)
auth = OtpAuth(app)


@app.route('/')
def index():
    return render_template('index.html', SECRET=SECRET)


@app.route('/check_hotp', methods=['POST'])
def check_hotp():
    flash(repr(auth.valid_hotp(SECRET, request.form['hotp'])), category='hotp')
    return redirect(url_for('index'))


@app.route('/check_totp', methods=['POST'])
def check_totp():
    flash(repr(auth.valid_totp(SECRET, request.form['totp'])), category='totp')
    return redirect(url_for('index'))


@app.route('/google_authenticator')
def google_authenticator():
    return auth.google_qrcode(SECRET, 'totp', 'Example:foo@bar.baz', 'Foo')


app.config['SECRET_KEY'] = SECRET
app.run(debug=True)
