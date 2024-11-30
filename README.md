# Voting System

## Description
A Python program that simulates a voting process for a constituency. It ensures eligibility criteria, prevents duplicate voting, and calculates the results.

## Features
- Ensures only users aged 18 and above can vote.
- Accepts valid IDs within a specified range (2000-8999).
- Prevents duplicate voting by tracking voter IDs.
- Allows users to choose from five voting options:
  1. BJP
  2. Congress
  3. BRS
  4. TDP
  5. Nota
- Displays the total votes for each option and announces the winner.

## Example Output
-- Enter your age: 25
- WELCOME TO ABC CONSTITUENCY
- Enter your name: Alice
- Enter your id: 2001
- ======================
- Option 1: BJP
- Option 2: Congress
- Option 3: BRS
- Option 4: TDP
- Option 5: Nota
- ======================
- Cast your vote: 3
- 2001 vote casted successfully thank you!!

- Voting process completed
- BJP: 0
- Congress: 0
- BRS: 1
- TDP: 0
- Nota: 0
- Winner is BRS with votes 1
