"""
Blueprint making stuff
"""


import json
from typing import Sequence


BLUEPRINT_TEMPLATE = """
{
  "bodies": [
    {
      "childs": [
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

    def __init__(self, position: Sequence[int], block: str, color: str):
        self.position: Sequence[int] = position
        self.color: str = color
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

        # make sure position exists
        if block.z not in self.blocks:
            self.blocks = dict()
        if block.y not in self.blocks[block.z]:
            self.blocks[block.z] = dict()
        if block.x not in self.blocks[block.z][block.y]:
            self.blocks[block.z][block.y] = dict()

        # add block
        self.blocks[block.z][block.y][block.x] = block

    def get_block(self, position: Sequence[int]) -> Block | None:
        """
        Returns a block or None for given position.
        :param position: position
        :return: Block or None
        """

        x, y, z = position

        if z not in self.blocks:
            return None
        if y not in self.blocks[z]:
            return None
        if x not in self.blocks[z][y]:
            return None
        return self.blocks[z][y][x]

    def json(self) -> dict:
        """
        Output JSON blueprint object
        """

        # append all blocks
        blocks = []
        for z in self.blocks:
            for y in self.blocks[z]:
                for x in self.blocks[z][y]:
                    block_temp = json.loads(BLOCK_TEMPLATE.format(
                        size_x=1,
                        size_y=1,
                        size_z=1,
                        pos_x=x,
                        pos_y=y,
                        pos_z=z,
                        block_id=BLOCKS[self.blocks[z][y][x].type],
                        color=self.blocks[z][y][x].color))
                    blocks.append(block_temp)

        # make blueprint body
        out = json.loads(BLUEPRINT_TEMPLATE)
        out["bodies"][0]["childs"] = out

        # return output
        return out
