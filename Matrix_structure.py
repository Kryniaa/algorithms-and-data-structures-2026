class Matrix:

    def __init__(self, matrix, c=0):
        if isinstance(matrix, tuple):
            self.__matrix = [[c] * matrix[1] for i in range(matrix[0])]
        else:
            self.__matrix = matrix

    def size(self):
        return (len(self.__matrix),len(self.__matrix[0]))
    
    def __add__(self, var):
        if self.size() != var.size():
            return None
        
        result = Matrix(self.size())

        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                result.__matrix[i][j] = self.__matrix[i][j] + var.__matrix[i][j]
        
        return result
    def __mul__(self, var):
        if self.size()[1] != var.size()[0]:
            return None
        
        result = Matrix((self.size()[0],var.size()[1]))

        for i in range(self.size()[0]):
            for j in range(var.size()[1]):
                sum = 0
                for k in range(self.size()[1]):
                    result[i][j] += self.__matrix[i][k] * var.__matrix[k][j]
        
        return result
    
    def __eq__(self, var):
        if self.size() != var.size():
            return False

        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                if(self.__matrix[i][j] != var.__matrix[i][j]):
                    return False
        
        return True
    
    def __getitem__(self, row):
        return self.__matrix[row]
    
    def __str__(self):
        res = ""
        for row in self.__matrix:
            res += "| "
            n = 0
            for elem in row:
                if n+1 == self.size()[1]:
                    res += str(elem) + " "
                else:
                    res += str(elem) + "  "
                n += 1
            res += "|\n"
        return res.strip()

def transpose(matrix):
    if not isinstance(matrix, Matrix):
        return None
    
    result = Matrix((matrix.size()[1],matrix.size()[0]))
    
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            result[j][i] = matrix[i][j]
    
    return result

m1 = Matrix(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

print("m1:")
print(m1)
print("\n")

m2 = Matrix(
[ [3, 1],
  [2, 1],
  [1, 0]]
)

print("m2:")
print(m2)
print("\n")

print("m1*m2:")
print(m1*m2)