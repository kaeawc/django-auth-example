# -*- coding: utf-8 -*
from test.account import Account
from test.account import AccountTestCase


class LoginSpec(AccountTestCase):

    def test_success(self):
        """
        A user should be able to login with valid credentials.
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        response = self.login(email=email, password=password)

        assert response is not None
        assert response.ok is True, response

    def test_user_does_not_exist(self):
        """
        If a user's account was deleted those credentials should no longer be valid.
        """

        email = Account.create_email()
        password = Account.create_password()
        response = self.login(email=email, password=password)

        assert response is not None
        assert response.ok is False, response
        assert response.reason.startswith(u"Invalid credentials"), response

    def test_missing_fields(self):
        """
        If any or all fields are missing from login submission the user should be denied.
        """

        response = self.login()

        assert response is not None
        assert response.ok is False, response
        assert response.reason.startswith(u"Missing fields"), u"Response is %s" % response
