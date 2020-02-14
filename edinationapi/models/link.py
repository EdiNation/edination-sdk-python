# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Link(object):

    """Implementation of the 'Link' model.

    TODO: type model description here.

    Attributes:
        rel (string): TODO: type description here.
        href (string): TODO: type description here.
        action (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rel":'Rel',
        "href":'Href',
        "action":'Action'
    }

    def __init__(self,
                 rel=None,
                 href=None,
                 action=None):
        """Constructor for the Link class"""

        # Initialize members of the class
        self.rel = rel
        self.href = href
        self.action = action


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
        rel = dictionary.get('Rel')
        href = dictionary.get('Href')
        action = dictionary.get('Action')

        # Return an object of this model
        return cls(rel,
                   href,
                   action)


