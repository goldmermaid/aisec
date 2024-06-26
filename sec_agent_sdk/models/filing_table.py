# coding: utf-8

"""
    cambioml-sec-agent-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FilingTable(str, Enum):
    """
    FilingTable
    """

    """
    allowed enum values
    """
    BALANCE_SHEET = 'balance-sheet'
    CASH_FLOW_STATEMENT = 'cash-flow-statement'
    INCOME_STATEMENT = 'income-statement'
    BUSINESS_SEGMENTS_AND_KPIS = "business-segments-and-kpis"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FilingTable from a JSON string"""
        return cls(json.loads(json_str))


