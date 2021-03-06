# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class S003(object):

    """Implementation of the 'S003' model.

    TODO: type model description here.

    Attributes:
        interchange_recipient_identification_1 (string): TODO: type
            description here.
        identification_code_qualifier_2 (string): TODO: type description
            here.
        interchange_recipient_internal_identification_3 (string): TODO: type
            description here.
        interchange_recipient_internal_sub_identification_4 (string): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interchange_recipient_identification_1":'InterchangeRecipientIdentification_1',
        "identification_code_qualifier_2":'IdentificationCodeQualifier_2',
        "interchange_recipient_internal_identification_3":'InterchangeRecipientInternalIdentification_3',
        "interchange_recipient_internal_sub_identification_4":'InterchangeRecipientInternalSubIdentification_4'
    }

    def __init__(self,
                 interchange_recipient_identification_1=None,
                 identification_code_qualifier_2=None,
                 interchange_recipient_internal_identification_3=None,
                 interchange_recipient_internal_sub_identification_4=None):
        """Constructor for the S003 class"""

        # Initialize members of the class
        self.interchange_recipient_identification_1 = interchange_recipient_identification_1
        self.identification_code_qualifier_2 = identification_code_qualifier_2
        self.interchange_recipient_internal_identification_3 = interchange_recipient_internal_identification_3
        self.interchange_recipient_internal_sub_identification_4 = interchange_recipient_internal_sub_identification_4


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
        interchange_recipient_identification_1 = dictionary.get('InterchangeRecipientIdentification_1')
        identification_code_qualifier_2 = dictionary.get('IdentificationCodeQualifier_2')
        interchange_recipient_internal_identification_3 = dictionary.get('InterchangeRecipientInternalIdentification_3')
        interchange_recipient_internal_sub_identification_4 = dictionary.get('InterchangeRecipientInternalSubIdentification_4')

        # Return an object of this model
        return cls(interchange_recipient_identification_1,
                   identification_code_qualifier_2,
                   interchange_recipient_internal_identification_3,
                   interchange_recipient_internal_sub_identification_4)


