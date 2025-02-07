"""
Application class
"""


import os
import json
import argparse
from source.makers import *


class Application:
    """
    Application class
    """

    def __init__(self):
        self.args: argparse.Namespace | None = None

    def parse_args(self):
        """
        Parse CLI arguments
        """

        # make parser
        parser = argparse.ArgumentParser(prog="SMC Card Maker", description="Scrap Mechanic Computer Card Maker")

        # add arguments
        parser.add_argument("-i", "--input",
                            help="input file",
                            required=True)
        parser.add_argument("-t", "--type",
                            help="input file type",
                            choices=["QCPU", "MCPU2.0"],
                            required=True)
        parser.add_argument("--prettify",
                            help="write 'blueprint.json' with indents",
                            action="store_true",
                            default=False)

        # parse
        self.args = parser.parse_args()

    @staticmethod
    def ensure_directories():
        """
        Ensures some of the directories exist
        """

        if not os.path.isdir("blueprints"):
            os.mkdir("blueprints")

    def run(self):
        """
        Runs the application
        """

        # ensure directories
        self.ensure_directories()

        # parse CLI arguments
        self.parse_args()

        # read input file
        with open(self.args.input, "rb") as file:
            data = file.read()

        # make blueprint
        if self.args.type == "QCPU":
            blueprint = QCPUCardMaker.make_card(data)
        elif self.args.type == "MCPU2.0":
            blueprint = MCPU20CardMaker.make_card(data)
        else:
            raise Exception

        # make blueprint
        indents = 2 if self.args.prettify else None
        with open("blueprints/blueprint.json", "w", encoding="ASCII") as file:
            file.write(json.dumps(blueprint, indent=indents))
