import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

#SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")

#try:
#    PROJECT_STAGING_DATABASE = os.environ['PROJECT_STAGING_DATABASE']
#except:
#    PROJECT_STAGING_DATABASE = 'clutch_diagnostics_rapid_test_results'

#try:
#    FRAXSES_META_URI = os.environ['FRAXSES_META_URI']
#except:
#    FRAXSES_META_URI = 'mssql+pymssql://fraxses:password101!@34.73.11.207/fraxses'

#SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@35.226.140.100:3306/{0}?charset=utf8'.format(PROJECT_STAGING_DATABASE)

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fraxses:fraxses@db:5432/clutch'
#SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexb:alexb@34.74.248.83:5432/postgres'

#FRAXSES_META_URI = 'mssql+pymssql://fraxses:password101!@34.73.11.207/fraxses'

#FRAXSES_HIVE_URI = r'hive://35.192.66.5:10000/default'

SQLALCHEMY_BINDS = {
    'app':SQLALCHEMY_DATABASE_URI,
#    'fraxses': FRAXSES_META_URI,
#    'clutch': CLUTCH_PBM_URI,
#    'hive': FRAXSES_HIVE_URI
}

CSRF_ENABLED = True

APP_NAME = "Clutch"

#APP_ICON = "https://storage.cloud.google.com/superset-static/clutch_logo.png?authuser=1"

AUTH_TYPE = AUTH_DB

UPLOAD_FOLDER = basedir + "/app/static/uploads/"

IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

IMG_UPLOAD_URL = "/static/uploads/"

FILE_ALLOWED_EXTENSIONS = ("txt", "pdf", "jpeg", "jpg", "gif", "png", "img")
