"""
Blueprint making stuff
"""


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
  "color": "8D8F89",
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


class Blueprint:
    """
    Scrap Mechanic blueprint
    """

    def __init__(self):
        pass
