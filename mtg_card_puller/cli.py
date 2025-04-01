"""Console script for mtg_card_puller."""

import sys
import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.command(context_settings=CONTEXT_SETTINGS)
def main(args=None):
    """Console script for mtg_card_puller."""
    click.echo("Replace this message by putting your code into "
               "mtg_card_puller.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
