# -*- coding: utf-8 -*
import functools
from app import settings
from datetime import datetime
from django.http.response import HttpResponse, JsonResponse, REASON_PHRASES

STATUS_CODES = REASON_PHRASES.keys()


def jsonify(func):
    """
    This decorator returns a HttpResponse in JSON format with the object
    returned from f(*args, **kwargs).
    If the object returned by f has a to_dict
    method it will be called before serialize it to JSON
    """

    @functools.wraps(func)
    def wrap(*args, **kwarg):

        request = args[0]
        start_time = datetime.utcnow()
        try:
            response = func(*args, **kwarg)
        except Exception as ex:
            end_time = datetime.utcnow()
            duration = int((end_time - start_time).total_seconds() * 1000)
            return write_response(request, exception=ex, reason=u"Failed to process request", duration=duration, start_time=start_time, end_time=end_time)
        else:
            end_time = datetime.utcnow()
            duration = int((end_time - start_time).total_seconds() * 1000)

        if isinstance(response, HttpResponse):
            return write_response(response)

        if not isinstance(response, dict) and hasattr(response, u'to_dict'):
            response = response.to_dict()

        try:
            if isinstance(response, dict):

                # If a status code was passed, attempt to use it
                status = response.get(u"status")
                if not isinstance(status, int) or status not in STATUS_CODES:
                    status = None

                return write_response(request, response=response, status=status, duration=duration, start_time=start_time, end_time=end_time)

            if isinstance(response, list):
                return write_response(request, response=response, status=200, duration=duration, start_time=start_time, end_time=end_time)
        except Exception as ex:
            return write_response(request, exception=ex, reason=u"Failed to serialized response", duration=duration, start_time=start_time, end_time=end_time)
        else:
            return write_response(response)

    return wrap


def write_response(request, response=None, exception=None, reason=None, status=None, duration=None, start_time=None, end_time=None):

    if reason is None and exception is not None:
        reason = exception.__getattribute__(u"message")

    if response is None:
        response = {
            u"ok": False,
            u"reason": reason,
        }

    if settings.DEBUG:
        response[u"ajax"] = request.is_ajax()
        response[u"secure"] = request.is_secure()
        response[u"encoding"] = request.encoding
        response[u"method"] = request.method
        response[u"path"] = request.path
        response[u"path_info"] = request.path_info
        response[u"scheme"] = request.scheme
        response[u"user"] = request.user.__str__()
        response[u"controller"] = request.resolver_match.url_name
        response[u"duration"] = duration
        response[u"start_time"] = start_time
        response[u"end_time"] = end_time
        response[u"session"] = {
            u"key": request.session.session_key,
            u"modified": request.session.modified,
        }

    return JsonResponse(response, status=status, reason=reason)


def logged_out(func):
    """
    Controllers decorated with @logged_out deny users who have the 'user_id' cookie.
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrap(*args, **kwargs):

        request = args[0]

        if request.user and request.user.is_authenticated():
            controller = request.resolver_match.url_name
            return {u"ok": False, u"status": 401, u"reason": u"You must be logged out to access %s." % controller}

        response = func(*args, **kwargs)

        return response

    return wrap


def logged_in(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):

        request = args[0]

        if request.user and not request.user.is_authenticated():
            controller = request.resolver_match.url_name
            return {u"ok": False, u"status": 401, u"reason": u"You must be logged in to access %s." % controller}

        response = func(*args, **kwargs)

        return response

    return wrap


def facebook(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):

        response = func(*args, **kwargs)

        return response

    return wrap
