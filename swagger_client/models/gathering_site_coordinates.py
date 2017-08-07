# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GatheringSiteCoordinates(object):
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
        'longitude_decimal': 'float',
        'latitude_decimal': 'float',
        'grid_cell_system': 'str',
        'grid_latitude_decimal': 'float',
        'grid_longitude_decimal': 'float',
        'grid_cell_code': 'str',
        'grid_qualifier': 'str',
        'geo_shape': 'Point'
    }

    attribute_map = {
        'longitude_decimal': 'longitudeDecimal',
        'latitude_decimal': 'latitudeDecimal',
        'grid_cell_system': 'gridCellSystem',
        'grid_latitude_decimal': 'gridLatitudeDecimal',
        'grid_longitude_decimal': 'gridLongitudeDecimal',
        'grid_cell_code': 'gridCellCode',
        'grid_qualifier': 'gridQualifier',
        'geo_shape': 'geoShape'
    }

    def __init__(self, longitude_decimal=None, latitude_decimal=None, grid_cell_system=None, grid_latitude_decimal=None, grid_longitude_decimal=None, grid_cell_code=None, grid_qualifier=None, geo_shape=None):
        """
        GatheringSiteCoordinates - a model defined in Swagger
        """

        self._longitude_decimal = None
        self._latitude_decimal = None
        self._grid_cell_system = None
        self._grid_latitude_decimal = None
        self._grid_longitude_decimal = None
        self._grid_cell_code = None
        self._grid_qualifier = None
        self._geo_shape = None
        self.discriminator = None

        if longitude_decimal is not None:
          self.longitude_decimal = longitude_decimal
        if latitude_decimal is not None:
          self.latitude_decimal = latitude_decimal
        if grid_cell_system is not None:
          self.grid_cell_system = grid_cell_system
        if grid_latitude_decimal is not None:
          self.grid_latitude_decimal = grid_latitude_decimal
        if grid_longitude_decimal is not None:
          self.grid_longitude_decimal = grid_longitude_decimal
        if grid_cell_code is not None:
          self.grid_cell_code = grid_cell_code
        if grid_qualifier is not None:
          self.grid_qualifier = grid_qualifier
        if geo_shape is not None:
          self.geo_shape = geo_shape

    @property
    def longitude_decimal(self):
        """
        Gets the longitude_decimal of this GatheringSiteCoordinates.

        :return: The longitude_decimal of this GatheringSiteCoordinates.
        :rtype: float
        """
        return self._longitude_decimal

    @longitude_decimal.setter
    def longitude_decimal(self, longitude_decimal):
        """
        Sets the longitude_decimal of this GatheringSiteCoordinates.

        :param longitude_decimal: The longitude_decimal of this GatheringSiteCoordinates.
        :type: float
        """

        self._longitude_decimal = longitude_decimal

    @property
    def latitude_decimal(self):
        """
        Gets the latitude_decimal of this GatheringSiteCoordinates.

        :return: The latitude_decimal of this GatheringSiteCoordinates.
        :rtype: float
        """
        return self._latitude_decimal

    @latitude_decimal.setter
    def latitude_decimal(self, latitude_decimal):
        """
        Sets the latitude_decimal of this GatheringSiteCoordinates.

        :param latitude_decimal: The latitude_decimal of this GatheringSiteCoordinates.
        :type: float
        """

        self._latitude_decimal = latitude_decimal

    @property
    def grid_cell_system(self):
        """
        Gets the grid_cell_system of this GatheringSiteCoordinates.

        :return: The grid_cell_system of this GatheringSiteCoordinates.
        :rtype: str
        """
        return self._grid_cell_system

    @grid_cell_system.setter
    def grid_cell_system(self, grid_cell_system):
        """
        Sets the grid_cell_system of this GatheringSiteCoordinates.

        :param grid_cell_system: The grid_cell_system of this GatheringSiteCoordinates.
        :type: str
        """

        self._grid_cell_system = grid_cell_system

    @property
    def grid_latitude_decimal(self):
        """
        Gets the grid_latitude_decimal of this GatheringSiteCoordinates.

        :return: The grid_latitude_decimal of this GatheringSiteCoordinates.
        :rtype: float
        """
        return self._grid_latitude_decimal

    @grid_latitude_decimal.setter
    def grid_latitude_decimal(self, grid_latitude_decimal):
        """
        Sets the grid_latitude_decimal of this GatheringSiteCoordinates.

        :param grid_latitude_decimal: The grid_latitude_decimal of this GatheringSiteCoordinates.
        :type: float
        """

        self._grid_latitude_decimal = grid_latitude_decimal

    @property
    def grid_longitude_decimal(self):
        """
        Gets the grid_longitude_decimal of this GatheringSiteCoordinates.

        :return: The grid_longitude_decimal of this GatheringSiteCoordinates.
        :rtype: float
        """
        return self._grid_longitude_decimal

    @grid_longitude_decimal.setter
    def grid_longitude_decimal(self, grid_longitude_decimal):
        """
        Sets the grid_longitude_decimal of this GatheringSiteCoordinates.

        :param grid_longitude_decimal: The grid_longitude_decimal of this GatheringSiteCoordinates.
        :type: float
        """

        self._grid_longitude_decimal = grid_longitude_decimal

    @property
    def grid_cell_code(self):
        """
        Gets the grid_cell_code of this GatheringSiteCoordinates.

        :return: The grid_cell_code of this GatheringSiteCoordinates.
        :rtype: str
        """
        return self._grid_cell_code

    @grid_cell_code.setter
    def grid_cell_code(self, grid_cell_code):
        """
        Sets the grid_cell_code of this GatheringSiteCoordinates.

        :param grid_cell_code: The grid_cell_code of this GatheringSiteCoordinates.
        :type: str
        """

        self._grid_cell_code = grid_cell_code

    @property
    def grid_qualifier(self):
        """
        Gets the grid_qualifier of this GatheringSiteCoordinates.

        :return: The grid_qualifier of this GatheringSiteCoordinates.
        :rtype: str
        """
        return self._grid_qualifier

    @grid_qualifier.setter
    def grid_qualifier(self, grid_qualifier):
        """
        Sets the grid_qualifier of this GatheringSiteCoordinates.

        :param grid_qualifier: The grid_qualifier of this GatheringSiteCoordinates.
        :type: str
        """

        self._grid_qualifier = grid_qualifier

    @property
    def geo_shape(self):
        """
        Gets the geo_shape of this GatheringSiteCoordinates.

        :return: The geo_shape of this GatheringSiteCoordinates.
        :rtype: Point
        """
        return self._geo_shape

    @geo_shape.setter
    def geo_shape(self, geo_shape):
        """
        Sets the geo_shape of this GatheringSiteCoordinates.

        :param geo_shape: The geo_shape of this GatheringSiteCoordinates.
        :type: Point
        """

        self._geo_shape = geo_shape

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
        if not isinstance(other, GatheringSiteCoordinates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
