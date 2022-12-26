import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    database = sys.argv[1]
    with open(database, "r") as db:
        dbReader = csv.DictReader(db)
        dbList = list(dbReader)

    # TODO: Read DNA sequence file into a variable
    sequence = sys.argv[2]
    with open(sequence, "r") as seq:
        seqReader = seq.read()

    # TODO: Find longest match of each STR in DNA sequence
    # Create an array to store the SRT
    longestMatch = []

    # Loop to read the SRT in the first line of dbReader starting in column 1 (first is the name)
    for i in range(1, len(dbReader.fieldnames)):
        SRT = dbReader.fieldnames[i]
        longestMatch.append(0)
        # i-1 as arrays are 0 indexed. Use the prewritten function pass the reader for the sequence and the newly created SRT
        longestMatch[i - 1] = longest_match(seqReader, SRT)
        # DEBUG: print(longestMatch[i - 1])

    # TODO: Check database for matching profiles
    # Loop over the entries of the database ignoring the first line
    for i in range(0, len(dbList)):
        match = 0

        # Loop over the columns of each entry in the database
        for j in range(1, len(dbReader.fieldnames)):

            # DEBUG: print(dbList[i][dbReader.fieldnames[j]])
            # If the current value of dbList....  is the same as the value of longestMatch in the same column is a match
            if int(dbList[i][dbReader.fieldnames[j]]) == longestMatch[j - 1]:
                match += 1

        # If the number of matches is the same as the number of columns in the dictionary print the name of the match
        # -1 cause column 0 is the name
        if match == len(dbReader.fieldnames)-1:
            print(dbList[i][dbReader.fieldnames[0]])

            # If is a match, return as not possible to have more than one matches
            return
        
    # If no match, print it.
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
