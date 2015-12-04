True North
==========

True North is an unofficial Python library for parsing CSV usage history files
for `Compass Card`_, Vancouver's transit fare card.

.. _Compass Card: https://www.compasscard.ca/

Installation
------------

True North requires Python 3.

Clone the repository::

  git clone https://github.com/tdryer/truenorth.git

Install the :code:`truenorth` Python package::

  cd truenorth
  python setup.py install

Examples
--------

Load a CSV file and print each time you tapped-in::

  import truenorth
  with open('my_compass_card_history.csv') as csv_file:
      for txn in truenorth.parse_csv_file(csv_file):
          if txn.transaction_type == truenorth.TransactionType.tap_in:
              print(txn)

Do the same thing using the included command line tool::

  truenorth my_compass_card_history.csv --transaction-type tap_in

Find the total amount spent on tap-ins, tap-outs, and transfers::

  truenorth my_compass_card_history.csv --sum-amounts \
      --transaction-type tap_in \
      --transaction-type tap_out \
      --transaction-type transfer
