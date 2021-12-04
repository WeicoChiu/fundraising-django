"""Gunicorn *development* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "fundrasing.wsgi:application"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = "0.0.0.0:8000"
# decide worker for handling request, asyn mode to boost server
workers_class = "gthread"
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/prod.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/prod.pid"
# Daemonize the Gunicorn process (detach & enter background)
# daemon = True
