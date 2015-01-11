# -*- coding: utf-8 -*
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class AuthManager(object):

    @classmethod
    def create_user(cls, email, password):

        user = User.objects.create_user(username=email, email=email, password=password)

        try:
            user.save()
        except IntegrityError:
            return {u"ok": False, u"reason": u"A user already exists with the given email address."}
        except Exception as ex:
            return {u"ok": False, u"reason": ex.message}
        else:
            return {u"ok": True, u"user": {u"id": user.id}}
