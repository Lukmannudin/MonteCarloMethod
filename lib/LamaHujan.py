import pandas as pd

class LamaHujan:
    def __init__(self):
        self.datacurahhujan = pd.read_csv("datalamahujantahunan.csv")
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
        self.category = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    def setFrequencyAndsetN(self):
        f1 = 0
        f2 = 0
        f3 = 0
        f4 = 0
        f5 = 0
        f6 = 0
        f7 = 0
        f8 = 0
        f9 = 0
        f10 = 0
        f11 = 0
        f12 = 0

        current = 0
    
        for x in range(len(self.dataset)):
            for y in range(len(self.dataset[x])):
                current = self.dataset[x][y]
                if current == 1:
                    f1 = f1 +1
                elif current == 2:
                    f2 = f2 +1
                elif current == 3:
                    f3 = f3 +1
                elif current == 4:
                    f4 = f4 +1
                elif current == 5:
                    f5 = f5 +1
                elif current == 6:
                    f6 = f6 +1
                elif current == 7:
                    f7 = f7 +1
                elif current == 8:
                    f8 = f8 +1
                elif current == 9:
                    f9 = f9 +1
                elif current == 10:
                    f10 = f10 +1
                elif current == 11:
                    f11 = f11 +1
                elif current == 12:
                    f12 = f12 +1
        

        self.n = f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12
        self.frequency = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]

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

    def getLamaHujan(self):
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
   
    def getDataLamaHujan(self):
        return self.dataset
