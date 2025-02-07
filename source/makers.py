"""
Card makers
"""


from math import ceil
from io import BytesIO
from source.classes import Colors
from source.blueprint import Block, Blueprint


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

        # magic values
        mask_size = 5  # 5 bits
        mask = 2**mask_size - 1  # 5 bits per color
        splits = ceil(24 / 5)  # 24 bit instruction size divided by size of mask in bits

        blueprint = Blueprint()
        for instruction_idx, instruction in enumerate(instructions):
            i_value = int.from_bytes(instruction)
            # shift the mask around the binary value, and cut out the part that is needed
            colors = [(i_value & (mask << (x * mask_size))) >> (x * mask_size) for x in range(splits-1, -1, -1)]

            # go through colors and add them as blocks
            for color_idx, color in enumerate(colors):
                # make color
                str_color = Colors.ALL[color]

                # make block
                block = Block((color_idx, instruction_idx, 0), "plastic", str_color)

                # add blocks to blueprint
                blueprint.add_block(block)

        return blueprint.json()


class MCPU20CardMaker(CardMaker):
    """
    @Mureccell's CPU 2.0 CardMaker
    """

    @staticmethod
    def make_card(data: bytes) -> dict:
        """
        Makes a card for @Mureccell's CPU 2.0
        """

        # make stream
        stream = BytesIO(data)

        # read instructions
        instructions: list[int] = []
        while instruction := stream.read(32):
            stream.read(2)  # skip '\r\n'
            value = int(instruction, 2)  # convert string value to int
            instructions.append(value)

        # make and return card
        return MCPU20CardMaker._make_card(instructions)

    @staticmethod
    def _make_card(instructions: list[int]) -> dict:
        """
        Makes a program card for @Mureccell's CPU
        :param instructions: list of int instructions
        :return: json object card blueprint
        """
