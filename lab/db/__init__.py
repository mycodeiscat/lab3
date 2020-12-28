from flask_sqlalchemy import SQLAlchemy











db: SQLAlchemy = SQLAlchemy()




# load all model classes now
import lab.model  # noqa: F811
