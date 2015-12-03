"""Tests for Transaction parsing."""

import datetime
import io

from truenorth.transaction import (
    parse_csv_file, Transaction, Location, TransactionType, Product,
    _parse_transaction
)


def test_parse_transaction():
    txn_dict = {
        'DateTime': 'Nov-27-2015 09:00 AM',
        'Location': 'Main Street Stn',
        'Transaction': 'Tap out at Main Street Stn',
        'Product': 'Stored Value',
        'Amount': '-1.05'
    }
    txn = _parse_transaction(txn_dict)
    assert txn == Transaction(
        datetime.datetime(2015, 11, 27, 9, 00),
        Location('Main Street Stn'),
        TransactionType.tap_out,
        Product.stored_value,
        -105
    )


def test_parse_csv_file():
    csv_file = io.StringIO(
        'DateTime,Location,Transaction,Product,Amount\n'
        'Nov-27-2015 09:00 AM,Main Street Stn,Tap out at Main Street Stn,'
        'Stored Value,-1.05\n'
        'Nov-27-2015 05:00 PM,Main Street Stn,Tap in at Main Street Stn,'
        'Stored Value,0\n'
    )
    txn_list = list(parse_csv_file(csv_file))
    assert txn_list == [
        Transaction(
            datetime.datetime(2015, 11, 27, 9, 00),
            Location('Main Street Stn'),
            TransactionType.tap_out,
            Product.stored_value,
            -105
        ),
        Transaction(
            datetime.datetime(2015, 11, 27, 17, 00),
            Location('Main Street Stn'),
            TransactionType.tap_in,
            Product.stored_value,
            0
        ),
    ]
