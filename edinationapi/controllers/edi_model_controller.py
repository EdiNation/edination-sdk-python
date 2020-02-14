# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

from edinationapi.api_helper import APIHelper
from edinationapi.configuration import Configuration
from edinationapi.controllers.base_controller import BaseController
from edinationapi.http.auth.custom_header_auth import CustomHeaderAuth
from edinationapi.models.edi_model import EdiModel
from edinationapi.exceptions.error_details_exception import ErrorDetailsException

class EdiModelController(BaseController):

    """A Controller to access Endpoints in the edinationapi API."""


    def upload(self,
                file_name):
        """Does a POST request to /models.

        Uploads a model file to a subscription. It must be a valid DOT NET
        assembly.

        Args:
            file_name (string): Upload File

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/models'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'fileName': file_name
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, files=_files)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)

    def get_models(self,
                   system=True):
        """Does a GET request to /models.

        Retrieves all models for a subscription.

        Args:
            system (bool, optional): Whether to retrieve EdiNation's or custom
                uploaded models.

        Returns:
            list of EdiModel: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/models'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'system': system
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EdiModel.from_dictionary)

    def get_model(self,
                  id,
                  system=True):
        """Does a GET request to /models/{id}.

        Retrieve a particular model file as a stream.

        Args:
            id (string): The model name.
            system (bool, optional): Whether to search in EdiNation's or
                custom uploaded models.

        Returns:
            binary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/models/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'system': system
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request, binary = True)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def delete(self,
                id):
        """Does a DELETE request to /models/{id}.

        Deletes a particular model from the custom models.

        Args:
            id (string): The model name.

        Returns:
            void: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/models/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'id': id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)
