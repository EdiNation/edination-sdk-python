# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class IEA(object):

    """Implementation of the 'IEA' model.

    TODO: type model description here.

    Attributes:
        number_of_included_groups_1 (string): TODO: type description here.
        interchange_control_number_2 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_of_included_groups_1":'NumberOfIncludedGroups_1',
        "interchange_control_number_2":'InterchangeControlNumber_2'
    }

    def __init__(self,
                 number_of_included_groups_1=None,
                 interchange_control_number_2=None):
        """Constructor for the IEA class"""

        # Initialize members of the class
        self.number_of_included_groups_1 = number_of_included_groups_1
        self.interchange_control_number_2 = interchange_control_number_2


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
        number_of_included_groups_1 = dictionary.get('NumberOfIncludedGroups_1')
        interchange_control_number_2 = dictionary.get('InterchangeControlNumber_2')

        # Return an object of this model
        return cls(number_of_included_groups_1,
                   interchange_control_number_2)


