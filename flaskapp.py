from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from commons import urls
from services.shortend_url_handler import ShortendUrl, RedirectUrl

app = Flask(__name__)
CORS(app)

api = Api(app)


#Add all routes here
api.add_resource(ShortendUrl, urls.CREATE_SHORTEND_URL_PATH)
api.add_resource(RedirectUrl, urls.GET_URL_PATH)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)