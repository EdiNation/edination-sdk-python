# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class S001(object):

    """Implementation of the 'S001' model.

    TODO: type model description here.

    Attributes:
        syntax_identifier_1 (string): TODO: type description here.
        syntax_version_number_2 (string): TODO: type description here.
        service_code_list_directory_version_number_3 (string): TODO: type
            description here.
        character_encoding_4 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "syntax_identifier_1":'SyntaxIdentifier_1',
        "syntax_version_number_2":'SyntaxVersionNumber_2',
        "service_code_list_directory_version_number_3":'ServiceCodeListDirectoryVersionNumber_3',
        "character_encoding_4":'CharacterEncoding_4'
    }

    def __init__(self,
                 syntax_identifier_1=None,
                 syntax_version_number_2=None,
                 service_code_list_directory_version_number_3=None,
                 character_encoding_4=None):
        """Constructor for the S001 class"""

        # Initialize members of the class
        self.syntax_identifier_1 = syntax_identifier_1
        self.syntax_version_number_2 = syntax_version_number_2
        self.service_code_list_directory_version_number_3 = service_code_list_directory_version_number_3
        self.character_encoding_4 = character_encoding_4


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        syntax_identifier_1 = dictionary.get('SyntaxIdentifier_1')
        syntax_version_number_2 = dictionary.get('SyntaxVersionNumber_2')
        service_code_list_directory_version_number_3 = dictionary.get('ServiceCodeListDirectoryVersionNumber_3')
        character_encoding_4 = dictionary.get('CharacterEncoding_4')

        # Return an object of this model
        return cls(syntax_identifier_1,
                   syntax_version_number_2,
                   service_code_list_directory_version_number_3,
                   character_encoding_4)


