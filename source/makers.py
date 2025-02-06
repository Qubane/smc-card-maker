"""
Card makers
"""


from typing import Any


class CardMaker:
    """
    Base card maker namespace
    """

    @staticmethod
    def make_card(data: Any) -> Any:
        """
        Makes a card
        """


class QCPUCardMaker(CardMaker):
    """
    Quantum CPU architecture card maker
    """

    @staticmethod
    def make_card(data: bytes) -> Any:
        """
        Makes a card for QCPU's
        """
