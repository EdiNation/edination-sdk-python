# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.link

class EdiModel(object):

    """Implementation of the 'EdiModel' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        date_created (string): TODO: type description here.
        links (list of Link): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'Name',
        "date_created":'DateCreated',
        "links":'Links'
    }

    def __init__(self,
                 name=None,
                 date_created=None,
                 links=None):
        """Constructor for the EdiModel class"""

        # Initialize members of the class
        self.name = name
        self.date_created = date_created
        self.links = links


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
        name = dictionary.get('Name')
        date_created = dictionary.get('DateCreated')
        links = None
        if dictionary.get('Links') != None:
            links = list()
            for structure in dictionary.get('Links'):
                links.append(edinationapi.models.link.Link.from_dictionary(structure))

        # Return an object of this model
        return cls(name,
                   date_created,
                   links)


