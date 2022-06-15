from argparse import ArgumentParser, Namespace

from prime_bus_factor.utils import common

version: str = "0.5.0"


def mainArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Bus Factor Computer",
        description="A tool to compute both the Bus Factor and Developer Count of a repository",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Commits Extractor. DEFAULT: commits.json",
        defaultFile="commits.json",
    )
    parser.add_argument(
        "-b",
        "--bin",
        help="Bin the Bus Factor and Developer Counts to a number of days. DEFAULT: 1",
        type=int,
        required=False,
        default=1,
    )
    common.versionArg(parser=parser, version=version)
    parser.add_argument(
        "-a",
        "--alpha",
        help="The percent change of the code base a developer needs to contribute in a time interval to be considered for the Bus Factor computation. DEFAULT: 0.8",
        type=float,
        default=0.8,
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="JSON file to output Bus Factor and Developer Count computations to. DEFAULT: bf_dc.json",
        defaultFile="bf_dc.json",
    )

    return parser.parse_args()


def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Bus Factor Grapher",
        description=f"A tool for graphing Bus Factor and Developer Count information from the output of the {common.name} Bus Factor Computer. By default, it graphs the Bus Factor.",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Bus Factor Computer. DEFAULT: bf_dc.json",
        defaultFile="bf_dc.json",
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="Filename of the graph. DEFAULT: busFactor.pdf",
        defaultFile="busFactor.pdf",
    )
    common.plotTypeArg(
        parser=parser,
        helpMessage="Type of graph to plot. DEFAULT: bar",
        defaultValue="bar",
    )
    common.plotTitleArg(
        parser=parser,
        helpMessage='Title of the graph. DEFAULT: "Bus Factor"',
        defaultValue="Bus Factor",
    )
    common.plotXLabelArg(
        parser=parser,
        helpMessage="Label of the X axis of the graph. DEFAULT: Days",
        defaultValue="Days",
    )
    common.plotXDataArg(
        parser=parser,
        helpMessage="Data to plot on the X axis. DEFAULT: days_since_0",
        defaultValue="days_since_0",
    )
    common.plotYLabelArg(
        parser=parser,
        helpMessage="Label of the Y axis of the graph. DEFAULT: Bus Factor",
        defaultValue="Bus Factor",
    )
    common.plotYDataArg(
        parser=parser,
        helpMessage="Data to plot on the y axis. DEFAULT: busFactor",
        defaultValue="busFactor",
    )
    common.plotStylesheetArg(parser=parser)
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()
