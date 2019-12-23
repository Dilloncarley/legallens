Gather Rent leases 
Analyze Rent leases to build data set:
    1. Select sentence that says when the lease starts and ends
    2. Select sentence that says what day of the month the rent is due:
        (This should include if the lease says monthly, bi-weekly or weekly)

LABELS:
RENT_DUE_DATE,
RENT_START_DATE
RENT_END_DATE

==========================

EXAMPLE Training Data:

TRAINING_DATA = [
("Rent is due on the 1st of each month.", {'entities': [(23, 38, 'RENT_DUE_DATE')]}),
("Rent $655 (Monthly)", {'entities': [(14, 20, 'RENT_DUE_DATE')]}),
("This lease begins on October 21, 2019", {'entities': [(25, 39, 'RENT_START_DATE')]}),
("This lease ends on November 21, 2020", {'entities': [(23, 38, 'RENT_END_DATE')]}),
    # And many more examples...
]
