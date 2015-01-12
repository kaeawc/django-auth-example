# -*- coding: utf-8 -*
from test.account import Account
from test.account import AccountTestCase


class GetUserPreferencesSpec(AccountTestCase):

    def test_success(self):
        """
        A user should be able to get preferences with valid credentials
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        response = self.login(email=email, password=password)

        # Check that login worked ok
        assert response.ok is True, response

        # Use the logged in session to get user preferences
        response = self.http_get(u"/preferences")

        assert response.ok is True, response


class EditUserPreferencesSpec(AccountTestCase):

    def test_success_without_changing(self):
        """
        A user should be able to edit preferences with valid credentials
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        response = self.login(email=email, password=password)

        # Check that login worked ok
        assert response.ok is True, response

        # Use the logged in session to get user preferences
        response = self.http_post(u"/preferences")

        assert response.ok is True, response