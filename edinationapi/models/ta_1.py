# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TA1(object):

    """Implementation of the 'TA1' model.

    TODO: type model description here.

    Attributes:
        interchange_control_number_1 (string): TODO: type description here.
        interchange_date_2 (string): TODO: type description here.
        interchange_time_3 (string): TODO: type description here.
        interchange_acknowledgment_code_4 (string): TODO: type description
            here.
        interchange_note_code_5 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interchange_control_number_1":'InterchangeControlNumber_1',
        "interchange_date_2":'InterchangeDate_2',
        "interchange_time_3":'InterchangeTime_3',
        "interchange_acknowledgment_code_4":'InterchangeAcknowledgmentCode_4',
        "interchange_note_code_5":'InterchangeNoteCode_5'
    }

    def __init__(self,
                 interchange_control_number_1=None,
                 interchange_date_2=None,
                 interchange_time_3=None,
                 interchange_acknowledgment_code_4=None,
                 interchange_note_code_5=None):
        """Constructor for the TA1 class"""

        # Initialize members of the class
        self.interchange_control_number_1 = interchange_control_number_1
        self.interchange_date_2 = interchange_date_2
        self.interchange_time_3 = interchange_time_3
        self.interchange_acknowledgment_code_4 = interchange_acknowledgment_code_4
        self.interchange_note_code_5 = interchange_note_code_5


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
        interchange_control_number_1 = dictionary.get('InterchangeControlNumber_1')
        interchange_date_2 = dictionary.get('InterchangeDate_2')
        interchange_time_3 = dictionary.get('InterchangeTime_3')
        interchange_acknowledgment_code_4 = dictionary.get('InterchangeAcknowledgmentCode_4')
        interchange_note_code_5 = dictionary.get('InterchangeNoteCode_5')

        # Return an object of this model
        return cls(interchange_control_number_1,
                   interchange_date_2,
                   interchange_time_3,
                   interchange_acknowledgment_code_4,
                   interchange_note_code_5)


