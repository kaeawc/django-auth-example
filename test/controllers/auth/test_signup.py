# -*- coding: utf-8 -*
from test.account import Account
from test.account import AccountTestCase


class SignupSpec(AccountTestCase):

    def test_success(self):
        """
        A user should be able to signup for the app if they have a valid email address and password.
        """

        email = Account.create_email()
        password = Account.create_password()

        account, response = self.signup(email=email, password=password, password_confirmation=password)

        assert response is not None
        assert response.ok is True, response

    def test_user_already_exists(self):
        """
        A user should not be able to signup with an email of another user.
        """

        email = Account.create_email()
        password = Account.create_password()

        # Original signup
        self.signup(email=email, password=password, password_confirmation=password)

        # Another signup using the same email
        account, response = self.signup(email=email, password=password, password_confirmation=password)

        assert response is not None
        assert response.ok is False, response
        assert response.reason.startswith(u"column username is not unique"), u"Response is %s" % response

    def test_short_password(self):
        """
        Users should not be able to signup with passwords less than 10 characters.
        """

        email = Account.create_email()
        password = Account.create_password()[:4]

        account, response = self.signup(email=email, password=password, password_confirmation=password)

        assert response is not None
        assert response.ok is False, u"Response is %s" % response
        assert response.reason.startswith(u"Password must be at least 10 characters"), u"Response is %s" % response

    def test_confirmation_password_does_not_match(self):
        """
        The confirmation password must match the original password exactly on signup.
        """

        email = Account.create_email()
        password = Account.create_password()
        another_password = Account.create_password()

        # Original signup
        account, response = self.signup(email=email, password=password, password_confirmation=another_password)

        assert response is not None
        assert response.ok is False, u"Response is %s" % response
        assert response.reason.startswith(u"Passwords don't match."), u"Response is %s" % response

    def test_missing_fields(self):
        """
        If any or all fields are missing from signup submission the user should be denied.
        """

        account, response = self.signup()

        assert response is not None
        assert response.ok is False, u"Response is %s" % response
        assert response.reason.startswith(u"Missing fields"), u"Response is %s" % response
