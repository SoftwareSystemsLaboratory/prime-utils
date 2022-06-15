from argparse import ArgumentParser, Namespace

from prime_commits.utils import common

version: str = "0.12.0"


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Commit Extractor",
        description="A tool to extract all LOC information from a single branch of a Git repository on a per commit basis",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory containg the .git folder of the repository to analyze",
        type=str,
        required=False,
        default=".",
    )
    parser.add_argument(
        "-b",
        "--branch",
        help="Branch of the Git repository to analyze. DEFAULT: HEAD",
        type=str,
        required=False,
        default="HEAD",
    )
    parser.add_argument(
        "-p",
        "--processes",
        help="Number of cores that cloc should use. NOTE: 0 disables multiprocessing. DEFAULT: 0",
        type=int,
        required=False,
        default=0,
    )
    common.versionArg(parser=parser, version=version)
    common.outputFileArg(
        parser=parser,
        helpMessage="JSON file to extract commits to. DEFAULT: commits.json",
        defaultFile="commits.json",
    )

    return parser.parse_args()


def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Commit Grapher",
        description=f"A tool for graphing LOC information from the output of the {common.name} Commit Extractor",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.plotXDataArg(
        parser=parser,
        helpMessage="X data to plot. NOTE: Should be equivalent to a key in the input file. DEFAULT: days_since_0",
    )
    common.plotYDataArg(
        parser=parser,
        helpMessage="Y data to plot. NOTE: Should be equivalent to a key in the input file. DEFAULT: commit_number",
    )
    common.plotTypeArg(
        parser=parser,
        helpMessage="Specify the plot type. NOTE: Can only be line or bar. DEFAULT: line",
        defaultValue="line",
    )
    common.plotTitleArg(
        parser=parser,
        helpMessage="Title of the graph. DEFAULT: Commits",
        defaultValue="Commits",
    )
    common.plotXLabelArg(
        parser=parser,
        helpMessage="Label of the X axis. DEFAULT: Time",
        defaultValue="Time",
    )
    common.plotYLabelArg(
        parser=parser, helpMessage="Label of the Y axis. DEFAULT: Commits"
    )
    common.plotStylesheetArg(
        parser=parser,
    )
    common.versionArg(parser=parser, version=version)
    common.outputFileArg(
        parser=parser,
        helpMessage="File to save graph to. DEFAULT: commits.pdf",
        defaultFile="commits.pdf",
    )
    common.inputFileArg(
        parser=parser,
        helpMessage="File to generate graph from. DEFAULT: commits.json",
        defaultFile="commits.json",
    )
    return parser.parse_args()
