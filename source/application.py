"""
Application class
"""


import argparse


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
        parser.add_argument("--use-color",
                            help="output color compressed cards",
                            type=int,
                            default=0)

        # parse
        self.args = parser.parse_args()

    def run(self):
        """
        Runs the application
        """

        # parse CLI arguments
        self.parse_args()
