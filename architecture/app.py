"""
This is a simple microservice in which you can create
and store a short url.

This MS allows you to get the original URL.
In that case we will need to store the Original URL
as key and the shorten as value.

In this case I'm going to build a service to store the data
into the simpleast 'database', (a global variable).
Keep in mind that in future iterations updating the service
will be enough to interact with a proper DB if needed.

This is one of the limitations aside from the fact that each
execution has to store all the requests in memory.
In that case the memory space will be filled in some point.

Some edge cases will be to be a well formated and valid URL,
In that case we can use [urllib.parse] library.

In future iterations we can use the following schema:
- URL insert to DB
- DB record an ID
- encode the ID to get the unique shorted URL
- decode it and store it
- send the short url to the user

To make it simpler let's use a hashmap to store the URLs.
With the following schema:
{
    id (int): {
        URL: url (String),
        Shorted: short_url (String),
    } (Object)
}
"""
from flask import Flask
from flask_restplus import Api

from api.controller import ns


app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='Short URL service',
    description='The service will allow a user to convert an URL to a shortened URL',
)

api.add_namespace(ns)

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000)
