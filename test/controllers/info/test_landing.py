# -*- coding: utf-8 -*
import unittest
from client import Client


class LandingSpec(unittest.TestCase):

    def test_success(self):
        """
        Anyone should be able to view the landing page
        """
        response = Client.http_get(u"")

        assert response is not None
        assert response.ok is True, response
        assert response.controller == u"landing", response
        assert response.duration < 10