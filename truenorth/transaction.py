"""Transaction class and parsers."""

import csv
import datetime
import decimal
import enum


class Location(object):
    """A location where a transaction can occur."""

    def __init__(self, location_string):
        self.location_string = location_string

    def __repr__(self):
        return 'Location({!r})'.format(self.location_string)

    def __eq__(self, other):
        return self.location_string == other.location_string


class TransactionType(enum.Enum):
    """A transaction type."""

    tap_in = 1
    tap_out = 2
    transfer = 3
    auto_loaded = 4
    loaded = 5
    purchase = 6


class Product(enum.Enum):
    """A product a transaction can involve (eg. stored value)."""

    stored_value = 1


class Transaction(object):
    """A card transaction."""

    def __init__(self, date_time, location, transaction_type, product, amount):
        self.date_time = date_time
        self.location = location
        self.transaction_type = transaction_type
        self.product = product
        self.amount = amount

    def __repr__(self):
        return 'Transaction({!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.transaction_type, self.date_time, self.location, self.product,
            self.amount
        )

    def __eq__(self, other):
        return (
            self.date_time == other.date_time and
            self.location == other.location and
            self.transaction_type == other.transaction_type and
            self.product == other.product and
            self.amount == other.amount
        )


def _parse_transaction_type(string):
    """Return TransactionType parsed from string."""
    if string.startswith('Tap in at '):
        return TransactionType.tap_in
    elif string.startswith('Tap out at '):
        return TransactionType.tap_out
    elif string.startswith('Transfer at '):
        return TransactionType.transfer
    elif string == 'AutoLoaded':
        return TransactionType.auto_loaded
    elif string.startswith('Loaded at'):
        return TransactionType.loaded
    elif string.startswith('Purchase at '):
        return TransactionType.purchase
    else:
        raise ValueError('Unknown transaction type: {}'.format(repr(string)))


def _parse_date_time(string):
    """Return datetime parsed from string."""
    date_time_format = '%b-%d-%Y %I:%M %p'  # Nov-04-2015 09:06 AM
    return datetime.datetime.strptime(string, date_time_format)


def _parse_location(string):
    """Return Location parsed from string."""
    return Location(string)


def _parse_amount(string):
    """Return amount in integer cents parsed from string."""
    return int(decimal.Decimal(string) * 100)


def _parse_product(string):
    """Return Product parsed from string."""
    if string == 'Stored Value':
        return Product.stored_value
    else:
        raise ValueError('Unknown product: {}'.format(repr(string)))


def _parse_transaction(transaction_dict):
    """Return Product parsed from dictionary."""
    transaction_type = _parse_transaction_type(transaction_dict['Transaction'])
    date_time = _parse_date_time(transaction_dict['DateTime'])
    location = _parse_location(transaction_dict['Location'])
    amount = _parse_amount(transaction_dict['Amount'])
    product = _parse_product(transaction_dict['Product'])
    return Transaction(date_time, location, transaction_type, product, amount)


def parse_csv_file(csv_file):
    """Generate Transactions contained in a usage history CSV file."""
    transaction_reader = csv.DictReader(csv_file)
    for transaction_dict in transaction_reader:
        yield _parse_transaction(transaction_dict)
