# Legal Lens
This project is to serve the purpose of analysing rent agreements and highlighting important pieces of information in them. This could include when the rent is due each month, any security deposits due, moveout agreements, etc. 

## Natural Language Processing Library That I am Using
https://spacy.io/

### First Goals
* Find the lease terms (start, end) dates
* Find when the rent is due each month

#### How to Achieve these Goals

* Gather Training Rent leases (Getting mine from https://www.docracy.com/) Just search "rent leases" or something similar
* Analyze Rent leases to build data set:
    1. Select sentences that states when the lease starts and ends
    2. Select sentences that states what day of the month the rent is due:
        (This should include if the lease says monthly, bi-weekly or weekly)

LABELS:
RENT_DUE_DATE,
RENT_START_DATE
RENT_END_DATE

==========================

EXAMPLE Training Data:

```TRAINING_DATA = [
("Rent is due on the 1st of each month.", {'entities': [(23, 38, 'RENT_DUE_DATE')]}),
("Rent $655 (Monthly)", {'entities': [(14, 20, 'RENT_DUE_DATE')]}),
("This lease begins on October 21, 2019", {'entities': [(25, 39, 'RENT_START_DATE')]}),
("This lease ends on November 21, 2020", {'entities': [(23, 38, 'RENT_END_DATE')]}),
    # And many more examples...
]```
