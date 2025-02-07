"""
Card makers
"""


from typing import Any


class CardMaker:
    """
    Base card maker namespace
    """

    @staticmethod
    def make_card(data: bytes) -> Any:
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


class MCPU20CardMaker(CardMaker):
    """
    @Mureccell's CPU 2.0 CardMaker
    """

    @staticmethod
    def make_card(data: bytes) -> Any:
        """
        Makes a card for @Mureccell's CPU 2.0
        """
