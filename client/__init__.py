# -*- coding: utf-8 -*
import json
import requests


class Client(object):

    def __init__(self):
        pass

    def __enter__(self):
        self.session = requests.Session()
        self.cookies = self.session.cookies
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        exc_info = (exc_type, exc_val, exc_tb)

        if any(exc_info):
            raise exc_type, exc_val, exc_tb

        return self

    @classmethod
    def http_get(cls, path, session=None):

        url = u"%s/%s" % (cls.get_host(), path)

        if session is None:
            session = requests.Session()

        response = session.get(url)
        return ServerResponse(response, session)

    @classmethod
    def http_post(cls, path, data=None, content_type=None, session=None):

        url = u"%s/%s" % (cls.get_host(), path)

        if session is None:
            session = requests.Session()

        response = session.post(url, data, content_type)
        return ServerResponse(response, session)

    @staticmethod
    def get_host():
        return u"http://localhost:9000"


class ServerResponse:

    def __init__(self, response, session):
        self.ok = False
        self.reason = None
        self.result = response.text
        response = {}
        try:
            response = json.loads(self.result)
        except:
            pass

        self.__dict__.update(response)
        self.session = session
        self.cookies = requests.utils.dict_from_cookiejar(session.cookies)

    def __str__(self):

        if self.ok:
            return u"ok"

        if self.reason is not None:
            return u"is not okay because %s" % self.reason

        if self.result:
            return self.result

        return u"critical error"

    def json(self):
        return json.dumps(self)
