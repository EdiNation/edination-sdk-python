# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

import edinationapi.models.s_001
import edinationapi.models.s_002
import edinationapi.models.s_003
import edinationapi.models.s_004
import edinationapi.models.s_005

class UNB(object):

    """Implementation of the 'UNB' model.

    TODO: type model description here.

    Attributes:
        syntaxidentifier_1 (S001): TODO: type description here.
        interchangesender_2 (S002): TODO: type description here.
        interchangerecipient_3 (S003): TODO: type description here.
        dateandtimeofpreparation_4 (S004): TODO: type description here.
        interchange_control_reference_5 (string): TODO: type description
            here.
        recipientsreferencepassworddetails_6 (S005): TODO: type description
            here.
        application_reference_7 (string): TODO: type description here.
        processing_priority_code_8 (string): TODO: type description here.
        acknowledgement_request_9 (string): TODO: type description here.
        interchange_agreement_identifier_10 (string): TODO: type description
            here.
        test_indicator_11 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "syntaxidentifier_1":'SYNTAXIDENTIFIER_1',
        "interchangesender_2":'INTERCHANGESENDER_2',
        "interchangerecipient_3":'INTERCHANGERECIPIENT_3',
        "dateandtimeofpreparation_4":'DATEANDTIMEOFPREPARATION_4',
        "interchange_control_reference_5":'InterchangeControlReference_5',
        "recipientsreferencepassworddetails_6":'RECIPIENTSREFERENCEPASSWORDDETAILS_6',
        "application_reference_7":'ApplicationReference_7',
        "processing_priority_code_8":'ProcessingPriorityCode_8',
        "acknowledgement_request_9":'AcknowledgementRequest_9',
        "interchange_agreement_identifier_10":'InterchangeAgreementIdentifier_10',
        "test_indicator_11":'TestIndicator_11'
    }

    def __init__(self,
                 syntaxidentifier_1=None,
                 interchangesender_2=None,
                 interchangerecipient_3=None,
                 dateandtimeofpreparation_4=None,
                 interchange_control_reference_5=None,
                 recipientsreferencepassworddetails_6=None,
                 application_reference_7=None,
                 processing_priority_code_8=None,
                 acknowledgement_request_9=None,
                 interchange_agreement_identifier_10=None,
                 test_indicator_11=None):
        """Constructor for the UNB class"""

        # Initialize members of the class
        self.syntaxidentifier_1 = syntaxidentifier_1
        self.interchangesender_2 = interchangesender_2
        self.interchangerecipient_3 = interchangerecipient_3
        self.dateandtimeofpreparation_4 = dateandtimeofpreparation_4
        self.interchange_control_reference_5 = interchange_control_reference_5
        self.recipientsreferencepassworddetails_6 = recipientsreferencepassworddetails_6
        self.application_reference_7 = application_reference_7
        self.processing_priority_code_8 = processing_priority_code_8
        self.acknowledgement_request_9 = acknowledgement_request_9
        self.interchange_agreement_identifier_10 = interchange_agreement_identifier_10
        self.test_indicator_11 = test_indicator_11


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
        syntaxidentifier_1 = edinationapi.models.s_001.S001.from_dictionary(dictionary.get('SYNTAXIDENTIFIER_1')) if dictionary.get('SYNTAXIDENTIFIER_1') else None
        interchangesender_2 = edinationapi.models.s_002.S002.from_dictionary(dictionary.get('INTERCHANGESENDER_2')) if dictionary.get('INTERCHANGESENDER_2') else None
        interchangerecipient_3 = edinationapi.models.s_003.S003.from_dictionary(dictionary.get('INTERCHANGERECIPIENT_3')) if dictionary.get('INTERCHANGERECIPIENT_3') else None
        dateandtimeofpreparation_4 = edinationapi.models.s_004.S004.from_dictionary(dictionary.get('DATEANDTIMEOFPREPARATION_4')) if dictionary.get('DATEANDTIMEOFPREPARATION_4') else None
        interchange_control_reference_5 = dictionary.get('InterchangeControlReference_5')
        recipientsreferencepassworddetails_6 = edinationapi.models.s_005.S005.from_dictionary(dictionary.get('RECIPIENTSREFERENCEPASSWORDDETAILS_6')) if dictionary.get('RECIPIENTSREFERENCEPASSWORDDETAILS_6') else None
        application_reference_7 = dictionary.get('ApplicationReference_7')
        processing_priority_code_8 = dictionary.get('ProcessingPriorityCode_8')
        acknowledgement_request_9 = dictionary.get('AcknowledgementRequest_9')
        interchange_agreement_identifier_10 = dictionary.get('InterchangeAgreementIdentifier_10')
        test_indicator_11 = dictionary.get('TestIndicator_11')

        # Return an object of this model
        return cls(syntaxidentifier_1,
                   interchangesender_2,
                   interchangerecipient_3,
                   dateandtimeofpreparation_4,
                   interchange_control_reference_5,
                   recipientsreferencepassworddetails_6,
                   application_reference_7,
                   processing_priority_code_8,
                   acknowledgement_request_9,
                   interchange_agreement_identifier_10,
                   test_indicator_11)


