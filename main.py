# This part of the program states the number of rows we want.
n = int(9)

# In this for loop, we state that for variable row in range, the range is the value of n, 0, and whatever n - 1 is.
# If n was = 5, then it would be 5, 0, -1, meaning the output would be 54321. We also need a variable for the column
# (col) and we need to put that for loop inside of the for loop for the row. Here, we mention how many columns we want
# in the output. When row is = 4, we want 4 columns, when row = 3, 3 columns, etc. The first print function says that
# we want to print the number of columns and we also have an end command to make sure the program doesn't print numbers
# in a single column. Lastly, the final print command is for a new line when the program repeats what it should be
# doing.
for row in range(n, 0, -1):
    for col in range(row, 0, -1):
        print(col, end="")
    print()