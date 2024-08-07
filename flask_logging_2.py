from flask import Flask
import logging


app = Flask(__name__)

#DEBUG, INFO, WARNING, ERROR, CRITICAL

log_level = logging.DEBUG
log_file = 'app.log'
log_file_mode = 'a' #append
log_format = '%(asctime)s - %(levelname)s - %(message)s'
 
if __name__ == "__main__":
    app.run(debug=True)