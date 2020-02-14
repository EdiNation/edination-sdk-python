# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.isa
import edinationapi.models.ta_1
import edinationapi.models.x_12_group
import edinationapi.models.iea
import edinationapi.models.operation_result

class X12Interchange(object):

    """Implementation of the 'X12Interchange' model.

    TODO: type model description here.

    Attributes:
        segment_delimiter (string): TODO: type description here.
        data_element_delimiter (string): TODO: type description here.
        isa (ISA): TODO: type description here.
        ta_1 (TA1): TODO: type description here.
        groups (list of X12Group): TODO: type description here.
        iea_trailers (list of IEA): TODO: type description here.
        result (OperationResult): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segment_delimiter":'SegmentDelimiter',
        "data_element_delimiter":'DataElementDelimiter',
        "isa":'ISA',
        "groups":'Groups',
        "ta_1":'TA1',
        "iea_trailers":'IEATrailers',
        "result":'Result'
    }

    def __init__(self,
                 segment_delimiter=None,
                 data_element_delimiter=None,
                 isa=None,
                 groups=None,
                 ta_1=None,
                 iea_trailers=None,
                 result=None):
        """Constructor for the X12Interchange class"""

        # Initialize members of the class
        self.segment_delimiter = segment_delimiter
        self.data_element_delimiter = data_element_delimiter
        self.isa = isa
        self.ta_1 = ta_1
        self.groups = groups
        self.iea_trailers = iea_trailers
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
        segment_delimiter = dictionary.get('SegmentDelimiter')
        data_element_delimiter = dictionary.get('DataElementDelimiter')
        isa = edinationapi.models.isa.ISA.from_dictionary(dictionary.get('ISA')) if dictionary.get('ISA') else None
        groups = None
        if dictionary.get('Groups') != None:
            groups = list()
            for structure in dictionary.get('Groups'):
                groups.append(edinationapi.models.x_12_group.X12Group.from_dictionary(structure))
        ta_1 = edinationapi.models.ta_1.TA1.from_dictionary(dictionary.get('TA1')) if dictionary.get('TA1') else None
        iea_trailers = None
        if dictionary.get('IEATrailers') != None:
            iea_trailers = list()
            for structure in dictionary.get('IEATrailers'):
                iea_trailers.append(edinationapi.models.iea.IEA.from_dictionary(structure))
        result = edinationapi.models.operation_result.OperationResult.from_dictionary(dictionary.get('Result')) if dictionary.get('Result') else None

        # Return an object of this model
        return cls(segment_delimiter,
                   data_element_delimiter,
                   isa,
                   groups,
                   ta_1,
                   iea_trailers,
                   result)


