

from sqlalchemy.ext.automap import automap_base
import time
import sys
from sqlalchemy import text
from axsx.manager import Rocket
from axsx.model import Config
from axsx.model import EngineConfig

# try:
#     raise ConnectionAbortedError('asdsadfgdg')
# except ConnectionAbortedError as e:
#     print(f"==>> dir(e): {dir(e)}")
#     print(f"==>> dir(e): {e.errno}")
#     print(f"==>> dir(e): {e.__repr__}")
#     print(f"==>> dir(e): {e.__str__}")
#     print(f"==>> dir(e): {e.strerror}")
#     print(f"==>> dir(e): {e.winerror}")
#     print(f"==>> dir(e): {e}")
# sys.exit(0)
db = Rocket()


my_conf = {
    'xx': Config(
        urls=[
            # 'mysql+pymysql://root:admin@localhost:3306/test_db',
            'cockroachdb://user_xice15:s1AI9xe7cZSGTsWL@crdb3.mosynx.com:26257/service_vigil',
            'mysql+pymysql://root:admin@xxxaa/mosynx_mmc_test',
        ],
        configs=EngineConfig(
            # pool_pre_ping=True
        )
    )
}

db = Rocket()
db.setup(my_conf)
enigin = db.get_engine('xx')

Base = automap_base()
# Base.prepare(autoload_with=db.get_engine('xx'))
Base.prepare(autoload_with=enigin)
service = Base.classes.service
print(f"==>> service: {service}")
# print(f"==>> Base.classes: {Base.classes}")
# print(f"==>> Base.classes: {dir(Base.classes.__dir__)}")

# c = db.create('xx', service(name='jk', url='xx22.com'))
c = db.read_line('xx', service, name='jk')
# c = db.create('xx', service(name='jk', url='xx22.com'))
# c = db.create('xx', service(name='jk', url='xx22.com'))
print(f"==>> c: {c.id}")


# while True:
#     with db.get_session('xx') as session:
#         c = session.execute(text('select 1')).all()
#         print(f"==>> c: {c}")

#     time.sleep(5)


# @db.handle_transaction(db_name='xx')
# def test_1(session=None):
#     session.add()
