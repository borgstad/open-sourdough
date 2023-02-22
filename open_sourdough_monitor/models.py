import sqlalchemy
import sqlalchemy_utils
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from open_sourdough_monitor import settings

db_settings = settings.OPEN_SOURDOUGH_DB["default"]
engine = sqlalchemy.create_engine(
    f"""postgresql://{db_settings["DB_NAME"]}:{db_settings["PASSWORD"]}@{db_settings["HOST"]}:{db_settings["PORT"]}/open-sour-dough"""
)
_SessionFactory = sqlalchemy.orm.sessionmaker(bind=engine)

Base = sqlalchemy.ext.declarative.declarative_base()

if not sqlalchemy_utils.database_exists(engine.url):
    sqlalchemy_utils.create_database(engine.url)


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()


class SourDoughImages(Base):
    __tablename__ = "sourdough_images"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    time_of_image = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

    def __init__(self, name, time_of_image):
        self.name = name
        self.time_of_image = time_of_image


if not sqlalchemy.inspect(engine).has_table(SourDoughImages.__tablename__):
    SourDoughImages.__table__.create(engine)
