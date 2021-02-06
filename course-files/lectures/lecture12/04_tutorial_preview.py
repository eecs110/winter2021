frank_pixels = (
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 1, 2, 1, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 2, 3, 3, 3, 3, 3, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 0, 2, 2, 0, 0)
)

for row in frank_pixels:
    print(row)
    
# challenge 1: how do I print each number in the first row?
#
# challenge 2:  Modify the above as follows
# - if the number is 0, print the word 'red'
# - if the number is 1, print the word 'green'
# - if the number is 2, print the word 'blue'
# - if the number is 3, print the word 'purple'
#
# challenge 3: Modify challenge 2 as follows:
# - Output the colors for EVERY row (not just the first one)
# - Before each row, print "ROW X", where X is the number of the row
