from argparse import ArgumentParser

from version_utility.utils.self import readVersion

name: str = "PRIME"
author: str = "Software and Systems Laboratory"


def version(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-v",
        "--version",
        help="Display the version of this tool",
        action="version",
        version=f"{parser.prog}: {readVersion()}",
    )
