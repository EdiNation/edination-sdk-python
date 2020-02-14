# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.ung
import edinationapi.models.une

class EdifactGroup(object):

    """Implementation of the 'EdifactGroup' model.

    TODO: type model description here.

    Attributes:
        ung (UNG): TODO: type description here.
        transactions (list of object): TODO: type description here.
        une_trailers (list of UNE): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transactions":'Transactions',
        "ung":'UNG',
        "une_trailers":'UNETrailers'
    }

    def __init__(self,
                 transactions=None,
                 ung=None,
                 une_trailers=None):
        """Constructor for the EdifactGroup class"""

        # Initialize members of the class
        self.ung = ung
        self.transactions = transactions
        self.une_trailers = une_trailers


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
        transactions = dictionary.get('Transactions')
        ung = edinationapi.models.ung.UNG.from_dictionary(dictionary.get('UNG')) if dictionary.get('UNG') else None
        une_trailers = None
        if dictionary.get('UNETrailers') != None:
            une_trailers = list()
            for structure in dictionary.get('UNETrailers'):
                une_trailers.append(edinationapi.models.une.UNE.from_dictionary(structure))

        # Return an object of this model
        return cls(transactions,
                   ung,
                   une_trailers)


