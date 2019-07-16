import pandas as pd

class CurahHujan:
    def __init__(self):
        self.datacurahhujan = pd.read_csv("datacurahhujantahunan.csv")
        self.dataset = self.datacurahhujan.iloc[:,:].values
        self.numberDecimal = 3
        self.startRandom = 0.001
        self.category = None
        self.n = 0
        self.frequency = None
        self.probability = None
        self.cumulativeProbability = None
        self.randomNumberInterval = []
    
    def setCategory(self):
        self.category = [1300,1700,2500,2800,3000]
    
    def setFrequencyAndsetN(self):
        f1 = 0
        f2 = 0
        f3 = 0
        f4 = 0
        f5 = 0
        current = 0
    
        for x in range(len(self.dataset)):
            for y in range(len(self.dataset[x])):
                current = self.dataset[x][y]
                if current == 1300:
                    f1 = f1 +1
                elif current == 1700:
                    f2 = f2 +1
                elif current == 2500:
                    f3 = f3 +1
                elif current == 2800:
                    f4 = f4 +1
                elif current == 3000:
                    f5 = f5 +1
        
        self.n = f1+f2+f3+f4+f5
        self.frequency = [f1,f2,f3,f4,f5]

    def getN(self):
        return self.n

    def setProbability(self):
        result = []

        for x in range(len(self.frequency)):
            result.append(round(self.frequency[x] / self.getN(),self.numberDecimal))

        self.probability = result
    
    def setCumulativeProbability(self):
        result = []
        currentCount = 0

        for x in range(len(self.probability)):
            currentCount = round(currentCount + self.probability[x],self.numberDecimal)
            result.append(currentCount)
        
        self.cumulativeProbability = result
    
    def setRandomNumberInterval(self):
        tb = self.startRandom #tepi atas /tepi bawah
        
        for x in range(len(self.cumulativeProbability)):
            interval = []            
            interval.append(tb)
            interval.append(self.cumulativeProbability[x])
            tb = self.cumulativeProbability[x] + self.startRandom
            self.randomNumberInterval.append(interval)

    def getCurahHujan(self):
        self.setCategory()
        self.setFrequencyAndsetN()
        self.setProbability()
        self.setCumulativeProbability()
        self.setRandomNumberInterval()

        table = {}
        table["category"] = self.category
        table["frequency"] = self.frequency
        table["probability"] = self.probability
        table["cumulative_probability"] = self.cumulativeProbability
        table["random_number_interval"] = self.randomNumberInterval
        return table
   
    def getDataCurahHujan(self):
        return self.dataset


