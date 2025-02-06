"""
Blueprint making stuff
"""


from typing import Sequence


BLUEPRINT_TEMPLATE = """
{
  "bodies": [
    {
      "childs": [
        {block_section}
      ]
    }
  ],
  "version": 4
}
"""

BLOCK_TEMPLATE = """
{
  "bounds": {
    "x": {size_x},
    "y": {size_y},
    "z": {size_z}
  },
  "color": "{color}",
  "pos": {
    "x": {pos_x},
    "y": {pos_y},
    "z": {pos_z}
  },
  "shapeId": "{block_id}",
  "xaxis": 1,
  "zaxis": 3
}
"""

BLOCKS: dict[str, str] = {
    "concrete": "a6c6ce30-dd47-4587-b475-085d55c6a3b4",
    "glass": "5f41af56-df4c-4837-9b3c-10781335757f",
    "plastic": "628b2d61-5ceb-43e9-8334-a4135566df7a"
}


class Block:
    """
    Block container class
    """

    def __init__(self, position: Sequence[int], block: str):
        self.position: Sequence[int] = position
        self.type: str = block

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]

    @property
    def z(self) -> int:
        return self.position[2]


class Blueprint:
    """
    Scrap Mechanic blueprint
    """

    def __init__(self):
        self.blocks: dict[int, dict[int, dict[int, Block]]] = dict()

    def add_block(self, block: Block) -> None:
        """
        Adds a block.
        :param block: block type
        """
