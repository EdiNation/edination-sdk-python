# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UNE(object):

    """Implementation of the 'UNE' model.

    TODO: type model description here.

    Attributes:
        group_control_count_1 (string): TODO: type description here.
        group_reference_number_2 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_control_count_1":'GroupControlCount_1',
        "group_reference_number_2":'GroupReferenceNumber_2'
    }

    def __init__(self,
                 group_control_count_1=None,
                 group_reference_number_2=None):
        """Constructor for the UNE class"""

        # Initialize members of the class
        self.group_control_count_1 = group_control_count_1
        self.group_reference_number_2 = group_reference_number_2


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
        group_control_count_1 = dictionary.get('GroupControlCount_1')
        group_reference_number_2 = dictionary.get('GroupReferenceNumber_2')

        # Return an object of this model
        return cls(group_control_count_1,
                   group_reference_number_2)


