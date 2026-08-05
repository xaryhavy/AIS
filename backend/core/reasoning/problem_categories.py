"""
AIS Core
Problem Categories

Defines the standard business problem categories
recognized by AIS.

Author: Fabian Ezenwajiaku
Project: AIS
"""

from enum import Enum


class ProblemCategory(Enum):
    """
    Standard business problem categories.
    """

    MARKETING = "Marketing"

    SALES = "Sales"

    FINANCE = "Finance"

    HR = "Human Resources"

    OPERATIONS = "Operations"

    PRODUCT = "Product"

    CUSTOMER_SUPPORT = "Customer Support"

    STRATEGY = "Strategy"

    TECHNOLOGY = "Technology"

    UNKNOWN = "Unknown"