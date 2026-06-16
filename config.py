import os

from dotenv import load_dotenv

load_dotenv()


def _as_bool(value, default=False):
    if value is None:
        return default
    return value.strip().lower() in ('1', 'true', 'yes', 'on')


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = _as_bool(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))

SECRET_KEY = os.environ.get('SECRET_KEY')

# Email Configuration (Brevo SMTP settings)
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_USE_TLS = _as_bool(os.environ.get('MAIL_USE_TLS'), True)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = (
    os.environ.get('MAIL_DEFAULT_SENDER_NAME'),
    os.environ.get('MAIL_DEFAULT_SENDER_EMAIL'),
)
