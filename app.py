from lib.RandomNumberGenerator import RandomNumberGenerator
from lib.CurahHujan import CurahHujan
from lib.LamaHujan import LamaHujan

class App():
    def __init__(self):
        self.a = None
        self.c = None
        self.m = None
        self.z0 = None
        self.n = None
        self.lcgUniform = None
        self.multiplicativeUniform = None
        self.curahHujan = CurahHujan().getCurahHujan()
        self.lamaHujan = LamaHujan().getLamaHujan()
        self.curahHujanSimulation = None
        self.lamaHujanSimulation = None
        self.intensitasLamaHujan = None

    def setRandomNumberGenerator(self,a, c, m, z0, n):
        self.a = a
        self.c = c
        self.m = m
        self.z0 = z0
        self.n = n

    def setLCG(self):
        rng = RandomNumberGenerator(self.a,self.c,self.m,self.z0,self.n)
        self.lcgUniform = rng.resultLCG()["ui"]

    def setMultiplicative(self):
        rng = RandomNumberGenerator(self.a,self.c,self.m,self.z0,self.n)
        self.multiplicativeUniform = rng.resultMultiplicative()["ui"]
    
    def setCurahHujanSimulation(self):
        # Untuk Simulasi
        result = []
        lcgNumbers = self.lcgUniform
        curahHujanNumbers = self.curahHujan
        category = curahHujanNumbers["category"]
        randomNumberInterval = curahHujanNumbers["random_number_interval"]
     
        for x in range(self.n):
            for y in range(len(randomNumberInterval)):
                if (lcgNumbers[x]>=randomNumberInterval[y][0] and lcgNumbers[x]<=randomNumberInterval[y][1]) :
                    result.append(category[y])
        

        self.curahHujanSimulation = result
    
    def setLamaHujanSimulation(self):
         # Untuk Simulasi
        result = []
        multiplicativeNumbers = self.multiplicativeUniform
        lamaHujanNumbers = self.lamaHujan
        category = lamaHujanNumbers["category"]
        randomNumberInterval = lamaHujanNumbers["random_number_interval"]
     
        for x in range(self.n):
            for y in range(len(randomNumberInterval)):
                if (multiplicativeNumbers[x]>=randomNumberInterval[y][0] and multiplicativeNumbers[x]<=randomNumberInterval[y][1]) :
                    result.append(category[y])

        self.lamaHujanSimulation = result
    
    def setIntensitasCurahHujan(self):
        result = []
        for x in range(len(self.curahHujanSimulation)):
            result.append(self.curahHujanSimulation[x] / self.lamaHujanSimulation[x])
        
        self.intensitasLamaHujan = result
    
    def setStatusHujan(self):
        result = []
        
        for x in range(len(self.intensitasLamaHujan)):
            if (self.intensitasLamaHujan[x] < 100) :
                result.append("Hujan Ringan")
            elif (self.intensitasLamaHujan[x]>=100 and self.intensitasLamaHujan[x]<300):
                result.append("Hujan Sedang")
            elif (self.intensitasLamaHujan[x]>=300 and self.intensitasLamaHujan[x]<500):
                result.append("Hujan Lebat")
            elif (self.intensitasLamaHujan[x]>=500):
                result.append("Hujan Sangat Lebat")
        
        return result

        
    def generateTable(self):
       self.setLCG()
       self.setMultiplicative()
       self.setCurahHujanSimulation()
       self.setLamaHujanSimulation()
       self.setIntensitasCurahHujan()
       self.setStatusHujan()


app = App()
app.setRandomNumberGenerator(221,23,1201,10116347,5)
app.generateTable()
