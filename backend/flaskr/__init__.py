#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort, jsonify
from sqlalchemy import distinct
from logging import Formatter, FileHandler
import logging
import sys
from models import *


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def index():
  return jsonify({
    'message': "Hello, App"
  })


#----------------------------------------------------------------------------#
# Errors
#----------------------------------------------------------------------------#

@app.errorhandler(400)
def bad_request(error):
    return (jsonify({
            "success": False,
            "error": 400,
            "message": "bad request",
            }), 400)

@app.errorhandler(404)
def not_found(error):
    return (jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found",
            }), 404)

@app.errorhandler(405)
def not_allowed(error):
    return (jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed",
            }), 405)

@app.errorhandler(422)
def unprocessable(error):
    return (jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable",
            }), 422)

@app.errorhandler(500)
def unprocessable(error):
    return (jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error",
            }), 500)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
