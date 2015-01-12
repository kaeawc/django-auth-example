# -*- coding: utf-8 -*
from test.account import Account
from test.account import AccountTestCase


class LogoutSpec(AccountTestCase):

    def test_success(self):
        """
        After logging in with valid credentials, user should be able to logout.
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        self.login(email=email, password=password)
        response = self.logout()

        assert response is not None
        assert response.ok is True, response

    def test_user_does_not_exist(self):
        """
        After a user's account is deleted the cookie value should be invalid.

        Currently the test can't be written because we don't yet persist accounts.
        """

        response = self.logout()

        assert response is not None
        assert response.ok is False, response
        assert response.reason.startswith(u"You must be logged in"), response.reason

    def test_not_logged_in(self):
        """
        A user who is not currently logged in should be denied
        """

        email = Account.create_email()
        password = Account.create_password()
        self.signup(email=email, password=password, password_confirmation=password)
        response = self.logout()

        assert response is not None
        assert response.ok is False, response
        assert response.reason.startswith(u"You must be logged in"), response.reason
