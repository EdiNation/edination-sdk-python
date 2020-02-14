# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.s_006
import edinationapi.models.s_007
import edinationapi.models.s_004
import edinationapi.models.s_008

class UNG(object):

    """Implementation of the 'UNG' model.

    TODO: type model description here.

    Attributes:
        message_group_identification_1 (string): TODO: type description here.
        applicationsenderidentification_2 (S006): TODO: type description
            here.
        applicationrecipientidentification_3 (S007): TODO: type description
            here.
        dateandtimeofpreparation_4 (S004): TODO: type description here.
        group_reference_number_5 (string): TODO: type description here.
        controlling_agency_6 (string): TODO: type description here.
        messageversion_7 (S008): TODO: type description here.
        application_password_8 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message_group_identification_1":'MessageGroupIdentification_1',
        "applicationsenderidentification_2":'APPLICATIONSENDERIDENTIFICATION_2',
        "applicationrecipientidentification_3":'APPLICATIONRECIPIENTIDENTIFICATION_3',
        "dateandtimeofpreparation_4":'DATEANDTIMEOFPREPARATION_4',
        "group_reference_number_5":'GroupReferenceNumber_5',
        "controlling_agency_6":'ControllingAgency_6',
        "messageversion_7":'MESSAGEVERSION_7',
        "application_password_8":'ApplicationPassword_8'
    }

    def __init__(self,
                 message_group_identification_1=None,
                 applicationsenderidentification_2=None,
                 applicationrecipientidentification_3=None,
                 dateandtimeofpreparation_4=None,
                 group_reference_number_5=None,
                 controlling_agency_6=None,
                 messageversion_7=None,
                 application_password_8=None):
        """Constructor for the UNG class"""

        # Initialize members of the class
        self.message_group_identification_1 = message_group_identification_1
        self.applicationsenderidentification_2 = applicationsenderidentification_2
        self.applicationrecipientidentification_3 = applicationrecipientidentification_3
        self.dateandtimeofpreparation_4 = dateandtimeofpreparation_4
        self.group_reference_number_5 = group_reference_number_5
        self.controlling_agency_6 = controlling_agency_6
        self.messageversion_7 = messageversion_7
        self.application_password_8 = application_password_8


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
        message_group_identification_1 = dictionary.get('MessageGroupIdentification_1')
        applicationsenderidentification_2 = edinationapi.models.s_006.S006.from_dictionary(dictionary.get('APPLICATIONSENDERIDENTIFICATION_2')) if dictionary.get('APPLICATIONSENDERIDENTIFICATION_2') else None
        applicationrecipientidentification_3 = edinationapi.models.s_007.S007.from_dictionary(dictionary.get('APPLICATIONRECIPIENTIDENTIFICATION_3')) if dictionary.get('APPLICATIONRECIPIENTIDENTIFICATION_3') else None
        dateandtimeofpreparation_4 = edinationapi.models.s_004.S004.from_dictionary(dictionary.get('DATEANDTIMEOFPREPARATION_4')) if dictionary.get('DATEANDTIMEOFPREPARATION_4') else None
        group_reference_number_5 = dictionary.get('GroupReferenceNumber_5')
        controlling_agency_6 = dictionary.get('ControllingAgency_6')
        messageversion_7 = edinationapi.models.s_008.S008.from_dictionary(dictionary.get('MESSAGEVERSION_7')) if dictionary.get('MESSAGEVERSION_7') else None
        application_password_8 = dictionary.get('ApplicationPassword_8')

        # Return an object of this model
        return cls(message_group_identification_1,
                   applicationsenderidentification_2,
                   applicationrecipientidentification_3,
                   dateandtimeofpreparation_4,
                   group_reference_number_5,
                   controlling_agency_6,
                   messageversion_7,
                   application_password_8)


