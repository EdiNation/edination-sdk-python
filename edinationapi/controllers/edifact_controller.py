# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

from edinationapi.api_helper import APIHelper
from edinationapi.configuration import Configuration
from edinationapi.controllers.base_controller import BaseController
from edinationapi.http.auth.custom_header_auth import CustomHeaderAuth
from edinationapi.models.edifact_interchange import EdifactInterchange
from edinationapi.models.operation_result import OperationResult
from edinationapi.exceptions.error_details_exception import ErrorDetailsException

class EdifactController(BaseController):

    """A Controller to access Endpoints in the edinationapi API."""


    def read(self,
                file_name,
                ignore_null_values=False,
                continue_on_error=False,
                char_set='utf-8',
                model=None,
                eancom_s_3=False):
        """Does a POST request to /edifact/read.

        Reads an EDIFACT file and returns its contents translated to an array
        of EdifactInterchange objects.

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
            eancom_s_3 (bool, optional): The default syntax for EANCOM
                transactions. By default all EANCOM transactions will be
                translated and validated according to the rules of Syntax 4.
                Set this flag to true if you need Syntax 3 to be used.

        Returns:
            list of EdifactInterchange: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/edifact/read'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'ignoreNullValues': ignore_null_values,
            'continueOnError': continue_on_error,
            'charSet': char_set,
            'model': model,
            'eancomS3': eancom_s_3
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
        return APIHelper.json_deserialize(_context.response.raw_body, EdifactInterchange.from_dictionary)

    def write(self,
                preserve_whitespace=False,
                char_set='utf-8',
                postfix=None,
                same_repetion_and_data_element=False,
                eancom_s_3=False,
                content_type='application/json',
                body=None):
        """Does a POST request to /edifact/write.

        Translates an EdifactInterchange object to a raw EDIFACT interchange
        and returns it as a stream.

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
            same_repetion_and_data_element (bool, optional): Sometimes the
                same delimiter is used to denote data element separator and
                repetition separator as in IATA transactions. By default, this
                is false.
            eancom_s_3 (bool, optional): The default syntax for EANCOM
                transactions. By default all EANCOM transactions will be
                translated and validated according to the rules of Syntax 4.
                Set this flag to true if you need Syntax 3 to be used.
            content_type (string, optional): TODO: type description here.
                Example: application/json
            body (EdifactInterchange, optional): The EdifactInterchange object
                to translate to raw EDIFACT.

        Returns:
            binary: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/edifact/write'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'preserveWhitespace': preserve_whitespace,
            'charSet': char_set,
            'postfix': postfix,
            'sameRepetionAndDataElement': same_repetion_and_data_element,
            'eancomS3': eancom_s_3
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
                 syntax_set=None,
                 skip_trailer=False,
                 structure_only=False,
                 decimal_point='.',
                 eancom_s_3=False,
                 content_type='application/json',
                 body=None):
        """Does a POST request to /edifact/validate.

        Validates an EdifactInterchange object according to the EDIFACT
        standard rules for each version and transaction.

        Args:
            syntax_set (string, optional): In case you need to validate
                against a syntax set, different than UNOA and UNOB, populate
                this filed with all of the allowed symbols, url-escaped.      
                All data elements with alpha (A) or alphanumeric (AN) data
                types are validated against a syntax set of allowed
                characters. The supported syntax sets are UNOA and UNOB. The
                validator infers the correct syntax set from
                EdifactInterchange.UNB.SYNTAXIDENTIFIER_1.SyntaxIdentifier_1.
                The symbols added to this field will override the
                corresponding sets in both UNOA and UNOB.
            skip_trailer (bool, optional): You are allowed to validate an
                EdifactInterchange with missing interchange, functional group
                or transaction trailers (UNZ, UNE, UNT). This is because these
                will be automatically applied during the Write oprtaion so you
                don't have to worry about counting the items. By default it is
                expected that all trailers are present when you validate the
                EdifactInterchange and by default, this is set to false. To
                skip all trailer validation, set this to true.
            structure_only (bool, optional): This is equivalent to HIPAA Snip
                level 1, where only the structure and control segments are
                validated. By default, this is set to false, however if you
                want to not validate things such as data types, number of
                repeteitions or dates, set this to true.
            decimal_point (string, optional): This could be either point .
                (default) or comma ,.
            eancom_s_3 (bool, optional): The default syntax for EANCOM
                transactions. By default all EANCOM transactions will be
                validated according to the rules of Syntax 4. Set this flag to
                true if you need Syntax 3 to be used.
            content_type (string, optional): TODO: type description here.
                Example: application/json
            body (EdifactInterchange, optional): The EdifactInterchange object
                to validate.

        Returns:
            OperationResult: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/edifact/validate'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'syntaxSet': syntax_set,
            'skipTrailer': skip_trailer,
            'structureOnly': structure_only,
            'decimalPoint': decimal_point,
            'eancomS3': eancom_s_3
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
                syntax_set=None,
                detect_duplicates=False,
                tran_ref_number=1,
                interchange_ref_number=1,
                ack_for_valid_trans=False,
                batch_acks=True,
                technical_ack=None,
                eancom_s_3=False,
                content_type='application/json',
                body=None):
        """Does a POST request to /edifact/ack.

        Generates functional and/or technical CONTRL acknowledment(s) for the
        requested EdifactInterchange.

        Args:
            syntax_set (string, optional): In case you need to validate
                against a syntax set, different than UNOA and UNOB, populate
                this filed with all of the allowed symbols, url-escaped. All
                data elements with alpha (A) or alphanumeric (AN) data types
                are validated against a syntax set of allowed characters. The
                supported syntax sets are UNOA and UNOB. The validator infers
                the correct syntax set from
                EdifactInterchange.UNB.SYNTAXIDENTIFIER_1.SyntaxIdentifier_1.
                The symbols added to this field will override the
                corresponding sets in both UNOA and UNOB.
            detect_duplicates (bool, optional): If you need to detect
                duplicates as in functional groups or transactions with the
                same reference number, set this flag to true. The default is
                false.
            tran_ref_number (int, optional): The default is 1. Set this to
                whatever the CONTRL UNH.MessageReferenceNumber_01 needs to
                be.
            interchange_ref_number (int, optional): The default is 1. Set this
                to whatever the CONTRL
                EdifactInterchange.UNB.InterchangeControlReference_5 needs to
                be.
            ack_for_valid_trans (bool, optional): The default is false. Set
                this to true if you need UCM loops included for all valid
                transaction as well. By default UCM loops are generated only
                for invalid transactions.
            batch_acks (bool, optional): The default is true. Set this to
                false if you need to generate separate EdifactInterchange for
                each acknowledgment. By default all acknowledgments are
                batched in the same EdifactInterchange.
            technical_ack (string, optional): The default technical
                acknowledgment CONTRL is generated according to
                EdifactInterchange.UNB.AcknowledgementRequest_9. You can
                either enforce it to always generate technical CONTRLs or
                supress it to never generate any technical CONTRLs. This will
                override the flag in
                EdifactInterchange.UNB.AcknowledgementRequest_9.             
                The available values are: default, enforce, suppress.
            eancom_s_3 (bool, optional): The default syntax for EANCOM
                transactions. By default all EANCOM transactions will be
                validated according to the rules of Syntax 4. Set this flag to
                true if you need Syntax 3 to be used.
            content_type (string, optional): TODO: type description here.
                Example: application/json
            body (EdifactInterchange, optional): The EdifactInterchange object
                to acknowledge.

        Returns:
            list of EdifactInterchange: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/edifact/ack'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'syntaxSet': syntax_set,
            'detectDuplicates': detect_duplicates,
            'tranRefNumber': tran_ref_number,
            'interchangeRefNumber': interchange_ref_number,
            'ackForValidTrans': ack_for_valid_trans,
            'batchAcks': batch_acks,
            'technicalAck': technical_ack,
            'eancomS3': eancom_s_3
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
        return APIHelper.json_deserialize(_context.response.raw_body, EdifactInterchange.from_dictionary)
