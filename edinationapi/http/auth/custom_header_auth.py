# -*- coding: utf-8 -*-

"""
    edinationapi

    This file was automatically generated for EdiNation by APIMATIC v2.0 ( https://apimatic.io ).
"""

from edinationapi.configuration import Configuration


class CustomHeaderAuth:

    @staticmethod
    def apply(http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which 
                authentication will be added.

        """                
        http_request.add_header("Ocp-Apim-Subscription-Key", Configuration.ocp_apim_subscription_key)
