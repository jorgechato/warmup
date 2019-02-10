from flask_restplus import Resource
from flask_restplus import Namespace
from flask_restplus import abort
from flask import request

from utils.errors import BadRequest
from api.schema import URL_schema
from api.schema import Original_schema
from api.schema import Short_schema
from api.service import UrlDAO


ns = Namespace('', description='Simple URL shorted MS')
ns.add_model('URL', URL_schema)
ns.add_model('Short', Short_schema)
ns.add_model('Original', Original_schema)


DAO = UrlDAO()

@ns.route("/shorten")
class Short(Resource):
    @ns.doc(body=Original_schema)
    @ns.expect(Original_schema)
    @ns.marshal_with(URL_schema, skip_none=True, code=200)
    def put(self, **kwargs):
        url = DAO.put(ns.payload, request.host_url)
        if url == None:
            return abort(400, BadRequest)
        return url


@ns.route("/original")
class Original(Resource):
    @ns.doc(body=Short_schema)
    @ns.expect(Short_schema)
    @ns.marshal_with(URL_schema, skip_none=True, code=200)
    def put(self, **kwargs):
        url = DAO.get_url_by_short(ns.payload, request.host_url)
        if url == None:
            return abort(404)
        return url