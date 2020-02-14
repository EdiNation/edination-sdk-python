# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.operation_detail

class OperationResult(object):

    """Implementation of the 'OperationResult' model.

    TODO: type model description here.

    Attributes:
        last_index (int): TODO: type description here.
        details (list of OperationDetail): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_index":'LastIndex',
        "details":'Details',
        "status":'Status'
    }

    def __init__(self,
                 last_index=None,
                 details=None,
                 status=None):
        """Constructor for the OperationResult class"""

        # Initialize members of the class
        self.last_index = last_index
        self.details = details
        self.status = status


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
        last_index = dictionary.get('LastIndex')
        details = None
        if dictionary.get('Details') != None:
            details = list()
            for structure in dictionary.get('Details'):
                details.append(edinationapi.models.operation_detail.OperationDetail.from_dictionary(structure))
        status = dictionary.get('Status')

        # Return an object of this model
        return cls(last_index,
                   details,
                   status)


