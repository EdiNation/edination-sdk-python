# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UNA(object):

    """Implementation of the 'UNA' model.

    TODO: type model description here.

    Attributes:
        component_data_element (string): TODO: type description here.
        data_element (string): TODO: type description here.
        decimal_notation (string): TODO: type description here.
        release_indicator (string): TODO: type description here.
        reserved (string): TODO: type description here.
        segment (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "component_data_element":'ComponentDataElement',
        "data_element":'DataElement',
        "decimal_notation":'DecimalNotation',
        "release_indicator":'ReleaseIndicator',
        "reserved":'Reserved',
        "segment":'Segment'
    }

    def __init__(self,
                 component_data_element=None,
                 data_element=None,
                 decimal_notation=None,
                 release_indicator=None,
                 reserved=None,
                 segment=None):
        """Constructor for the UNA class"""

        # Initialize members of the class
        self.component_data_element = component_data_element
        self.data_element = data_element
        self.decimal_notation = decimal_notation
        self.release_indicator = release_indicator
        self.reserved = reserved
        self.segment = segment


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
        component_data_element = dictionary.get('ComponentDataElement')
        data_element = dictionary.get('DataElement')
        decimal_notation = dictionary.get('DecimalNotation')
        release_indicator = dictionary.get('ReleaseIndicator')
        reserved = dictionary.get('Reserved')
        segment = dictionary.get('Segment')

        # Return an object of this model
        return cls(component_data_element,
                   data_element,
                   decimal_notation,
                   release_indicator,
                   reserved,
                   segment)


