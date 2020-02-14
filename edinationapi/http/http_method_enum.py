# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

class HttpMethodEnum(object):

    """Enumeration of an HTTP Method

    Attributes:
        GET: A GET Request
        POST: A POST Request
        PUT: A PUT Request
        PATCH: A PATCH Request
        DELETE: A DELETE Request

    """

    GET = "GET"

    POST = "POST"

    PUT = "PUT"

    PATCH = "PATCH"

    DELETE = "DELETE"

    HEAD = "HEAD"

    @classmethod
    def to_string(cls, val):
        """Returns the string equivalent for the Enum.

        """
        for k, v in list(vars(cls).items()):
            if v == val:
                return k

    @classmethod
    def from_string(cls, str):
        """Creates an instance of the Enum from a given string.

        """
        return getattr(cls, str.upper(), None)
