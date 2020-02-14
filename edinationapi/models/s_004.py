# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class S004(object):

    """Implementation of the 'S004' model.

    TODO: type model description here.

    Attributes:
        date_1 (string): TODO: type description here.
        time_2 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_1":'Date_1',
        "time_2":'Time_2'
    }

    def __init__(self,
                 date_1=None,
                 time_2=None):
        """Constructor for the S004 class"""

        # Initialize members of the class
        self.date_1 = date_1
        self.time_2 = time_2


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
        date_1 = dictionary.get('Date_1')
        time_2 = dictionary.get('Time_2')

        # Return an object of this model
        return cls(date_1,
                   time_2)


