from sqlalchemy import create_engine
import json

class DbConnection:
    def __init__(self):
        with open("config/config.json", "r") as config_file:
            self.config = json.load(config_file)

    def get_db_engine(self):
        db_conf = self.config["database"]

        connection_url = (
            f"mysql+mysqlconnector://{db_conf['user']}:"
            f"{db_conf['password']}@{db_conf['host']}/"
            f"{db_conf['database']}"
        )
        engine = create_engine(connection_url, echo=True) 
        return engine