"""Main module."""

import re
import argparse
import logging
from typing import Tuple


def extract_card_id(mox_full_name: str) -> Tuple[str, int]:
    """Extracts the card ID from the full name of a card.

    Args:
        mox_full_name (str): The full name of the card.

    Returns:
        str: The card ID.
    """
    # Extract the card ID using regex
    card_series = ""
    card_number = ""
    match = re.search(r'\d (.*) (\([A-Z]{3}\)) (\d)', mox_full_name)
    if match:
        card_series = match.group(2)
        card_number = int(match.group(3))

        logger.debug(f"Extracted card series: {card_series}, card number: {card_number} from full name: {mox_full_name}")
    else:
        raise ValueError("Problem matching card ID from full name: " + mox_full_name)

    return card_series, card_number


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract card ID from full name.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose output")

    # Parse arguments
    args = parser.parse_args()

    logger = logging.getLogger(__name__)
