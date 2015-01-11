# -*- coding: utf-8 -*
import unittest
from client import Client
from client.account import Account


class GetUserProfileSpec(unittest.TestCase):

    def test_success(self):
        """
        A user should be able to get a profile with valid credentials
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            response = Account.login(email=email, password=password, session=client.session)

            # Check that login worked ok
            assert response.ok is True, response

            # Use the logged in session to get user profile
            response = Client.http_get(u"profile", session=client.session)

            assert response.ok is True, response


class EditUserProfileSpec(unittest.TestCase):

    def test_success_without_changing(self):
        """
        A user should be able to edit their profile with valid credentials
        """

        with Client() as client:

            email = Account.create_email()
            password = Account.create_password()
            Account.signup(email=email, password=password, password_confirmation=password, session=client.session)
            response = Account.login(email=email, password=password, session=client.session)

            # Check that login worked ok
            assert response.ok is True, response

            # Use the logged in session to get user profile
            response = Client.http_post(u"profile", session=client.session)

            assert response.ok is True, response