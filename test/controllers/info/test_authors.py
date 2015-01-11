# -*- coding: utf-8 -*
import unittest
from client import Client


class AuthorsSpec(unittest.TestCase):

    def test_success(self):
        """
        Anyone should be able to view the authors page
        """
        response = Client.http_get(u"authors")

        assert response is not None
        assert response.ok is True, response
        assert response.controller == u"authors", response
        assert response.duration < 10