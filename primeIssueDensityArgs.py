from argparse import ArgumentParser, Namespace

from prime_issue_density.utils import common

version: str = "0.4.0"


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Issue Density Computer",
        description="A tool to compute the Issue Density of a repository",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    parser.add_argument(
        "-c",
        "--commits",
        help=f"Commits JSON file from {common.name} Commits Extractor. DEFAULT: commits_loc.json",
        default="commits_loc.json",
        required=False,
        type=str,
    )
    parser.add_argument(
        "-i",
        "--issues",
        help=f"Issues JSON file from {common.name} Issues Extractor. DEFAULT: issues.json",
        default="issues.json",
        required=False,
        type=str,
    )
    common.versionArg(parser=parser, version=version)
    common.outputFileArg(
        parser=parser,
        helpMessage="JSON file to output Issue Density computations to. DEFAULT: issueDensity.json",
        defaultFile="issueDensity.json",
    )

    return parser.parse_args()


def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Issue Density Grapher",
        description=f"A tool for graphing Issue Density information from the output of the {common.name} Issue Density Computer.",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Issue Density Computer. DEFAULT: issueDensity.json",
        defaultFile="issueDensity.json",
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="Filename of the graph. DEFAULT: issueDensity.pdf",
        defaultFile="issueDensity.pdf",
    )
    common.plotTypeArg(
        parser=parser,
        helpMessage="Type of graph to plot. DEFAULT: line",
        defaultValue="line",
    )
    common.plotTitleArg(
        parser=parser,
        helpMessage='Title of the graph. DEFAULT: "Issue Density""',
        defaultValue="Issue Density",
    )
    common.plotXLabelArg(
        parser=parser,
        helpMessage="Labe of the X axis of the graph. DEFAULT: Days",
        defaultValue="Days",
    )
    common.plotYLabelArg(
        parser=parser,
        helpMessage='Label of the Y axis of the graph. DEFAULT: "Issue Density"',
        defaultValue="Issue Density",
    )
    common.plotStylesheetArg(parser=parser)
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()
