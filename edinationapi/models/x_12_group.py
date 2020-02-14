# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.gs
import edinationapi.models.ge

class X12Group(object):

    """Implementation of the 'X12Group' model.

    TODO: type model description here.

    Attributes:
        gs (GS): TODO: type description here.
        transactions (list of object): TODO: type description here.
        ge_trailers (list of GE): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gs":'GS',
        "transactions":'Transactions',
        "ge_trailers":'GETrailers'
    }

    def __init__(self,
                 gs=None,
                 transactions=None,
                 ge_trailers=None):
        """Constructor for the X12Group class"""

        # Initialize members of the class
        self.gs = gs
        self.transactions = transactions
        self.ge_trailers = ge_trailers


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
        gs = edinationapi.models.gs.GS.from_dictionary(dictionary.get('GS')) if dictionary.get('GS') else None
        transactions = dictionary.get('Transactions')
        ge_trailers = None
        if dictionary.get('GETrailers') != None:
            ge_trailers = list()
            for structure in dictionary.get('GETrailers'):
                ge_trailers.append(edinationapi.models.ge.GE.from_dictionary(structure))

        # Return an object of this model
        return cls(gs,
                   transactions,
                   ge_trailers)


