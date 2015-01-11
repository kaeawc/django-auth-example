# -*- coding: utf-8 -*
from app.controllers.decorator import jsonify, logged_in


@jsonify
@logged_in
def preferences(_):
    return {u'ok': True, u'status': 200}


@jsonify
@logged_in
def profile(_):
    return {u'ok': True, u'status': 200}
