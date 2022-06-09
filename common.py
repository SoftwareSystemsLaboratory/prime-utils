from argparse import ArgumentParser, HelpFormatter
from operator import attrgetter

from version_utility.main import readFile, readVersion

name: str = "PRIME"
author: str = "Software and Systems Laboratory"


class SortingHelpFormatter(HelpFormatter):
    def add_arguments(self, actions):
        actions = sorted(actions, key=attrgetter("option_strings"))
        super(SortingHelpFormatter, self).add_arguments(actions)


def versionArg(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-v",
        "--version",
        help="Display the version of this tool",
        action="version",
        version=f"{parser.prog}: {readVersion(readFile())}",
    )


def outputFileArg(parser: ArgumentParser, helpMessage: str, defaultFile: str) -> None:
    parser.add_argument(
        "-o",
        "--output",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultFile,
    )


def inputFileArg(parser: ArgumentParser, helpMessage: str, defaultFile: str) -> None:
    parser.add_argument(
        "-i",
        "--input",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultFile,
    )


def plotXDataArg(parser: ArgumentParser, helpMessage: str, defaultValue: str) -> None:
    parser.add_argument(
        "-x",
        "--x-data",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultValue,
    )


def plotYDataArg(parser: ArgumentParser, helpMessage: str, defaultValue: str) -> None:
    parser.add_argument(
        "-y",
        "--y-data",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultValue,
    )


def plotTypeArg(parser: ArgumentParser, helpMessage: str, defaultValue: str) -> None:
    parser.add_argument(
        "--type",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultValue,
    )


def plotTitleArg(parser: ArgumentParser, helpMessage: str, defaultValue: str) -> None:
    parser.add_argument(
        "--title",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultValue,
    )


def plotXLabelArg(parser: ArgumentParser, helpMessage: str, defaultValue: str) -> None:
    parser.add_argument(
        "--x-label",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultValue,
    )


def plotYLabelArg(parser: ArgumentParser, helpMessage: str, defaultValue: str) -> None:
    parser.add_argument(
        "--y-label",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultValue,
    )


def plotStylesheetArg(
    parser: ArgumentParser, helpMessage: str, defaultFile: str
) -> None:
    parser.add_argument(
        "--stylesheet",
        help=helpMessage,
        type=str,
        required=False,
        default=defaultFile,
    )
