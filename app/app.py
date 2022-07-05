import os, sys

pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pwd)

try:
    from API import app, api, docs, CTDDataView
    from flask_marshmallow import Marshmallow
    from flask import redirect
    from seeds import create_db, load_data
    from models import db, CTD

except Exception as e:
    print("app.py Modules are Missing : {} ".format(e))

api.add_resource(CTDDataView, "/ctd_data")
docs.register(CTDDataView)

DB_URL = os.path.join(pwd, "CTD_DB.sqlite")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return redirect("/swagger-ui")


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
