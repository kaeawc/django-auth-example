# -*- coding: utf-8 -*
from test import DjangoTestCase


class AuthorsSpec(DjangoTestCase):

    def test_success(self):
        """
        Anyone should be able to view the authors page
        """
        response = self.http_get(u"/authors")

        assert response is not None
        assert response.ok is True, response
        assert response.controller == u"authors", response
        assert response.duration < 10
