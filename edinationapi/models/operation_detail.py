# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class OperationDetail(object):

    """Implementation of the 'OperationDetail' model.

    TODO: type model description here.

    Attributes:
        index (int): TODO: type description here.
        transaction_index (int): TODO: type description here.
        transaction_ref (string): TODO: type description here.
        segment_id (string): TODO: type description here.
        value (string): TODO: type description here.
        message (string): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "index":'Index',
        "transaction_index":'TransactionIndex',
        "transaction_ref":'TransactionRef',
        "segment_id":'SegmentId',
        "value":'Value',
        "message":'Message',
        "status":'Status'
    }

    def __init__(self,
                 index=None,
                 transaction_index=None,
                 transaction_ref=None,
                 segment_id=None,
                 value=None,
                 message=None,
                 status=None):
        """Constructor for the OperationDetail class"""

        # Initialize members of the class
        self.index = index
        self.transaction_index = transaction_index
        self.transaction_ref = transaction_ref
        self.segment_id = segment_id
        self.value = value
        self.message = message
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
        index = dictionary.get('Index')
        transaction_index = dictionary.get('TransactionIndex')
        transaction_ref = dictionary.get('TransactionRef')
        segment_id = dictionary.get('SegmentId')
        value = dictionary.get('Value')
        message = dictionary.get('Message')
        status = dictionary.get('Status')

        # Return an object of this model
        return cls(index,
                   transaction_index,
                   transaction_ref,
                   segment_id,
                   value,
                   message,
                   status)


