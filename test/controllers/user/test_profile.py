# -*- coding: utf-8 -*
from test.account import Account
from test.account import AccountTestCase


class GetUserProfileSpec(AccountTestCase):

    def test_success(self):
        """
        A user should be able to get a profile with valid credentials
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        response = self.login(email=email, password=password)

        # Check that login worked ok
        assert response.ok is True, response

        # Use the logged in session to get user profile
        response = self.http_get(u"/profile")

        assert response.ok is True, response


class EditUserProfileSpec(AccountTestCase):

    def test_success_without_changing(self):
        """
        A user should be able to edit their profile with valid credentials
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        response = self.login(email=email, password=password)

        # Check that login worked ok
        assert response.ok is True, response

        # Use the logged in session to get user profile
        response = self.http_post(u"/profile")

        assert response.ok is True, response