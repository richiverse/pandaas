#! /usr/bin/env python3
"""RestY Python"""
from importlib import import_module
from os import environ
from traceback import format_exc

from flask import Flask, request, jsonify

from middleware import list_routes
from utils import rgetattr

api = Flask(__name__)


@api.errorhandler(Exception)
def exception_handler(error):
    # type: (Exception) -> Exception
    """Show uncaught exceptions.

    Args:
        error

    Raises:
        Exception
        """
    raise Exception(format_exc())


@api.route('/')
def list_api_routes():
    """List all endpoints"""
    return jsonify(list_routes(api))


@api.route('/<module>/<attrs>', methods=['POST'])
def get_python_call(module, attrs):
    json_args = request.json or {}
    kwargs = {k: v  for k, v in json_args.items() if k != '__subattrs'}
    subattrs = json_args.get('__subattrs')
    mod = import_module(module)
    result = rgetattr(mod, attrs)(**kwargs)

    if subattrs:
        for item in subattrs:
            kwd = "".join(i for i in item.keys())
            result = rgetattr(result, kwd)(item[kwd])

    return jsonify(result)

if __name__ == '__main__':
    DEBUG = False if environ['STAGE'] == 'prod' else True
    api.run(debug=DEBUG,port=6000)
