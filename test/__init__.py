# -*- coding: utf-8 -*
import json
from datetime import datetime
from django.test import TestCase
from django.http.response import JsonResponse


class DjangoTestCase(TestCase):

    def http_get(self, path):

        if self.client is None:
            raise Exception(u"Cannot make requests if test server hasn't been initialized.")

        start_time = datetime.utcnow()
        response = self.client.get(path)
        end_time = datetime.utcnow()
        duration = (start_time - end_time).total_seconds() * 1000
        return ServerResponse(response, client=self.client, duration=duration)

    def http_post(self, path, data=None, content_type=None):

        if self.client is None:
            raise Exception(u"Cannot make requests if test server hasn't been initialized.")

        start_time = datetime.utcnow()
        response = self.client.post(path, data)
        end_time = datetime.utcnow()
        duration = (start_time - end_time).total_seconds() * 1000
        return ServerResponse(response, client=self.client, duration=duration)


class ServerResponse:

    def __init__(self, response, client, duration):
        self.ok = False
        self.reason = None
        self.duration = duration
        self.controller = None
        self.response = None

        if isinstance(response, JsonResponse):
            self.response = dict(json.loads(response.content))
            self.__dict__.update(self.response)

        else:
            raise Exception(response)

    def __str__(self):

        if self.ok:
            return u"ok, %s" % self.response

        if self.reason is not None:
            return u"is not okay because %s: %s" % (self.reason, self.response)

        if self.response:
            return self.response

        return u"critical error"

    def json(self):
        return json.dumps(self)
