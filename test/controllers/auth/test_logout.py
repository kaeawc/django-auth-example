# -*- coding: utf-8 -*
import unittest
from client import Client
from client.account import Account


class LogoutSpec(unittest.TestCase):

    def test_success(self):
        """
        After logging in with valid credentials, user should be able to logout.
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            Account.login(email=email, password=password, session=client.session)
            response = Account.logout(session=client.session)

            assert response is not None
            assert response.ok is True, response

    def test_user_does_not_exist(self):
        """
        After a user's account is deleted the cookie value should be invalid.

        Currently the test can't be written because we don't yet persist accounts.
        """

        with Client() as client:

            response = Account.logout(session=client.session)

            assert response is not None
            assert response.ok is False, response
            assert response.reason.startswith(u"You must be logged in"), response.reason

    def test_not_logged_in(self):
        """
        A user who is not currently logged in should be denied
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            response = Account.logout(session=client.session)

            assert response is not None
            assert response.ok is False, response
            assert response.reason.startswith(u"You must be logged in"), response.reason
