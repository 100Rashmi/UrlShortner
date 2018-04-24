import json

from flask import request, Response, redirect
from flask_restful import Resource

from commons import constants
from controllers import shortend_url_controller


class ShortendUrl(Resource):

    # create shortend url
    def post(self):
        json_body = request.get_json(force=True)
        long_url = json_body['long_url']

        short_url = shortend_url_controller.create_shortend_url(long_url)
        return Response(response = json.dumps({'short_url':short_url}), status = 201, mimetype = 'application/json')


class RedirectUrl(Resource):
    # get shortend url if it is not expired
    def get(self, shortpath):
        resp, long_url = shortend_url_controller.redirect_url(shortpath)
        if constants.Status.SUCCESS == resp:
            return redirect(long_url, 302)
        elif constants.Status.EXPIRED == resp :
            return Response(response=json.dumps({'message':resp}), status=498, mimetype='application/json')
        elif constants.Status.NOT_PRESENT == resp:
            return Response(response=json.dumps({'message':constants.Status.NOT_FOUND}), status=404, mimetype='application/json')
        else:
            return Response(response=json.dumps({'message':constants.Status.INTERNAL_SERVER_ERROR}), status=500, mimetype='application/json')







