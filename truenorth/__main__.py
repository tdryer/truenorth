"""Command line interface for viewing card usage history."""

import argparse

from truenorth import transaction


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile')
    txn_type_names = [member.name for member in transaction.TransactionType]
    parser.add_argument('--transaction-type', action='append',
                        choices=txn_type_names)
    parser.add_argument('--location', action='append')
    args = parser.parse_args()
    with open(args.csvfile) as csv_file:
        for txn in transaction.parse_csv_file(csv_file):
            if (
                    args.transaction_type and
                    txn.transaction_type.name not in args.transaction_type
            ):
                pass
            elif (
                    args.location and
                    txn.location.location_string not in args.location
            ):
                pass
            else:
                print(txn)


if __name__ == '__main__':
    main()
