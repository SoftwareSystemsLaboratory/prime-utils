from argparse import ArgumentParser, HelpFormatter
from operator import attrgetter

from version_utility.main import readFile, readVersion

name: str = "PRIME"
author: str = "Software and Systems Laboratory"


class SortingHelpFormatter(HelpFormatter):
    def add_arguments(self, actions):
        actions = sorted(actions, key=attrgetter("option_strings"))
        super(SortingHelpFormatter, self).add_arguments(actions)


def version(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-v",
        "--version",
        help="Display the version of this tool",
        action="version",
        version=f"{parser.prog}: {readVersion(readFile())}",
    )


def outputFile(parser: ArgumentParser, helpMessage: str, defaultFile: str) -> None:
    parser.add_argument(
        "-o",
        "--output",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultFile,
    )
