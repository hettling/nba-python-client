# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MultiMediaGatheringEvent(object):
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
        'project_title': 'str',
        'world_region': 'str',
        'continent': 'str',
        'country': 'str',
        'iso3166_code': 'str',
        'province_state': 'str',
        'island': 'str',
        'locality': 'str',
        'city': 'str',
        'sublocality': 'str',
        'locality_text': 'str',
        'date_time_begin': 'datetime',
        'date_time_end': 'datetime',
        'method': 'str',
        'altitude': 'str',
        'altitude_unif_of_measurement': 'str',
        'depth': 'str',
        'depth_unit_of_measurement': 'str',
        'gathering_persons': 'list[Person]',
        'gathering_organizations': 'list[Organization]',
        'site_coordinates': 'list[GatheringSiteCoordinates]',
        'chrono_stratigraphy': 'list[ChronoStratigraphy]',
        'litho_stratigraphy': 'list[LithoStratigraphy]',
        'iptc': 'Iptc4xmpExt',
        'bio_stratigraphic': 'list[BioStratigraphy]'
    }

    attribute_map = {
        'project_title': 'projectTitle',
        'world_region': 'worldRegion',
        'continent': 'continent',
        'country': 'country',
        'iso3166_code': 'iso3166Code',
        'province_state': 'provinceState',
        'island': 'island',
        'locality': 'locality',
        'city': 'city',
        'sublocality': 'sublocality',
        'locality_text': 'localityText',
        'date_time_begin': 'dateTimeBegin',
        'date_time_end': 'dateTimeEnd',
        'method': 'method',
        'altitude': 'altitude',
        'altitude_unif_of_measurement': 'altitudeUnifOfMeasurement',
        'depth': 'depth',
        'depth_unit_of_measurement': 'depthUnitOfMeasurement',
        'gathering_persons': 'gatheringPersons',
        'gathering_organizations': 'gatheringOrganizations',
        'site_coordinates': 'siteCoordinates',
        'chrono_stratigraphy': 'chronoStratigraphy',
        'litho_stratigraphy': 'lithoStratigraphy',
        'iptc': 'iptc',
        'bio_stratigraphic': 'bioStratigraphic'
    }

    def __init__(self, project_title=None, world_region=None, continent=None, country=None, iso3166_code=None, province_state=None, island=None, locality=None, city=None, sublocality=None, locality_text=None, date_time_begin=None, date_time_end=None, method=None, altitude=None, altitude_unif_of_measurement=None, depth=None, depth_unit_of_measurement=None, gathering_persons=None, gathering_organizations=None, site_coordinates=None, chrono_stratigraphy=None, litho_stratigraphy=None, iptc=None, bio_stratigraphic=None):
        """
        MultiMediaGatheringEvent - a model defined in Swagger
        """

        self._project_title = None
        self._world_region = None
        self._continent = None
        self._country = None
        self._iso3166_code = None
        self._province_state = None
        self._island = None
        self._locality = None
        self._city = None
        self._sublocality = None
        self._locality_text = None
        self._date_time_begin = None
        self._date_time_end = None
        self._method = None
        self._altitude = None
        self._altitude_unif_of_measurement = None
        self._depth = None
        self._depth_unit_of_measurement = None
        self._gathering_persons = None
        self._gathering_organizations = None
        self._site_coordinates = None
        self._chrono_stratigraphy = None
        self._litho_stratigraphy = None
        self._iptc = None
        self._bio_stratigraphic = None
        self.discriminator = None

        if project_title is not None:
          self.project_title = project_title
        if world_region is not None:
          self.world_region = world_region
        if continent is not None:
          self.continent = continent
        if country is not None:
          self.country = country
        if iso3166_code is not None:
          self.iso3166_code = iso3166_code
        if province_state is not None:
          self.province_state = province_state
        if island is not None:
          self.island = island
        if locality is not None:
          self.locality = locality
        if city is not None:
          self.city = city
        if sublocality is not None:
          self.sublocality = sublocality
        if locality_text is not None:
          self.locality_text = locality_text
        if date_time_begin is not None:
          self.date_time_begin = date_time_begin
        if date_time_end is not None:
          self.date_time_end = date_time_end
        if method is not None:
          self.method = method
        if altitude is not None:
          self.altitude = altitude
        if altitude_unif_of_measurement is not None:
          self.altitude_unif_of_measurement = altitude_unif_of_measurement
        if depth is not None:
          self.depth = depth
        if depth_unit_of_measurement is not None:
          self.depth_unit_of_measurement = depth_unit_of_measurement
        if gathering_persons is not None:
          self.gathering_persons = gathering_persons
        if gathering_organizations is not None:
          self.gathering_organizations = gathering_organizations
        if site_coordinates is not None:
          self.site_coordinates = site_coordinates
        if chrono_stratigraphy is not None:
          self.chrono_stratigraphy = chrono_stratigraphy
        if litho_stratigraphy is not None:
          self.litho_stratigraphy = litho_stratigraphy
        if iptc is not None:
          self.iptc = iptc
        if bio_stratigraphic is not None:
          self.bio_stratigraphic = bio_stratigraphic

    @property
    def project_title(self):
        """
        Gets the project_title of this MultiMediaGatheringEvent.

        :return: The project_title of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._project_title

    @project_title.setter
    def project_title(self, project_title):
        """
        Sets the project_title of this MultiMediaGatheringEvent.

        :param project_title: The project_title of this MultiMediaGatheringEvent.
        :type: str
        """

        self._project_title = project_title

    @property
    def world_region(self):
        """
        Gets the world_region of this MultiMediaGatheringEvent.

        :return: The world_region of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._world_region

    @world_region.setter
    def world_region(self, world_region):
        """
        Sets the world_region of this MultiMediaGatheringEvent.

        :param world_region: The world_region of this MultiMediaGatheringEvent.
        :type: str
        """

        self._world_region = world_region

    @property
    def continent(self):
        """
        Gets the continent of this MultiMediaGatheringEvent.

        :return: The continent of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._continent

    @continent.setter
    def continent(self, continent):
        """
        Sets the continent of this MultiMediaGatheringEvent.

        :param continent: The continent of this MultiMediaGatheringEvent.
        :type: str
        """

        self._continent = continent

    @property
    def country(self):
        """
        Gets the country of this MultiMediaGatheringEvent.

        :return: The country of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this MultiMediaGatheringEvent.

        :param country: The country of this MultiMediaGatheringEvent.
        :type: str
        """

        self._country = country

    @property
    def iso3166_code(self):
        """
        Gets the iso3166_code of this MultiMediaGatheringEvent.

        :return: The iso3166_code of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._iso3166_code

    @iso3166_code.setter
    def iso3166_code(self, iso3166_code):
        """
        Sets the iso3166_code of this MultiMediaGatheringEvent.

        :param iso3166_code: The iso3166_code of this MultiMediaGatheringEvent.
        :type: str
        """

        self._iso3166_code = iso3166_code

    @property
    def province_state(self):
        """
        Gets the province_state of this MultiMediaGatheringEvent.

        :return: The province_state of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._province_state

    @province_state.setter
    def province_state(self, province_state):
        """
        Sets the province_state of this MultiMediaGatheringEvent.

        :param province_state: The province_state of this MultiMediaGatheringEvent.
        :type: str
        """

        self._province_state = province_state

    @property
    def island(self):
        """
        Gets the island of this MultiMediaGatheringEvent.

        :return: The island of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._island

    @island.setter
    def island(self, island):
        """
        Sets the island of this MultiMediaGatheringEvent.

        :param island: The island of this MultiMediaGatheringEvent.
        :type: str
        """

        self._island = island

    @property
    def locality(self):
        """
        Gets the locality of this MultiMediaGatheringEvent.

        :return: The locality of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this MultiMediaGatheringEvent.

        :param locality: The locality of this MultiMediaGatheringEvent.
        :type: str
        """

        self._locality = locality

    @property
    def city(self):
        """
        Gets the city of this MultiMediaGatheringEvent.

        :return: The city of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this MultiMediaGatheringEvent.

        :param city: The city of this MultiMediaGatheringEvent.
        :type: str
        """

        self._city = city

    @property
    def sublocality(self):
        """
        Gets the sublocality of this MultiMediaGatheringEvent.

        :return: The sublocality of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._sublocality

    @sublocality.setter
    def sublocality(self, sublocality):
        """
        Sets the sublocality of this MultiMediaGatheringEvent.

        :param sublocality: The sublocality of this MultiMediaGatheringEvent.
        :type: str
        """

        self._sublocality = sublocality

    @property
    def locality_text(self):
        """
        Gets the locality_text of this MultiMediaGatheringEvent.

        :return: The locality_text of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._locality_text

    @locality_text.setter
    def locality_text(self, locality_text):
        """
        Sets the locality_text of this MultiMediaGatheringEvent.

        :param locality_text: The locality_text of this MultiMediaGatheringEvent.
        :type: str
        """

        self._locality_text = locality_text

    @property
    def date_time_begin(self):
        """
        Gets the date_time_begin of this MultiMediaGatheringEvent.

        :return: The date_time_begin of this MultiMediaGatheringEvent.
        :rtype: datetime
        """
        return self._date_time_begin

    @date_time_begin.setter
    def date_time_begin(self, date_time_begin):
        """
        Sets the date_time_begin of this MultiMediaGatheringEvent.

        :param date_time_begin: The date_time_begin of this MultiMediaGatheringEvent.
        :type: datetime
        """

        self._date_time_begin = date_time_begin

    @property
    def date_time_end(self):
        """
        Gets the date_time_end of this MultiMediaGatheringEvent.

        :return: The date_time_end of this MultiMediaGatheringEvent.
        :rtype: datetime
        """
        return self._date_time_end

    @date_time_end.setter
    def date_time_end(self, date_time_end):
        """
        Sets the date_time_end of this MultiMediaGatheringEvent.

        :param date_time_end: The date_time_end of this MultiMediaGatheringEvent.
        :type: datetime
        """

        self._date_time_end = date_time_end

    @property
    def method(self):
        """
        Gets the method of this MultiMediaGatheringEvent.

        :return: The method of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this MultiMediaGatheringEvent.

        :param method: The method of this MultiMediaGatheringEvent.
        :type: str
        """

        self._method = method

    @property
    def altitude(self):
        """
        Gets the altitude of this MultiMediaGatheringEvent.

        :return: The altitude of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """
        Sets the altitude of this MultiMediaGatheringEvent.

        :param altitude: The altitude of this MultiMediaGatheringEvent.
        :type: str
        """

        self._altitude = altitude

    @property
    def altitude_unif_of_measurement(self):
        """
        Gets the altitude_unif_of_measurement of this MultiMediaGatheringEvent.

        :return: The altitude_unif_of_measurement of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._altitude_unif_of_measurement

    @altitude_unif_of_measurement.setter
    def altitude_unif_of_measurement(self, altitude_unif_of_measurement):
        """
        Sets the altitude_unif_of_measurement of this MultiMediaGatheringEvent.

        :param altitude_unif_of_measurement: The altitude_unif_of_measurement of this MultiMediaGatheringEvent.
        :type: str
        """

        self._altitude_unif_of_measurement = altitude_unif_of_measurement

    @property
    def depth(self):
        """
        Gets the depth of this MultiMediaGatheringEvent.

        :return: The depth of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth of this MultiMediaGatheringEvent.

        :param depth: The depth of this MultiMediaGatheringEvent.
        :type: str
        """

        self._depth = depth

    @property
    def depth_unit_of_measurement(self):
        """
        Gets the depth_unit_of_measurement of this MultiMediaGatheringEvent.

        :return: The depth_unit_of_measurement of this MultiMediaGatheringEvent.
        :rtype: str
        """
        return self._depth_unit_of_measurement

    @depth_unit_of_measurement.setter
    def depth_unit_of_measurement(self, depth_unit_of_measurement):
        """
        Sets the depth_unit_of_measurement of this MultiMediaGatheringEvent.

        :param depth_unit_of_measurement: The depth_unit_of_measurement of this MultiMediaGatheringEvent.
        :type: str
        """

        self._depth_unit_of_measurement = depth_unit_of_measurement

    @property
    def gathering_persons(self):
        """
        Gets the gathering_persons of this MultiMediaGatheringEvent.

        :return: The gathering_persons of this MultiMediaGatheringEvent.
        :rtype: list[Person]
        """
        return self._gathering_persons

    @gathering_persons.setter
    def gathering_persons(self, gathering_persons):
        """
        Sets the gathering_persons of this MultiMediaGatheringEvent.

        :param gathering_persons: The gathering_persons of this MultiMediaGatheringEvent.
        :type: list[Person]
        """

        self._gathering_persons = gathering_persons

    @property
    def gathering_organizations(self):
        """
        Gets the gathering_organizations of this MultiMediaGatheringEvent.

        :return: The gathering_organizations of this MultiMediaGatheringEvent.
        :rtype: list[Organization]
        """
        return self._gathering_organizations

    @gathering_organizations.setter
    def gathering_organizations(self, gathering_organizations):
        """
        Sets the gathering_organizations of this MultiMediaGatheringEvent.

        :param gathering_organizations: The gathering_organizations of this MultiMediaGatheringEvent.
        :type: list[Organization]
        """

        self._gathering_organizations = gathering_organizations

    @property
    def site_coordinates(self):
        """
        Gets the site_coordinates of this MultiMediaGatheringEvent.

        :return: The site_coordinates of this MultiMediaGatheringEvent.
        :rtype: list[GatheringSiteCoordinates]
        """
        return self._site_coordinates

    @site_coordinates.setter
    def site_coordinates(self, site_coordinates):
        """
        Sets the site_coordinates of this MultiMediaGatheringEvent.

        :param site_coordinates: The site_coordinates of this MultiMediaGatheringEvent.
        :type: list[GatheringSiteCoordinates]
        """

        self._site_coordinates = site_coordinates

    @property
    def chrono_stratigraphy(self):
        """
        Gets the chrono_stratigraphy of this MultiMediaGatheringEvent.

        :return: The chrono_stratigraphy of this MultiMediaGatheringEvent.
        :rtype: list[ChronoStratigraphy]
        """
        return self._chrono_stratigraphy

    @chrono_stratigraphy.setter
    def chrono_stratigraphy(self, chrono_stratigraphy):
        """
        Sets the chrono_stratigraphy of this MultiMediaGatheringEvent.

        :param chrono_stratigraphy: The chrono_stratigraphy of this MultiMediaGatheringEvent.
        :type: list[ChronoStratigraphy]
        """

        self._chrono_stratigraphy = chrono_stratigraphy

    @property
    def litho_stratigraphy(self):
        """
        Gets the litho_stratigraphy of this MultiMediaGatheringEvent.

        :return: The litho_stratigraphy of this MultiMediaGatheringEvent.
        :rtype: list[LithoStratigraphy]
        """
        return self._litho_stratigraphy

    @litho_stratigraphy.setter
    def litho_stratigraphy(self, litho_stratigraphy):
        """
        Sets the litho_stratigraphy of this MultiMediaGatheringEvent.

        :param litho_stratigraphy: The litho_stratigraphy of this MultiMediaGatheringEvent.
        :type: list[LithoStratigraphy]
        """

        self._litho_stratigraphy = litho_stratigraphy

    @property
    def iptc(self):
        """
        Gets the iptc of this MultiMediaGatheringEvent.

        :return: The iptc of this MultiMediaGatheringEvent.
        :rtype: Iptc4xmpExt
        """
        return self._iptc

    @iptc.setter
    def iptc(self, iptc):
        """
        Sets the iptc of this MultiMediaGatheringEvent.

        :param iptc: The iptc of this MultiMediaGatheringEvent.
        :type: Iptc4xmpExt
        """

        self._iptc = iptc

    @property
    def bio_stratigraphic(self):
        """
        Gets the bio_stratigraphic of this MultiMediaGatheringEvent.

        :return: The bio_stratigraphic of this MultiMediaGatheringEvent.
        :rtype: list[BioStratigraphy]
        """
        return self._bio_stratigraphic

    @bio_stratigraphic.setter
    def bio_stratigraphic(self, bio_stratigraphic):
        """
        Sets the bio_stratigraphic of this MultiMediaGatheringEvent.

        :param bio_stratigraphic: The bio_stratigraphic of this MultiMediaGatheringEvent.
        :type: list[BioStratigraphy]
        """

        self._bio_stratigraphic = bio_stratigraphic

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
        if not isinstance(other, MultiMediaGatheringEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other