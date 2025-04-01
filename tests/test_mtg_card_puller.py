#!/usr/bin/env python

"""Tests for `mtg_card_puller` package."""

from mtg_card_puller import mtg_card_puller
from mtg_card_puller import cli
from click.testing import CliRunner
import pytest


@pytest.fixture
def test_deck_data():
    """Load sample data

    Load the sample data file in the data folder to test with
    """
    with open('tests/data/sample_deck.txt', 'r') as f:
        test_data = f.read()
    return test_data


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""

    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'mtg_card_puller.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

def test_extract_card_id():
    assert mtg_card_puller.extract_card_id("1 Mox Pearl (M10) 1") == ("(M10)", 1)

