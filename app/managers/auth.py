# -*- coding: utf-8 -*
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class AuthManager(object):

    @classmethod
    def create_user(cls, email, password):

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
        except IntegrityError as ex:

            msg = ex.__str__().lower()

            if u"unique" in msg:
                return {u"ok": False, u"reason": u"A user already exists with the given email address."}

            raise ex
        except Exception as ex:
            raise ex
        else:
            return {u"ok": True, u"user": {u"id": user.id}}
