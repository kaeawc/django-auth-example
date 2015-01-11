# -*- coding: utf-8 -*
from django.views.decorators.http import require_GET
from app.controllers.decorator import jsonify


@require_GET
@jsonify
def landing(_):
    return {'ok': True, 'status': 200}


@require_GET
@jsonify
def authors(_):
    return {'ok': True, 'status': 200}
