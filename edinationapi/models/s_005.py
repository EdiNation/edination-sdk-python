# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class S005(object):

    """Implementation of the 'S005' model.

    TODO: type model description here.

    Attributes:
        recipient_reference_password_1 (string): TODO: type description here.
        recipient_reference_password_qualifier_2 (string): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "recipient_reference_password_1":'RecipientReferencePassword_1',
        "recipient_reference_password_qualifier_2":'RecipientReferencePasswordQualifier_2'
    }

    def __init__(self,
                 recipient_reference_password_1=None,
                 recipient_reference_password_qualifier_2=None):
        """Constructor for the S005 class"""

        # Initialize members of the class
        self.recipient_reference_password_1 = recipient_reference_password_1
        self.recipient_reference_password_qualifier_2 = recipient_reference_password_qualifier_2


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
        recipient_reference_password_1 = dictionary.get('RecipientReferencePassword_1')
        recipient_reference_password_qualifier_2 = dictionary.get('RecipientReferencePasswordQualifier_2')

        # Return an object of this model
        return cls(recipient_reference_password_1,
                   recipient_reference_password_qualifier_2)


