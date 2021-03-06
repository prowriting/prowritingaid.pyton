# coding: utf-8

"""
    ProWritingAid API V2

    Official ProWritingAid API Version 2

    OpenAPI spec version: v2
    Contact: hello@prowritingaid.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AsyncResponseSummaryAnalysisResponse(object):
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
        'task_id': 'str',
        'result': 'SummaryAnalysisResponse'
    }

    attribute_map = {
        'task_id': 'TaskId',
        'result': 'Result'
    }

    def __init__(self, task_id=None, result=None):
        """
        AsyncResponseSummaryAnalysisResponse - a model defined in Swagger
        """

        self._task_id = None
        self._result = None

        if task_id is not None:
          self.task_id = task_id
        if result is not None:
          self.result = result

    @property
    def task_id(self):
        """
        Gets the task_id of this AsyncResponseSummaryAnalysisResponse.
        Async task Id. Empty or null if task was processed synchronously

        :return: The task_id of this AsyncResponseSummaryAnalysisResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """
        Sets the task_id of this AsyncResponseSummaryAnalysisResponse.
        Async task Id. Empty or null if task was processed synchronously

        :param task_id: The task_id of this AsyncResponseSummaryAnalysisResponse.
        :type: str
        """

        self._task_id = task_id

    @property
    def result(self):
        """
        Gets the result of this AsyncResponseSummaryAnalysisResponse.
        Actual response

        :return: The result of this AsyncResponseSummaryAnalysisResponse.
        :rtype: SummaryAnalysisResponse
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this AsyncResponseSummaryAnalysisResponse.
        Actual response

        :param result: The result of this AsyncResponseSummaryAnalysisResponse.
        :type: SummaryAnalysisResponse
        """

        self._result = result

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
        if not isinstance(other, AsyncResponseSummaryAnalysisResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
