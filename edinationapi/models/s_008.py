# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class S008(object):

    """Implementation of the 'S008' model.

    TODO: type model description here.

    Attributes:
        message_version_number_1 (string): TODO: type description here.
        message_release_number_2 (string): TODO: type description here.
        association_assigned_code_3 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message_version_number_1":'MessageVersionNumber_1',
        "message_release_number_2":'MessageReleaseNumber_2',
        "association_assigned_code_3":'AssociationAssignedCode_3'
    }

    def __init__(self,
                 message_version_number_1=None,
                 message_release_number_2=None,
                 association_assigned_code_3=None):
        """Constructor for the S008 class"""

        # Initialize members of the class
        self.message_version_number_1 = message_version_number_1
        self.message_release_number_2 = message_release_number_2
        self.association_assigned_code_3 = association_assigned_code_3


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
        message_version_number_1 = dictionary.get('MessageVersionNumber_1')
        message_release_number_2 = dictionary.get('MessageReleaseNumber_2')
        association_assigned_code_3 = dictionary.get('AssociationAssignedCode_3')

        # Return an object of this model
        return cls(message_version_number_1,
                   message_release_number_2,
                   association_assigned_code_3)


