

class RandomNumberGenerator:
    def __init__(self, a, c, m, z0, n):
        self.a = a
        self.c = c
        self.m = m
        self.zi = z0
        self.n = n

    def check(self):
        print(self.a)
    
    def countWithLCG(self,zi):
        # zi = nilai bilangan ke-i dari deretnya (RN yang baru)
        result = (self.a*zi+self.c) % self.m
        return result

    def resultIntegerLCGMethod(self):
        randomIntegerNumbers = []
        i=0
        while i <= self.n:
            self.zi = self.countWithLCG(self.zi)
            randomIntegerNumbers.append(self.zi)
            i = i +1

        return randomIntegerNumbers

    def countWithMultiplicative(self,zi):
        # zi = nilai bilangan ke-i dari deretnya (RN yang baru)
        result = (self.a*zi) % self.m
        return result

    def resultIntegerMultiplicativeMethod(self):
        randomIntegerNumbers = []
        i=0
        while i <= self.n:
            self.zi = self.countWithMultiplicative(self.zi)
            randomIntegerNumbers.append(self.zi)
            i = i +1

        return randomIntegerNumbers
    
    def resultLCG(self):
        result = {}
        randomUniformNumbers = []

        randomIntegerNumbers = self.resultIntegerLCGMethod()
        result["zi"] = randomIntegerNumbers
        
        for integerNumber in randomIntegerNumbers:
            resultUniform = round(integerNumber / self.m,3)
            randomUniformNumbers.append(resultUniform)

        result["ui"] = randomUniformNumbers
        return result
    
    def resultMultiplicative(self):
        result = {}
        randomUniformNumbers = []

        randomIntegerNumbers = self.resultIntegerMultiplicativeMethod()
        result["zi"] = randomIntegerNumbers
        
        for integerNumber in randomIntegerNumbers:
            resultUniform = round(integerNumber / self.m,3)
            randomUniformNumbers.append(resultUniform)

        result["ui"] = randomUniformNumbers
        return result
