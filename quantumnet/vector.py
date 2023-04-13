from math import sqrt

class Vector:
    def __init__(self, vectorComponents):
        if (not vectorComponents):
            raise ValueError("The list of vector components cannot be empty")
        if (not all(item.isdigit() for item in vectorComponents)):
            raise ValueError("The list of vector components can only contain numbers")
        self._vectorComponents = vectorComponents
        self._vectorSpace = len(vectorComponents)
    
    def getVectorComponents(self):
        return self._vectorComponents

    def getVectorSpace(self):
        return self._vectorSpace
    
    def __str__(self) -> str:
        vector = "<"
        for i in range(0, self._vectorSpace - 1):
            if (i == len(self._vectorComponents) - 1):
                vector += str(self._vectorComponents[i])
            else:
                vector += str(self._vectorComponents[i]) + ", "
        vector += ">"
        return vector
    
    def __eq__(self, otherVector: object) -> bool:
        if len(self._vectorComponents) != len(otherVector.getVectorSpace()):
            return False
        else:
            for i in range(0, self._vectorSpace):
                if self._vectorComponents[i] != otherVector.getVectorSpace()[i]:
                    return False
                else: continue
        return True
    
    def dot_product(self, otherVector: object) -> float:
        if self._vectorSpace != otherVector.getVectorSpace():
            raise ValueError("Cannot compute dot product because the vectors have different vector space")
        dot_product = 0
        for i in range(0, self.getVectorSpace()):
            dot_product += (self.getVectorComponents[i] * otherVector.getVectorComponents()[i])
        return dot_product
    
    def euclidean_norm(self) -> float:
        if not self.getVectorComponents:
            raise ValueError("The vector is empty <>")
        sum_of_squares = 0
        for i in range(self._vectorSpace):
            sum_of_squares += pow(self._vectorComponents[i], 2)
        
        return sqrt(sum_of_squares)
    
