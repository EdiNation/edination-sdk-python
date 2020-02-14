# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class S007(object):

    """Implementation of the 'S007' model.

    TODO: type model description here.

    Attributes:
        application_recipient_identification_1 (string): TODO: type
            description here.
        identification_code_qualifier_2 (string): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_recipient_identification_1":'ApplicationRecipientIdentification_1',
        "identification_code_qualifier_2":'IdentificationCodeQualifier_2'
    }

    def __init__(self,
                 application_recipient_identification_1=None,
                 identification_code_qualifier_2=None):
        """Constructor for the S007 class"""

        # Initialize members of the class
        self.application_recipient_identification_1 = application_recipient_identification_1
        self.identification_code_qualifier_2 = identification_code_qualifier_2


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
        application_recipient_identification_1 = dictionary.get('ApplicationRecipientIdentification_1')
        identification_code_qualifier_2 = dictionary.get('IdentificationCodeQualifier_2')

        # Return an object of this model
        return cls(application_recipient_identification_1,
                   identification_code_qualifier_2)


