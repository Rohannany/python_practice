import logging
from flask import Flask
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

#customize flask logging

#logging.basicConfig(format = "%(levelname)s:%(name)s:%(message)s")

# to access the route logger 
logger = logging.getLogger
# to configure the route logger, we need to create two handlers: config base handler and file based handler.
#add console handler to the root handler
consoleHandler = logging.StreamHandler() # sends logs to the console
logger.addHandler(consoleHandler)
#add file handler to the root handler 
fileHandler = RotatingFileHandler("logs.log", )


#configure Flask logging 
# #1 set the logging level
# app.logger.setLevel(logging.INFO)
# #2 log to a file 
# handler = logging.FileHandler("app.log") #order [DEBUG, INFO, WARNING, ERROR, CRITICAL]
# #3 add the file as handler
# app.logger.addHandler(handler)

@app.route("/")
def index():

    app.logger.info("This is an INFO message")
    # app.logger.debug("This is a DEBUG message")
    # app.logger.warning("This is a WARNING message")
    # app.logger.error("This is an ERROR message")
    # app.logger.critical("This is a CRITICAL message")
    return 'Hello, World!'

# to perform errorhandler

# @app.errorhandler(500)
# def server_error(error):
#     app.logger.exception("An exception occured during a request.")
#     return 'Internal sever error', 500

# run the flask application 
if __name__ == "__main__":
    app.run(debug = True)

