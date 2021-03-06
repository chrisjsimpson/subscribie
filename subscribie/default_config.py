from pathlib import Path
class DefaultConfig(object):
    path = Path()
    ENV = "development"
    SECRET_KEY = "random string. e.g. echo -e 'from os import urandom\\nprint urandom(25)' | python"
    DB_FULL_PATH = "./data.db"
    JAMLA_PATH = "./jamla.yaml"
    TEMPLATE_BASE_DIR = str(path.cwd().joinpath('themes'))
    TEMPLATE_FOLDER = "./themes/"
    STATIC_FOLDER = "./static/"
    UPLOADED_IMAGES_DEST = "./static/photos/"
    SUCCESS_REDIRECT_URL = "https://127.0.0.1:5000/complete_mandate"
    THANKYOU_URL = "https://127.0.0.1:5000/thankyou"
    GOCARDLESS_TOKEN = "sandbox_abc123"
    PENGUIN_URL = "http://127.0.0.1:8088"
    # Flask Mail @see https://pythonhosted.org/Flask-Mail/ for all options
    MAIL_SERVER = "127.0.0.1"
    MAIL_PORT = 25
    MAIL_DEFAULT_SENDER = "foo@example.com"
    MAIL_USERNAME = "username"
    MAIL_PASSWORD = "secret"
    MAIL_USE_TLS = "True"
