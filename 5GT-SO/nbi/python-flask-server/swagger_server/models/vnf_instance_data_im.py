# Author: Jordi Baranda
# Copyright (C) 2019 CTTC/CERCA
# License: To be defined. Currently use is restricted to partners of the 5G-Transformer project,
#          http://5g-transformer.eu/, no use or redistribution of any kind outside the 5G-Transformer project is
#          allowed.
# Disclaimer: this software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class VnfInstanceDataIm(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, vnf_instance_id: str=None, vnf_profile_id: str=None):  # noqa: E501
        """VnfInstanceDataIm - a model defined in Swagger

        :param vnf_instance_id: The vnf_instance_id of this VnfInstanceDataIm.  # noqa: E501
        :type vnf_instance_id: str
        :param vnf_profile_id: The vnf_profile_id of this VnfInstanceDataIm.  # noqa: E501
        :type vnf_profile_id: str
        """
        self.swagger_types = {
            "vnf_instance_id": str,
            "vnf_profile_id": str
        }

        self.attribute_map = {
            "vnf_instance_id": "vnfInstanceId",
            "vnf_profile_id": "vnfProfileId"
        }

        self._vnf_instance_id = vnf_instance_id
        self._vnf_profile_id = vnf_profile_id

    @classmethod
    def from_dict(cls, dikt) -> "VnfInstanceDataIm":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VnfInstanceData_im of this VnfInstanceDataIm.  # noqa: E501
        :rtype: VnfInstanceDataIm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vnf_instance_id(self) -> str:
        """Gets the vnf_instance_id of this VnfInstanceDataIm.


        :return: The vnf_instance_id of this VnfInstanceDataIm.
        :rtype: str
        """
        return self._vnf_instance_id

    @vnf_instance_id.setter
    def vnf_instance_id(self, vnf_instance_id: str):
        """Sets the vnf_instance_id of this VnfInstanceDataIm.


        :param vnf_instance_id: The vnf_instance_id of this VnfInstanceDataIm.
        :type vnf_instance_id: str
        """
        if vnf_instance_id is None:
            raise ValueError("Invalid value for `vnf_instance_id`, must not be `None`")  # noqa: E501

        self._vnf_instance_id = vnf_instance_id

    @property
    def vnf_profile_id(self) -> str:
        """Gets the vnf_profile_id of this VnfInstanceDataIm.


        :return: The vnf_profile_id of this VnfInstanceDataIm.
        :rtype: str
        """
        return self._vnf_profile_id

    @vnf_profile_id.setter
    def vnf_profile_id(self, vnf_profile_id: str):
        """Sets the vnf_profile_id of this VnfInstanceDataIm.


        :param vnf_profile_id: The vnf_profile_id of this VnfInstanceDataIm.
        :type vnf_profile_id: str
        """

        self._vnf_profile_id = vnf_profile_id
