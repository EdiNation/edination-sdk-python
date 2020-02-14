# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UNZ(object):

    """Implementation of the 'UNZ' model.

    TODO: type model description here.

    Attributes:
        interchange_control_count_1 (string): TODO: type description here.
        interchange_control_reference_2 (string): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interchange_control_count_1":'InterchangeControlCount_1',
        "interchange_control_reference_2":'InterchangeControlReference_2'
    }

    def __init__(self,
                 interchange_control_count_1=None,
                 interchange_control_reference_2=None):
        """Constructor for the UNZ class"""

        # Initialize members of the class
        self.interchange_control_count_1 = interchange_control_count_1
        self.interchange_control_reference_2 = interchange_control_reference_2


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
        interchange_control_count_1 = dictionary.get('InterchangeControlCount_1')
        interchange_control_reference_2 = dictionary.get('InterchangeControlReference_2')

        # Return an object of this model
        return cls(interchange_control_count_1,
                   interchange_control_reference_2)


