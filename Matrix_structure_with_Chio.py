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
    
    def chio_method(self):
        n = self.size()[0]

        if self.size()[1] != n:
            return None
        
        if n == 1:
            return self[0][0]
        
        if n == 2:
            return (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
        
        sign = 1
        if self[0][0] == 0:
            found = False

            for i in range(1,n):
                if self[i][0] != 0:
                    self.__matrix[0], self.__matrix[i] = self.__matrix[i], self.__matrix[0]
                    sign = -1
                    found = True
                    break
            if found == False:
                return 0
            
        a11 = self[0][0]
        new_matrix = Matrix((self.size()[0]-1, self.size()[1]-1 ))
        for i in range(new_matrix.size()[0]):
                for j in range(new_matrix.size()[1]):
                    new_matrix[i][j] = a11 * self[i + 1][j + 1] - self[0][j + 1] * self[i + 1][0] 

        return sign * (1 / (a11 ** (n - 2))) * new_matrix.chio_method()      

def transpose(matrix):
    if not isinstance(matrix, Matrix):
        return None
    
    result = Matrix((matrix.size()[1],matrix.size()[0]))
    
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            result[j][i] = matrix[i][j]
    
    return result


def main():
    m1 = Matrix([[5, 1, 1, 2, 3], 
                 [4, 2, 1, 7, 3], 
                 [2, 1, 2, 4, 7], 
                 [9, 1, 0, 7, 0], 
                 [1, 4, 7, 2, 2]])
    m2 = Matrix([[0, 1, 1, 2, 3], 
                 [4, 2, 1, 7, 3], 
                 [2, 1, 2, 4, 7], 
                 [9, 1, 0, 7, 0], 
                 [1, 4, 7, 2, 2]])
    m3 = Matrix([[0, 0, 0, 0, 0], 
                 [4, 2, 1, 7, 3], 
                 [2, 1, 2, 4, 7], 
                 [9, 1, 0, 7, 0], 
                 [1, 4, 7, 2, 2]])
    m4 = Matrix([[0, 1, 1, 2, 3], 
                 [0, 2, 1, 7, 3], 
                 [0, 1, 2, 4, 7], 
                 [0, 1, 0, 7, 0], 
                 [0, 4, 7, 2, 2]])
    
    print(m1.chio_method())
    print(m2.chio_method())
    print(m3.chio_method())
    print(m4.chio_method())

if __name__ == "__main__":
    main()