from argparse import ArgumentParser, Namespace

from prime_productivity.utils import common

version: str = "0.5.0"


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Productivity Computer",
        description="A tool to compute the Productivity of a repository",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Commit Extractor. DEFAULT: commits.json",
        defaultFile="commits.json",
    )
    common.versionArg(parser=parser, version=version)
    common.outputFileArg(
        parser=parser,
        helpMessage="JSON file to output Productivity computations to. DEFAULT: productivity.json",
        defaultFile="productivity.json",
    )

    return parser.parse_args()


def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Productivity Grapher",
        description=f"A tool for graphing Productivity information from the output of the {common.name} Productivity Computer.",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Productivity Computer. DEFAULT: productivity.json",
        defaultFile="productivity.json",
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="Filename of the graph. DEFAULT: productivity.pdf",
        defaultFile="productivity.pdf",
    )
    common.plotTypeArg(
        parser=parser,
        helpMessage="Type of graph to plot. DEFAULT: line",
        defaultValue="line",
    )
    common.plotTitleArg(
        parser=parser,
        helpMessage='Title of the graph. DEFAULT: "Productivity"',
        defaultValue="Productivity",
    )
    common.plotXLabelArg(
        parser=parser,
        helpMessage="Labe of the X axis of the graph. DEFAULT: Days",
        defaultValue="Days",
    )
    common.plotYLabelArg(
        parser=parser,
        helpMessage="Labe of the Y axis of the graph. DEFAULT: Productivity",
        defaultValue="Productivity",
    )
    common.plotStylesheetArg(parser=parser)
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()
