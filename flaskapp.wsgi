import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/ubuntu/Flask-running-app/")

from FlaskApp import app as application
application.secret_key = 'ITSASECRET'
