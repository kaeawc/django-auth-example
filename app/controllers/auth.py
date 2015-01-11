# -*- coding: utf-8 -*
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from app.controllers.decorator import jsonify, logged_out, logged_in, facebook
from app.managers.auth import AuthManager


@require_POST
@jsonify
@logged_out
def login(request):

    email = request.POST.get(u"email", u"")
    password = request.POST.get(u"password", u"")

    if len(password) == 0 or len(email) == 0:
        return {u"ok": False, u"status": 400, u"reason": u"Missing fields."}

    user = authenticate(username=email, password=password)

    if user and user.is_active:
        user_login(request, user)
        return {u"ok": True, u"status": 202}

    return {u"ok": False, u"status": 401, u"reason": u"Invalid credentials."}


@require_POST
@jsonify
@logged_out
def signup(request):

    email = request.POST.get(u"email", u"")
    password = request.POST.get(u"password", u"")
    password_confirmation = request.POST.get(u"password_confirmation", u"")

    if len(password) == 0 or len(password_confirmation) == 0 or len(email) == 0:
        return {u"ok": False, u"status": 400, u"reason": u"Missing fields."}

    if len(password) < 10:
        return {u"ok": False, u"status": 400, u"reason": u"Password must be at least 10 characters."}

    if password != password_confirmation:
        return {u"ok": False, u"status": 400, u"reason": u"Passwords don't match."}

    if not email or len(email) == 0 or u"@" not in email or email.startswith(u"@") or email.endswith(u"@"):
        return {u"ok": False, u"status": 400, u"reason": u"Not a valid email address"}

    try:
        result = AuthManager.create_user(email=email, password=password)
    except Exception as ex:
        return {u"ok": False, u"status": 500, u"reason": ex.message}

    if result[u"ok"] is True:
        result[u"status"] = 201
    else:
        result[u"status"] = 500

    return result


@require_POST
@jsonify
@logged_in
def logout(request):
    user_logout(request)
    return {u"ok": True, u"status": 202}


@require_POST
@jsonify
@facebook
def deauth(_):
    return {u"ok": True, u"status": 202}


def create_cookie():
    return u"asdfasdfasdf"