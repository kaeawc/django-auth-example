# -*- coding: utf-8 -*
import unittest
from client import Client
from client.account import Account


class GetUserPreferencesSpec(unittest.TestCase):

    def test_success(self):
        """
        A user should be able to get preferences with valid credentials
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            response = Account.login(email=email, password=password, session=client.session)

            # Check that login worked ok
            assert response.ok is True, response

            # Use the logged in session to get user preferences
            response = Client.http_get(u"preferences", session=client.session)

            assert response.ok is True, response


class EditUserPreferencesSpec(unittest.TestCase):

    def test_success_without_changing(self):
        """
        A user should be able to edit preferences with valid credentials
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            response = Account.login(email=email, password=password, session=client.session)

            # Check that login worked ok
            assert response.ok is True, response

            # Use the logged in session to get user preferences
            response = Client.http_post(u"preferences", session=client.session)

            assert response.ok is True, response