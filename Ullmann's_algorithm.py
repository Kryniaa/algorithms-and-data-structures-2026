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

class Graph2D:
    def __init__(self):
        self.matrix = Matrix((0,0))
        self.vertex_list = []

    def is_empty(self):
        return len(self.vertex_list) == 0
    
    def get_vertex(self, vertex_id):
        return self.vertex_list[vertex_id]
    
    def get_vertex_id(self, vertex):
        return self.vertex_list.index(vertex)
    
    def insert_vertex(self, vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            for row in self.matrix:
                row.append(0)
            new_size = len(self.vertex_list)
            new_row = [0] * new_size
            self.matrix._Matrix__matrix.append(new_row)

    def delete_vertex(self, vertex):
        if vertex in self.vertex_list:
            idx = self.get_vertex_id(vertex)
            for row in self.matrix:
                row.pop(idx)
            self.matrix._Matrix__matrix.pop(idx)
            self.vertex_list.pop(idx)    

    def insert_edge(self, v1, v2, edge=1):
        idx1 = self.get_vertex_id(v1)
        idx2 = self.get_vertex_id(v2)
        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def delete_edge(self, v1, v2):
        idx1 = self.get_vertex_id(v1)
        idx2 = self.get_vertex_id(v2)
        self.matrix[idx1][idx2] = 0
        self.matrix[idx2][idx1] = 0

    def get_edge(self, v1, v2):
        idx1 = self.get_vertex_id(v1)
        idx2 = self.get_vertex_id(v2)
        return self.matrix[idx1][idx2]

    def neighbours(self, vertex_id):
        for i in range(len(self.vertex_list)):
            edge = self.matrix[vertex_id][i]
            if edge != 0:
                yield (i, edge)
    
    def vertices(self):
        for idx in range(len(self.vertex_list)):
            yield idx