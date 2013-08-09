from flask import make_response
from otpauth import OtpAuth as _OtpAuth
from StringIO import StringIO
import qrcode


class OtpAuth(object):

    def __init__(self, app=None, *args, **kwargs):
        if app:
            self.app = app
            self.init_app(app, *args, **kwargs)

    def init_app(self, app, add_template_globals=True):
        if add_template_globals:
            app.add_template_global(self.hotp)
            app.add_template_global(self.totp)

    def _otpauth_method(self, name, secret, *args, **kwargs):
        return getattr(_OtpAuth(secret), name)(*args, **kwargs)

    def hotp(self, *args, **kwargs):
        return self._otpauth_method('hotp', *args, **kwargs)

    def totp(self, *args, **kwargs):
        return self._otpauth_method('totp', *args, **kwargs)

    def valid_hotp(self, *args, **kwargs):
        return self._otpauth_method('valid_hotp', *args, **kwargs)

    def valid_totp(self, *args, **kwargs):
        return self._otpauth_method('valid_totp', *args, **kwargs)

    def google_qrcode(self, secret, *args, **kwargs):
        auth = _OtpAuth(secret)
        qrcode_img = qrcode.make(auth.to_google(*args, **kwargs))
        f = StringIO()
        qrcode_img.save(f, 'jpeg')
        resp = make_response(f.getvalue())
        resp.headers['Content-Type'] = 'image/jpeg'
        return resp

