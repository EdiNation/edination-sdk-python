# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.una
import edinationapi.models.unb
import edinationapi.models.edifact_group
import edinationapi.models.unz
import edinationapi.models.operation_result

class EdifactInterchange(object):

    """Implementation of the 'EdifactInterchange' model.

    TODO: type model description here.

    Attributes:
        una (UNA): TODO: type description here.
        unb (UNB): TODO: type description here.
        groups (list of EdifactGroup): TODO: type description here.
        unz_trailers (list of UNZ): TODO: type description here.
        result (OperationResult): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "unb":'UNB',
        "groups":'Groups',
        "una":'UNA',
        "unz_trailers":'UNZTrailers',
        "result":'Result'
    }

    def __init__(self,
                 unb=None,
                 groups=None,
                 una=None,
                 unz_trailers=None,
                 result=None):
        """Constructor for the EdifactInterchange class"""

        # Initialize members of the class
        self.una = una
        self.unb = unb
        self.groups = groups
        self.unz_trailers = unz_trailers
        self.result = result


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
        unb = edinationapi.models.unb.UNB.from_dictionary(dictionary.get('UNB')) if dictionary.get('UNB') else None
        groups = None
        if dictionary.get('Groups') != None:
            groups = list()
            for structure in dictionary.get('Groups'):
                groups.append(edinationapi.models.edifact_group.EdifactGroup.from_dictionary(structure))
        una = edinationapi.models.una.UNA.from_dictionary(dictionary.get('UNA')) if dictionary.get('UNA') else None
        unz_trailers = None
        if dictionary.get('UNZTrailers') != None:
            unz_trailers = list()
            for structure in dictionary.get('UNZTrailers'):
                unz_trailers.append(edinationapi.models.unz.UNZ.from_dictionary(structure))
        result = edinationapi.models.operation_result.OperationResult.from_dictionary(dictionary.get('Result')) if dictionary.get('Result') else None

        # Return an object of this model
        return cls(unb,
                   groups,
                   una,
                   unz_trailers,
                   result)


