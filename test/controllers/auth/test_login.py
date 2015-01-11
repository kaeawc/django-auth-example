# -*- coding: utf-8 -*
import unittest
from client import Client
from client.account import Account


class LoginSpec(unittest.TestCase):

    def test_success(self):
        """
        A user should be able to login with valid credentials.
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            response = Account.login(email=email, password=password, session=client.session)

            assert response is not None
            assert response.ok is True, response

    def test_user_does_not_exist(self):
        """
        If a user's account was deleted those credentials should no longer be valid.
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            response = Account.login(email=email, password=password, session=client.session)

            assert response is not None
            assert response.ok is False, response
            assert response.reason.startswith(u"Invalid credentials"), response

    def test_missing_fields(self):
        """
        If any or all fields are missing from login submission the user should be denied.
        """

        response = Account.login()

        assert response is not None
        assert response.ok is False, response
        assert response.reason.startswith(u"Missing fields"), u"Response is %s" % response
