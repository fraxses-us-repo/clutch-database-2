from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
from pyhive import hive
import pandas as pd
from sqlalchemy import *
from sqlalchemy.schema import *

FRAXSES_HIVE_URI = r'hive://192.168.35.172:10000/default'

def createSession(dataObject):
    engine = create_engine(FRAXSES_HIVE_URI)
    Session = sessionmaker(bind=engine)
    dataObjectEngine = Table(dataObject, MetaData(bind=engine), autoload=True)
    session = Session()
    return session, dataObjectEngine

def sqlAlchemyQuery(session, dataObjectEngine):
    #session, dataObjectEngine = createSession(dataObject)
    df = pd.DataFrame(session.query(dataObjectEngine).all())
    print(df.head(10))
    return df
