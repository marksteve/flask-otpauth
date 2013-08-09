from setuptools import setup


if __name__ == '__main__':
    setup(
        name='Flask-OtpAuth',
        version='0.0.1',
        description='One Time Password Authentication for Flask',
        long_description=open('README.rst').read(),
        author='Mark Steve Samson',
        author_email='hello@marksteve.com',
        install_requires=[
            'Flask>=0.10',
            'otpauth',
            'qrcode',
        ],
        py_modules=['flask_otpauth'],
        url='https://github.com/marksteve/flask-otpauth',
        license='MIT',
        zip_safe=False,
    )
