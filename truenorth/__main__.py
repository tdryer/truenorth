"""Command line interface for viewing card usage history."""

import argparse

from truenorth import transaction


def filter_txns(txns, txn_type_filter, location_filter):
    """Filter transactions by type and/or location."""
    for txn in txns:
        if (
                txn_type_filter and
                txn.transaction_type.name not in txn_type_filter
        ):
            pass
        elif (
                location_filter and
                txn.location.location_string not in location_filter
        ):
            pass
        else:
            yield txn


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile')
    txn_type_names = [member.name for member in transaction.TransactionType]
    parser.add_argument('--transaction-type', action='append',
                        choices=txn_type_names)
    parser.add_argument('--location', action='append')
    parser.add_argument('--sum-amounts', action='store_true')
    args = parser.parse_args()
    with open(args.csvfile) as csv_file:
        txns = filter_txns(transaction.parse_csv_file(csv_file),
                           args.transaction_type, args.location)
        if args.sum_amounts:
            print(sum(txn.amount for txn in txns))
        else:
            for txn in txns:
                print(txn)


if __name__ == '__main__':
    main()
