from argparse import ArgumentParser, Namespace

from prime_issues.utils import common

version: str = "0.10.0"


def bugzillaArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Bugzilla Issues Downloader (BETA)",
        description="A tool to download all Issues from a Bugzilla hosted issue tracker",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )

    parser.add_argument(
        "-u",
        "--url",
        help="Bugzilla repository root url. DEFAULT: https://bugzilla.kernal.org. NOTE: Structure the URL exactly like the DEFAULT or else this will not work.",
        type=str,
        required=True,
        default="https://bugzilla.kernal.org",
    )
    common.inputFileArg(
        parser=parser,
        helpMessage="CSV file of exported Bugzilla bugs. DEFAULT: bugzillaIssues.csv",
        defaultFile="bugzillaIssues.csv",
    )

    common.outputFileArg(
        parser=parser,
        helpMessage="File to save JSON response(s) to. DEFAULT: bugzillaIssues.json",
        defaultFile="bugzillaIssues.json",
    )
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()


def githubArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} GitHub Issues Downloader",
        description="A tool to download all issues from a GitHub hosted repository",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--pull-request",
        help="Flag to enable the collection of pull requests with the other data",
        required=False,
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="GitHub formatted as repository owner/repository",
        type=str,
        required=True,
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="File to save JSON response(s) to. DEFAULT: githubIssues.json",
        defaultFile="githubIssues",
    )

    parser.add_argument(
        "-t",
        "--token",
        help="GitHub personal access token",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--log",
        help="File to store logs in. DEFAULT: github_issues.log",
        type=str,
        required=False,
        default="github_issues.log",
    )
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()


def gitlabArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Gitlab Issues Downloader",
        description="A tool to download all issues from a Gitlab hosted repository",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )

    parser.add_argument(
        "-r",
        "--repository",
        help="Gitlab repository ID",
        type=str,
        required=True,
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="File to save JSON response(s) to. DEFAULT: gitlabIssues.json",
        defaultFile="gitlabIssues.json",
    )
    parser.add_argument(
        "-t",
        "--token",
        help="Gitlab personal access token",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--log",
        help="File to store logs in. DEFAULT: gitlab_issues.log",
        type=str,
        required=False,
        default="gitlab_issues.log",
    )
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()


def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{common.name} Issues Grapher",
        description=f"A tool for graphing Issue information from the output of the {common.name} Issues Downloader.",
        epilog=f"Author(s): {common.author}",
        formatter_class=common.SortingHelpFormatter,
    )
    common.inputFileArg(
        parser=parser,
        helpMessage=f"JSON file from {common.name} Productivity Computer. DEFAULT: githubIssues.json",
        defaultFile="githubIssues.json",
    )
    common.outputFileArg(
        parser=parser,
        helpMessage="Filename of the graph. DEFAULT: githubIssues.pdf",
        defaultFile="githubIssues.pdf",
    )
    common.plotTypeArg(
        parser=parser,
        helpMessage="Type of graph to plot. DEFAULT: line",
        defaultValue="line",
    )
    common.plotTitleArg(
        parser=parser,
        helpMessage="Title of the graph. DEFAULT: Issues",
        defaultValue="Issues",
    )
    common.plotXLabelArg(
        parser=parser,
        helpMessage="Label of the X axis of the graph. DEFAULT: Days",
        defaultValue="Days",
    )
    common.plotYLabelArg(
        parser=parser,
        helpMessage="Label of the Y axis of the graph. DEFAULT: Issues",
        defaultValue="Issues",
    )
    common.plotXDataArg(
        parser=parser,
        helpMessage="Key of the x values to use for graphing. DEFAULT: opened_day_since_0",
        defaultValue="opened_day_since_0",
    )
    parser.add_argument(
        "--y-thousandths",
        help="Flag to divide the y values by 1000",
        action="store_true",
        required=False,
        default=False,
    )
    common.plotStylesheetArg(parser=parser)
    common.versionArg(parser=parser, version=version)
    return parser.parse_args()
