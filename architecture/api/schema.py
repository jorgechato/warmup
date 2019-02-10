from flask_restplus import fields
from flask_restplus import Model

URL_schema = Model('URL', {
    '__this': fields.Url(absolute=True),
    'original': fields.String,
    'short': fields.String,
    'id': fields.String,
})

Original_schema = Model('Original', {
    'url': fields.String,
})

Short_schema = Model('Short', {
    'shorted': fields.String,
})