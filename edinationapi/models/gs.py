# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class GS(object):

    """Implementation of the 'GS' model.

    TODO: type model description here.

    Attributes:
        code_identifying_information_type_1 (string): TODO: type description
            here.
        sender_id_code_2 (string): TODO: type description here.
        receiver_id_code_3 (string): TODO: type description here.
        date_4 (string): TODO: type description here.
        time_5 (string): TODO: type description here.
        group_control_number_6 (string): TODO: type description here.
        transaction_type_code_7 (string): TODO: type description here.
        version_and_release_8 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code_identifying_information_type_1":'CodeIdentifyingInformationType_1',
        "sender_id_code_2":'SenderIDCode_2',
        "receiver_id_code_3":'ReceiverIDCode_3',
        "date_4":'Date_4',
        "time_5":'Time_5',
        "group_control_number_6":'GroupControlNumber_6',
        "transaction_type_code_7":'TransactionTypeCode_7',
        "version_and_release_8":'VersionAndRelease_8'
    }

    def __init__(self,
                 code_identifying_information_type_1=None,
                 sender_id_code_2=None,
                 receiver_id_code_3=None,
                 date_4=None,
                 time_5=None,
                 group_control_number_6=None,
                 transaction_type_code_7=None,
                 version_and_release_8=None):
        """Constructor for the GS class"""

        # Initialize members of the class
        self.code_identifying_information_type_1 = code_identifying_information_type_1
        self.sender_id_code_2 = sender_id_code_2
        self.receiver_id_code_3 = receiver_id_code_3
        self.date_4 = date_4
        self.time_5 = time_5
        self.group_control_number_6 = group_control_number_6
        self.transaction_type_code_7 = transaction_type_code_7
        self.version_and_release_8 = version_and_release_8


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
        code_identifying_information_type_1 = dictionary.get('CodeIdentifyingInformationType_1')
        sender_id_code_2 = dictionary.get('SenderIDCode_2')
        receiver_id_code_3 = dictionary.get('ReceiverIDCode_3')
        date_4 = dictionary.get('Date_4')
        time_5 = dictionary.get('Time_5')
        group_control_number_6 = dictionary.get('GroupControlNumber_6')
        transaction_type_code_7 = dictionary.get('TransactionTypeCode_7')
        version_and_release_8 = dictionary.get('VersionAndRelease_8')

        # Return an object of this model
        return cls(code_identifying_information_type_1,
                   sender_id_code_2,
                   receiver_id_code_3,
                   date_4,
                   time_5,
                   group_control_number_6,
                   transaction_type_code_7,
                   version_and_release_8)


