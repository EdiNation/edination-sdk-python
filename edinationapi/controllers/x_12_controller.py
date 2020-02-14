# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

from edinationapi.api_helper import APIHelper
from edinationapi.configuration import Configuration
from edinationapi.controllers.base_controller import BaseController
from edinationapi.http.auth.custom_header_auth import CustomHeaderAuth
from edinationapi.models.x_12_interchange import X12Interchange
from edinationapi.models.operation_result import OperationResult
from edinationapi.exceptions.error_details_exception import ErrorDetailsException

class X12Controller(BaseController):

    """A Controller to access Endpoints in the edinationapi API."""


    def read(self,
                file_name,
                ignore_null_values=False,
                continue_on_error=False,
                char_set='utf-8',
                model=None):
        """Does a POST request to /x12/read.

        Reads an X12 file and returns its contents translated to an array of
        X12Interchange objects.

        Args:
            file_name (string): Upload File
            ignore_null_values (bool, optional): Whether to ignore all null
                values in the response. The default is false.
            continue_on_error (bool, optional): Whether to continue reading if
                a corrupt interchange is encountered. The default is false.
            char_set (string, optional): The encoding of the file contents.
                The default is utf-8. The available values are: unicodeFFFE,
                utf-32, utf-32BE, us-ascii, iso-8859-1, utf-7, utf-8, utf-16.
            model (string, optional): The model to use. By default, the API
                will infer the model based on the transaction and version
                identifiers.

        Returns:
            list of X12Interchange: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/x12/read'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'ignoreNullValues': ignore_null_values,
            'continueOnError': continue_on_error,
            'charSet': char_set,
            'model': model
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'fileName': file_name
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, files=_files)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, X12Interchange.from_dictionary)

    def write(self,
                preserve_whitespace=False,
                char_set='utf-8',
                postfix=None,
                content_type='application/json',
                body=None):
        """Does a POST request to /x12/write.

        Translates an X12Interchange object to a raw X12 interchange and
        returns it as a stream.

        Args:
            preserve_whitespace (bool, optional): Whether to preserve blank
                data elements so the output contains multiple delimiters
                instead of omitting any excess delimiters. The default is
                false.
            char_set (string, optional): The encoding of the file contents.
                The default is utf-8. The available values are: unicodeFFFE,
                utf-32, utf-32BE, us-ascii, iso-8859-1, utf-7, utf-8, utf-16.
            postfix (string, optional): The postfix to be applied at the end
                of each segment, just after the segment separator. This is
                usually a carriage return (CR), line feed (LF) or both. By
                default, there is no postfix.
            content_type (string, optional): TODO: type description here.
                Example: application/json
            body (X12Interchange, optional): The X12Interchange object to
                translate to raw X12.

        Returns:
            binary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/x12/write'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'preserveWhitespace': preserve_whitespace,
            'charSet': char_set,
            'postfix': postfix
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
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

    def validate(self,
                 basic_syntax=False,
                 syntax_set=None,
                 skip_trailer=False,
                 structure_only=False,
                 content_type='application/json',
                 body=None):
        """Does a POST request to /x12/validate.

        Validates an X12Interchange object according to the X12 standard rules
        for each version and transaction.

        Args:
            basic_syntax (bool, optional): All data elements with alpha (A) or
                alphanumeric (AN) data types are validated against a syntax
                set of allowed characters. The default syntax set is the
                Extended, hence the default for this parameter is false. By
                setting this to true, validation will use the Basic syntax
                set.
            syntax_set (string, optional): In case you need to validate
                against a syntax set, different than Basic and Extended,
                populate this filed with all of the allowed symbols,
                url-escaped.
            skip_trailer (bool, optional): You are allowed to validate an
                X12Interchange with missing interchange, functional group or
                transaction trailers (IEA, GE, SE). This is because these will
                be automatically applied during the Write oprtaion so you
                don't have to worry about counting the items. By default it is
                expected that all trailers are present when you validate the
                X12Interchange and by default, this is set to false. To skip
                all trailer validation, set this to true.
            structure_only (bool, optional): This is equivalent to HIPAA Snip
                level 1, where only the structure and control segments are
                validated. By default, this is set to false, however if you
                want to not validate things such as data types, number of
                repeteitions or dates, set this to true.
            content_type (string, optional): TODO: type description here.
                Example: application/json
            body (X12Interchange, optional): The X12Interchange object to
                validate.

        Returns:
            OperationResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/x12/validate'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'basicSyntax': basic_syntax,
            'syntaxSet': syntax_set,
            'skipTrailer': skip_trailer,
            'structureOnly': structure_only
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, OperationResult.from_dictionary)

    def ack(self,
                basic_syntax=False,
                syntax_set=None,
                detect_duplicates=False,
                tran_ref_number=1,
                interchange_ref_number=1,
                ack_for_valid_trans=False,
                batch_acks=True,
                technical_ack=None,
                ack='997',
                ak_901_is_p=False,
                content_type='application/json',
                body=None):
        """Does a POST request to /x12/ack.

        Generates functional/implementation and/or technical acknowledment(s)
        for the requested X12Interchange.

        Args:
            basic_syntax (bool, optional): All data elements with alpha (A) or
                alphanumeric (AN) data types are validated against a syntax
                set of allowed characters. The default syntax set is the
                Extended, hence the default for this parameter is false. By
                setting this to true, validation will use the Basic syntax
                set.
            syntax_set (string, optional): In case you need to validate
                against a syntax set, different than Basic and Extended,
                populate this filed with all of the allowed symbols,
                url-escaped.
            detect_duplicates (bool, optional): If you need to detect
                duplicates as in functional groups or transactions with the
                same reference number, set this flag to true. The default is
                false.
            tran_ref_number (int, optional): The default is 1. Set this to
                whatever the 997 or 999
                X12Interchange.ST.TransactionSetControlNumber_02 needs to be.
                In case there are multiple acknowledgments (for multiple
                functional groups), this will be starting reference number and
                every subsequent acknowledgment will have the previous
                reference number incremented with 1.
            interchange_ref_number (int, optional): The default is 1. Set this
                to whatever the 997 or 999
                X12Interchange.ISA.InterchangeControlNumber_13 needs to be.
            ack_for_valid_trans (bool, optional): The default is false. Set
                this to true if you need AK2 loops included for all valid
                transaction as well. By default AK2 loops are generated only
                for invalid transactions.
            batch_acks (bool, optional): The default is true. Set this to
                false if you need to generate separate X12Interchange for each
                acknowledgment. By default all acknowledgments are batched in
                the same X12Interchange.
            technical_ack (string, optional): The default technical
                acknowledgment TA1 is generated according to
                X12Interchange.ISA.AcknowledgementRequested_14. You can either
                enforce it to always generate TA1s or supress it to never
                generate any TA1s. This will override the flag in
                X12Interchange.ISA.AcknowledgementRequested_14.             
                The available values are: default, enforce, suppress.
            ack (string, optional): The default value is 997. The type of
                acknowledgment being generated. Set this to 999 if you need to
                generate an implementation instead of functional
                acknowledgment. The available values are: 997, 999.
            ak_901_is_p (bool, optional): The value of the AK9's first
                element. By default it is "E". Set this to true if you want
                this value to be "P" instead.
            content_type (string, optional): TODO: type description here.
                Example: application/json
            body (X12Interchange, optional): The X12Interchange object to
                acknowledge.

        Returns:
            list of X12Interchange: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/x12/ack'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'basicSyntax': basic_syntax,
            'syntaxSet': syntax_set,
            'detectDuplicates': detect_duplicates,
            'tranRefNumber': tran_ref_number,
            'interchangeRefNumber': interchange_ref_number,
            'ackForValidTrans': ack_for_valid_trans,
            'batchAcks': batch_acks,
            'technicalAck': technical_ack,
            'ack': ack,
            'ak901isP': ak_901_is_p
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': content_type
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorDetailsException('Bad Request', _context)
        elif _context.response.status_code == 500:
            raise ErrorDetailsException('Server Error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, X12Interchange.from_dictionary)
