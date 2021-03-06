from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'BLOG1',
        'Trusted_Connection':'yes',
        'HOST': 'localhost\SQLEXPRESS',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}