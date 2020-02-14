# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ISA(object):

    """Implementation of the 'ISA' model.

    TODO: type model description here.

    Attributes:
        authorization_information_qualifier_1 (string): TODO: type description
            here.
        authorization_information_2 (string): TODO: type description here.
        security_information_qualifier_3 (string): TODO: type description
            here.
        security_information_4 (string): TODO: type description here.
        sender_id_qualifier_5 (string): TODO: type description here.
        interchange_sender_id_6 (string): TODO: type description here.
        receiver_id_qualifier_7 (string): TODO: type description here.
        interchange_receiver_id_8 (string): TODO: type description here.
        interchange_date_9 (string): TODO: type description here.
        interchange_time_10 (string): TODO: type description here.
        interchange_control_standards_identifier_11 (string): TODO: type
            description here.
        interchange_control_version_number_12 (string): TODO: type description
            here.
        interchange_control_number_13 (string): TODO: type description here.
        acknowledgement_requested_14 (string): TODO: type description here.
        usage_indicator_15 (string): TODO: type description here.
        component_element_separator_16 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authorization_information_qualifier_1":'AuthorizationInformationQualifier_1',
        "authorization_information_2":'AuthorizationInformation_2',
        "security_information_qualifier_3":'SecurityInformationQualifier_3',
        "security_information_4":'SecurityInformation_4',
        "sender_id_qualifier_5":'SenderIDQualifier_5',
        "interchange_sender_id_6":'InterchangeSenderID_6',
        "receiver_id_qualifier_7":'ReceiverIDQualifier_7',
        "interchange_receiver_id_8":'InterchangeReceiverID_8',
        "interchange_date_9":'InterchangeDate_9',
        "interchange_time_10":'InterchangeTime_10',
        "interchange_control_standards_identifier_11":'InterchangeControlStandardsIdentifier_11',
        "interchange_control_version_number_12":'InterchangeControlVersionNumber_12',
        "interchange_control_number_13":'InterchangeControlNumber_13',
        "acknowledgement_requested_14":'AcknowledgementRequested_14',
        "usage_indicator_15":'UsageIndicator_15',
        "component_element_separator_16":'ComponentElementSeparator_16'
    }

    def __init__(self,
                 authorization_information_qualifier_1=None,
                 authorization_information_2=None,
                 security_information_qualifier_3=None,
                 security_information_4=None,
                 sender_id_qualifier_5=None,
                 interchange_sender_id_6=None,
                 receiver_id_qualifier_7=None,
                 interchange_receiver_id_8=None,
                 interchange_date_9=None,
                 interchange_time_10=None,
                 interchange_control_standards_identifier_11=None,
                 interchange_control_version_number_12=None,
                 interchange_control_number_13=None,
                 acknowledgement_requested_14=None,
                 usage_indicator_15=None,
                 component_element_separator_16=None):
        """Constructor for the ISA class"""

        # Initialize members of the class
        self.authorization_information_qualifier_1 = authorization_information_qualifier_1
        self.authorization_information_2 = authorization_information_2
        self.security_information_qualifier_3 = security_information_qualifier_3
        self.security_information_4 = security_information_4
        self.sender_id_qualifier_5 = sender_id_qualifier_5
        self.interchange_sender_id_6 = interchange_sender_id_6
        self.receiver_id_qualifier_7 = receiver_id_qualifier_7
        self.interchange_receiver_id_8 = interchange_receiver_id_8
        self.interchange_date_9 = interchange_date_9
        self.interchange_time_10 = interchange_time_10
        self.interchange_control_standards_identifier_11 = interchange_control_standards_identifier_11
        self.interchange_control_version_number_12 = interchange_control_version_number_12
        self.interchange_control_number_13 = interchange_control_number_13
        self.acknowledgement_requested_14 = acknowledgement_requested_14
        self.usage_indicator_15 = usage_indicator_15
        self.component_element_separator_16 = component_element_separator_16


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
        authorization_information_qualifier_1 = dictionary.get('AuthorizationInformationQualifier_1')
        authorization_information_2 = dictionary.get('AuthorizationInformation_2')
        security_information_qualifier_3 = dictionary.get('SecurityInformationQualifier_3')
        security_information_4 = dictionary.get('SecurityInformation_4')
        sender_id_qualifier_5 = dictionary.get('SenderIDQualifier_5')
        interchange_sender_id_6 = dictionary.get('InterchangeSenderID_6')
        receiver_id_qualifier_7 = dictionary.get('ReceiverIDQualifier_7')
        interchange_receiver_id_8 = dictionary.get('InterchangeReceiverID_8')
        interchange_date_9 = dictionary.get('InterchangeDate_9')
        interchange_time_10 = dictionary.get('InterchangeTime_10')
        interchange_control_standards_identifier_11 = dictionary.get('InterchangeControlStandardsIdentifier_11')
        interchange_control_version_number_12 = dictionary.get('InterchangeControlVersionNumber_12')
        interchange_control_number_13 = dictionary.get('InterchangeControlNumber_13')
        acknowledgement_requested_14 = dictionary.get('AcknowledgementRequested_14')
        usage_indicator_15 = dictionary.get('UsageIndicator_15')
        component_element_separator_16 = dictionary.get('ComponentElementSeparator_16')

        # Return an object of this model
        return cls(authorization_information_qualifier_1,
                   authorization_information_2,
                   security_information_qualifier_3,
                   security_information_4,
                   sender_id_qualifier_5,
                   interchange_sender_id_6,
                   receiver_id_qualifier_7,
                   interchange_receiver_id_8,
                   interchange_date_9,
                   interchange_time_10,
                   interchange_control_standards_identifier_11,
                   interchange_control_version_number_12,
                   interchange_control_number_13,
                   acknowledgement_requested_14,
                   usage_indicator_15,
                   component_element_separator_16)


