# -*- coding: utf-8 -*
import uuid
import random
import string
from test import DjangoTestCase


class Account(object):

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    @staticmethod
    def create_email():
        return u"some.one+%s@example.com" % uuid.uuid4().hex.__str__()

    @staticmethod
    def create_password(length=20):
        return u"".join([random.choice(string.digits) for _ in range(length)])


class AccountTestCase(DjangoTestCase):

    def signup(self, email=None, password=None, password_confirmation=None):

        data = {}

        if email is not None:
            data[u"email"] = email

        if password is not None:
            data[u"password"] = password

        if password_confirmation is not None:
            data[u"password_confirmation"] = password_confirmation

        response = self.http_post(u"/signup", data)

        return Account(email=email, password=password), response

    def login(self, email=None, password=None):

        data = {}

        if email is not None:
            data[u"email"] = email

        if password is not None:
            data[u"password"] = password

        return self.http_post(u"/login", data)

    def logout(self, email=None, password=None):

        data = {}

        if email is not None:
            data[u"email"] = email

        if password is not None:
            data[u"password"] = password

        return self.http_post(u"/logout", data)