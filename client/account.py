# -*- coding: utf-8 -*
import uuid
import random
import string
from client import Client


class Account(Client):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    @classmethod
    def signup(cls, email=None, password=None, password_confirmation=None, session=None):

        data = {}

        if email is not None:
            data[u"email"] = email

        if password is not None:
            data[u"password"] = password

        if password_confirmation is not None:
            data[u"password_confirmation"] = password_confirmation

        response = cls.http_post(u"signup", data, session=session)

        return Account(email=email, password=password), response

    @classmethod
    def login(cls, email=None, password=None, session=None):

        data = {}

        if email is not None:
            data[u"email"] = email

        if password is not None:
            data[u"password"] = password

        return cls.http_post(u"login", data, session=session)

    @classmethod
    def logout(cls, email=None, password=None, session=None):

        data = {}

        if email is not None:
            data[u"email"] = email

        if password is not None:
            data[u"password"] = password

        return cls.http_post(u"logout", data, session=session)

    @staticmethod
    def create_email():
        return u"some.one+%s@example.com" % uuid.uuid4().hex.__str__()

    @staticmethod
    def create_password(length=20):
        return u"".join([random.choice(string.digits) for _ in xrange(length)])