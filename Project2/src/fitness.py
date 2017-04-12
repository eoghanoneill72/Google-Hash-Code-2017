def fitness (A):
    
    if fitness_pos(A) > fitness_neg(A):
        return fitness_pos(A)
    else:
        return fitness_neg(A)

    def fitness_pos(A):
        
        fittest_pos = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                    if fitness(A) > fittest_pos:
                        fittest_pos = fitness(A)
                        return fittest_pos
        
    def fitness_neg(A):
        
        fittest_neg = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    A[i][j] = 0
                    if fitness(A) > fittest_neg:
                        fittest_neg = fitness(A)
                        return fittest_neg
                    
                    
                    
def fitness(A):
    if fitness(A[i-1]) > fitness(A[i]):
        return fitness(A[i-1])
    else:
        for not(A[i][j]):
            fitness(A)
        