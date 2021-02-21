from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from settings import Config
from encoder import CustomJSONEncoder

from controllers.product_controller import PRODUCT_BLUEPRINT

APP = Flask(__name__)
CORS(APP)

connect(db=Config.DATABASE_NAME,
        authentication_source=Config.DATABASE_AUTH_SOURCE,
        host=Config.DATABASE_HOST,
        port=Config.DATABASE_PORT,
        username=Config.DATABASE_USERNAME,
        password=Config.DATABASE_PASSWORD,
        ssl=Config.DATABASE_SSL,
        retryWrites=Config.RETRY_WRITES)

APP.json_encoder = CustomJSONEncoder

APP.register_blueprint(PRODUCT_BLUEPRINT, url_prefix='/api/product')


@APP.route('/', defaults={'path': ''})
@APP.route('/<path:path>')
def index(path):
    return APP.send_static_file('index.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port='5000', debug=True)
