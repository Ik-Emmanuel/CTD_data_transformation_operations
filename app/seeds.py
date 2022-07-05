import os
import pandas as pd
from models import db, CTD
from API import app

pwd = os.path.dirname(os.path.abspath(__file__))
DB_URL = os.path.join(pwd, "CTD_DB.sqlite")
database_exists = os.path.exists(DB_URL)


def create_db():
    if not database_exists:
        print("⏳Creating database...")
        try:
            with app.app_context():
                db.create_all()
            print("✅✅ Database created")
            load_data()
        except Exception as e:
            print("❌❌An error occurred while creating database: ", e)
    else:
        print("🏁Database already exists")


def load_data():
    data = pd.read_table("CTDF.txt", delimiter=" ", on_bad_lines="skip")
    data = data.iloc[1:, :]  # remove first row
    data.columns = data.columns.str.lower()
    data["datetime"] = pd.to_datetime(data["datetime"], errors="coerce")
    data = data.dropna(subset=["datetime"])
    print("⏳⏳⏳ Loading data into data base. Please wait  ...")

    data_list = [CTD(**data) for data in data.to_dict(orient="records")]
    try:
        with app.app_context():
            db.session.add_all(data_list)
            db.session.commit()
            print("✅✅ Data load complete ✅✅")
    except Exception as e:
        print("❌❌Error occurred loading data: ", e)
