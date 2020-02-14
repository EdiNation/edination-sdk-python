# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

from edinationapi.decorators import lazy_property
from edinationapi.configuration import Configuration
from edinationapi.controllers.edifact_controller import EdifactController
from edinationapi.controllers.edi_model_controller import EdiModelController
from edinationapi.controllers.x_12_controller import X12Controller


class EdinationapiClient(object):

    config = Configuration

    @lazy_property
    def edifact(self):
        return EdifactController()

    @lazy_property
    def edi_model(self):
        return EdiModelController()

    @lazy_property
    def x_12(self):
        return X12Controller()


    def __init__(self,
                 ocp_apim_subscription_key=None):
        if ocp_apim_subscription_key is not None:
            Configuration.ocp_apim_subscription_key = ocp_apim_subscription_key

