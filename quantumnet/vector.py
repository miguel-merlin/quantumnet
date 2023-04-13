class Vector:
    def __init__(self, vectorComponents):
        if (not vectorComponents):
            raise ValueError("The list of vector components cannot be empty")
        if (not all(item.isdigit() for item in vectorComponents)):
            raise ValueError("The list of vector components can only contain numbers")
        self._vectorComponents = vectorComponents
        self._vectorSpace = len(vectorComponents)
    
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
        if len(self._vectorComponents) != len(otherVector._vectorComponents):
            return False
        else:
            for i in range(0, self._vectorSpace):
                if self._vectorComponents[i] != otherVector._vectorComponents[i]:
                    return False
                else: continue
        return True

    
