from argparse import ArgumentParser, Namespace

from prime_issue_spoilage.utils import common

version: str = "0.4.0"


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Issue Spoilage Computer",
        description="A tool to compute the Issue Spoilage of a repository",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Issues Downloader. DEFAULT: issues.json",
        defaultFile="issues.json",
    )
    common.versionArg(parser=parser, version=version)
    common.outputFileArg(
        parser=parser,
        helpMessage="JSON file to output Issue Spoilage computations to. DEFAULT: issueSpoilage.json",
        defaultFile="issueSpoilage.json",
    )

    return parser.parse_args()


def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Issue Spoilage Grapher",
        description=f"A tool for graphing Issue Spoilage information from the output of the {common.name} Issue Spoilage Computer.",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Issue Spoilage Computer. DEFAULT: issueSpoilage.json",
        defaultFile="issueSpoilage.json",
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="Filename of the graph. DEFAULT: issueSpoilage.pdf",
        defaultFile="issueSpoilage.pdf",
    )
    common.plotTypeArg(
        parser=parser,
        helpMessage="Type of graph to plot. DEFAULT: line",
        defaultValue="line",
    )
    common.plotTitleArg(
        parser=parser,
        helpMessage='Title of the graph. DEFAULT: "Issue Spoilage"',
        defaultValue="Issue Spoilage",
    )
    common.plotXLabelArg(
        parser=parser,
        helpMessage="Label of the X axis of the graph. DEFAULT: Days",
        defaultValue="Days",
    )
    common.plotYLabelArg(
        parser=parser,
        helpMessage='Label of the Y axis of the graph. DEFAULT: "Issue "Spoilage',
        defaultValue="Issue Spoilage",
    )
    common.plotStylesheetArg(parser=parser)
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()
