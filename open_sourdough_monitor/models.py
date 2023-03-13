import datetime

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import sqlalchemy_utils

from open_sourdough_monitor import settings

db_settings = settings.OPEN_SOURDOUGH_DB
engine = sqlalchemy.create_engine(
    f"""postgresql://{db_settings["user"]}:{db_settings["password"]}@{db_settings["host"]}:{db_settings["port"]}/{db_settings["db_name"]}"""
)
_SessionFactory = sqlalchemy.orm.sessionmaker(bind=engine)

Base = sqlalchemy.ext.declarative.declarative_base()

# Create database if it doesn't exist
if not sqlalchemy_utils.database_exists(engine.url):
    sqlalchemy_utils.create_database(engine.url)


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()


class SourDoughImages(Base):
    __tablename__ = "images"

    name = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    time_of_image = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    session = sqlalchemy.Column(sqlalchemy.Integer)

    def __init__(self, name: str, time_of_image: datetime.datetime, session: int):
        self.name = name
        self.time_of_image = time_of_image
        self.session = session


class SourDoughMonitor(Base):
    __tablename__ = "monitor"

    percent_raise = sqlalchemy.Column(sqlalchemy.Float)
    name = sqlalchemy.Column(
        sqlalchemy.String, sqlalchemy.ForeignKey("images.name"), primary_key=True
    )
    time_delta = sqlalchemy.Column(sqlalchemy.Time)

    def __init__(self, name: str, time_of_image: datetime.datetime, session: int):
        self.name = name
        self.time_of_image = time_of_image
        self.session = session


def get_latest_id():
    with session_factory() as session:
        latest_id = session.query(sqlalchemy.func.max(SourDoughImages.session)).all()
        session.close()
    return latest_id[0][0]


if not sqlalchemy.inspect(engine).has_table(SourDoughImages.__tablename__):
    SourDoughImages.__table__.create(engine)
if not sqlalchemy.inspect(engine).has_table(SourDoughMonitor.__tablename__):
    SourDoughMonitor.__table__.create(engine)
