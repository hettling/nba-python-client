# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VernacularName(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'language': 'str',
        'preferred': 'bool',
        'references': 'list[Reference]',
        'experts': 'list[Expert]'
    }

    attribute_map = {
        'name': 'name',
        'language': 'language',
        'preferred': 'preferred',
        'references': 'references',
        'experts': 'experts'
    }

    def __init__(self, name=None, language=None, preferred=None, references=None, experts=None):
        """
        VernacularName - a model defined in Swagger
        """

        self._name = None
        self._language = None
        self._preferred = None
        self._references = None
        self._experts = None
        self.discriminator = None

        if name is not None:
          self.name = name
        if language is not None:
          self.language = language
        if preferred is not None:
          self.preferred = preferred
        if references is not None:
          self.references = references
        if experts is not None:
          self.experts = experts

    @property
    def name(self):
        """
        Gets the name of this VernacularName.

        :return: The name of this VernacularName.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VernacularName.

        :param name: The name of this VernacularName.
        :type: str
        """

        self._name = name

    @property
    def language(self):
        """
        Gets the language of this VernacularName.

        :return: The language of this VernacularName.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this VernacularName.

        :param language: The language of this VernacularName.
        :type: str
        """

        self._language = language

    @property
    def preferred(self):
        """
        Gets the preferred of this VernacularName.

        :return: The preferred of this VernacularName.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """
        Sets the preferred of this VernacularName.

        :param preferred: The preferred of this VernacularName.
        :type: bool
        """

        self._preferred = preferred

    @property
    def references(self):
        """
        Gets the references of this VernacularName.

        :return: The references of this VernacularName.
        :rtype: list[Reference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """
        Sets the references of this VernacularName.

        :param references: The references of this VernacularName.
        :type: list[Reference]
        """

        self._references = references

    @property
    def experts(self):
        """
        Gets the experts of this VernacularName.

        :return: The experts of this VernacularName.
        :rtype: list[Expert]
        """
        return self._experts

    @experts.setter
    def experts(self, experts):
        """
        Sets the experts of this VernacularName.

        :param experts: The experts of this VernacularName.
        :type: list[Expert]
        """

        self._experts = experts

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VernacularName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
