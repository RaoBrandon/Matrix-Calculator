class matrix:
    def __init__(self):
        '''Initialize the container variable'''
        self.contents = []

    def is_all_ints(self, row):
        '''This method takes a row and determines if all items in that row
        are integers'''

        all_ints = True
        # For every item in the row, if at least 1 is not an integer, then
        # all_ints must be false
        for item in row:
            if type(item) != int:
                all_ints = False
        return all_ints

    def is_multiplicable(self, matrix):
        '''This method takes a matrix node and compares it with self, if the
        dimensions of the matrix match with the dimensions of self.contents,
        that means that a multiplication between the two is computable'''

        # For the dimensions of 2 matrices, a*b and c*d the 2 matrices can be
        # multiplied iff b == c
        if len(self.contents[0]) == len(matrix.contents):
            is_multiplicable = True
        else:
            is_multiplicable = False
        return is_multiplicable

    def can_add(self, matrix):
        '''This method takes a matrix and compares it with itself and if the
        dimension are equal then it is possible to add these two matrices
        together
        '''

        # We have to check each row and make sure they are the same length
        if len(self.contents[0]) == len(matrix.contents[0]):
            can_add = True
        else:
            can_add = False
        return can_add

    def addrow(self, row):
        '''This method is used when rows are to be added to matrix nodes, using
        node.addrow(row) a new row will be appended to the node. There are two
        reasons addrow could not work, that is when the user tries to add a row
        with a non-int and when the user tries to add rows of unequal length
        '''

        # First we must use our all_ints method to see if the row
        # contains all integers
        if self.is_all_ints(row):
            # We should be able to add rows of any length to empty matrices
            if self.contents == []:
                self.contents.append(row)
            # If the matrix is not empty, the length of the row to be added
            # must be of the same length as the rows before it
            elif len(row) == len(self.contents[0]):
                self.contents.append(row)
            else:
                # If neither of these are true, it nmust mean the user tried to
                # add a rows of unequal length to the matrix
                print("Oops! That row wasnt of the same length as the others!")
        else:
            # The method all_ints returned false which means the user tried to
            # input a non-int
            print("Oops! I cannot add a row that contains a non-int!")

    def deleterow(self, row_num):
        '''This method is used to delete rows, given the row number to be
        removed it will simply remove the value of the content at that index'''

        self.contents.remove(self.contents[row_num])

    def dotproduct(self, row1, row2):
        '''This method returns the product of two rows of the same length'''

        # Running total
        mult_result = 0
        for number in range(0, len(row1)):
            # Multiply the numbers of matching indices and add to the total
            mult_result += row1[number]*row2[number]
        return mult_result

    def transpose(self, matrix):
        '''This method takes any a*b matrix and returns the b*a matrix where
        the rows become columns and columns become rows
        '''

        # Initialize empty matrix to add row values to
        transpose_matrix = []
        for row_length in range(0, len(matrix.contents[0])):
            # For every new column, the new row resets so it doesnt mix up
            # previous values into the following columns
            new_row = []
            for row in matrix.contents:
                # Takes each column entry and adds it to the new row entries
                new_row += [row[row_length]]
            # Adds the new row into the matrix
            transpose_matrix += [new_row]
        return transpose_matrix

    def multiply(self, matrix):
        '''This method tales a matrix and computes a matrix multiplation with
        its own contents. In matrix multiplication, each new entry is computed
        by doing a dot product with a row and column
        '''

        # First we must make sure the two matrices are multiplicable
        if self.is_multiplicable(matrix):
            # Initialize container for the resulting matrix
            resultant_matrix = []
            # First we transpose the given matrix into one with the same
            # dimensions as self.contents, this way we can use our dot_product
            # method for each row to row directly
            usable_matrix = self.transpose(matrix)
            # Compute the dot product of each row to row directly
            for row in self.contents:
                resultant_row = []
                for column in usable_matrix:
                    resultant_row += ([self.dotproduct(column, row)])
                resultant_matrix += [resultant_row]
        else:
            # The method is_multiplicable returned false, so the dimensions do
            # no match and the resultant matrix cannot be computed
            resultant_matrix = "The matrix dimensions do not match up!"
        return resultant_matrix

    def __str__(self):
        '''This method returns a string representation of self.contents, it
        prints out each row individually so the user can get a good idea of
        what are considered row entries and column entries'''

        print("Note that the last result is the list form of your matrix\n" +
              "if the matrix is empty it will display an empty list")
        for row in self.contents:
            print(row)
        return str(self.contents)
