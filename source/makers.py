"""
Card makers
"""


from io import BytesIO


class CardMaker:
    """
    Base card maker namespace
    """

    @staticmethod
    def make_card(data: bytes) -> dict:
        """
        Makes a card
        """


class QCPUCardMaker(CardMaker):
    """
    Quantum CPU architecture card maker
    """

    @staticmethod
    def make_card(data: bytes) -> dict:
        """
        Makes a card for QCPU's
        """

        # make byte stream
        stream = BytesIO(data)

        # read namespace
        namespace: bytes = b''
        while (char := stream.read(1)) != b'\x00':
            namespace += char

        # pick offset
        if namespace == b'QT':
            offset = 4
        elif namespace == b'QM':
            offset = 3
        else:
            raise NotImplementedError

        # read instructions
        instructions: list[bytes] = []
        while word := stream.read(offset):
            instructions.append(word)

        # make and return card
        return QCPUCardMaker._make_qt_card(instructions)

    @staticmethod
    def _make_qt_card(instructions: list[bytes]) -> dict:
        """
        Makes a program card for QT CPU linage
        :param instructions: list of bytes instructions
        :return: json object card blueprint
        """


class MCPU20CardMaker(CardMaker):
    """
    @Mureccell's CPU 2.0 CardMaker
    """

    @staticmethod
    def make_card(data: bytes) -> dict:
        """
        Makes a card for @Mureccell's CPU 2.0
        """
