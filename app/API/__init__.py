try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    from flask_marshmallow import Marshmallow

    from .views import CTDDataView

except Exception as e:
    print("__init Modules are Missing {}".format(e))

app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful


app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="CTD Data query Project",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/",  # URI to access UI of API Doc
    }
)
docs = FlaskApiSpec(app)