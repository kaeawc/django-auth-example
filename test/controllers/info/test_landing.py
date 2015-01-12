# -*- coding: utf-8 -*
from test import DjangoTestCase


class LandingSpec(DjangoTestCase):

    def test_success(self):
        """
        Anyone should be able to view the authors page
        """
        response = self.http_get(u"/")

        assert response is not None
        assert response.ok is True, response
        assert response.controller == u"landing", response
        assert response.duration < 10
