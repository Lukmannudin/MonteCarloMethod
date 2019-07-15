from lib.RandomNumberGenerator import RandomNumberGenerator
from lib.CurahHujan import CurahHujan
from lib.LamaHujan import LamaHujan
from prettytable import PrettyTable
import matplotlib.pyplot as plt

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
        self.intensitasCurahHujan = None
        self.statusHujan = None
        self.simulation = {}

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
     
        for x in range(self.n+1):
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
     
        for x in range(self.n+1):
            for y in range(len(randomNumberInterval)):
                if (multiplicativeNumbers[x]>=randomNumberInterval[y][0] and multiplicativeNumbers[x]<=randomNumberInterval[y][1]) :
                    result.append(category[y])

        self.lamaHujanSimulation = result
    
    def setIntensitasCurahHujan(self):
        result = []
        for x in range(len(self.curahHujanSimulation)):
            result.append(self.curahHujanSimulation[x] / self.lamaHujanSimulation[x])
        
        self.intensitasCurahHujan = result
    
    def setStatusHujan(self):
        result = []
        
        for x in range(len(self.intensitasCurahHujan)):
            if (self.intensitasCurahHujan[x] < 100) :
                result.append("Hujan Ringan")
            elif (self.intensitasCurahHujan[x]>=100 and self.intensitasCurahHujan[x]<300):
                result.append("Hujan Sedang")
            elif (self.intensitasCurahHujan[x]>=300 and self.intensitasCurahHujan[x]<500):
                result.append("Hujan Lebat")
            elif (self.intensitasCurahHujan[x]>=500):
                result.append("Hujan Sangat Lebat")
        
        self.statusHujan = result

        
    def setApp(self):
       self.setLCG()
       self.setMultiplicative()
       self.setCurahHujanSimulation()
       self.setLamaHujanSimulation()
       self.setIntensitasCurahHujan()
       self.setStatusHujan()
    
    def createSimulation(self):
        simulation = {}
        simulation["curah_hujan"] = self.lcgUniform
        simulation["lama_hujan"] = self.multiplicativeUniform
        simulation["curah_hujan_simulation"] = self.curahHujanSimulation
        simulation["lama_hujan_simulation"] = self.lamaHujanSimulation
        simulation["intensitas_curah_hujan"] = self.intensitasCurahHujan
        simulation["status_hujan"] = self.statusHujan
        
        return simulation

    def averageCurahHujan(self):
        count = 0
        for x in range(len(self.curahHujanSimulation)-1):
            count = count + self.curahHujanSimulation[x]
        
        result = count / (len(self.curahHujanSimulation)-1) 
        return round(result,3)
    
    def averageLamaHujan(self):
        count = 0
        for x in range(len(self.lamaHujanSimulation)-1):
            count = count + self.lamaHujanSimulation[x]
        
        result = count / (len(self.lamaHujanSimulation)-1) 
        return result
    
    def averageIntensitasCurahHujan(self):
        count = 0
        for x in range(len(self.intensitasCurahHujan)-1):
            count = count + self.intensitasCurahHujan[x]
        
        result = count / (len(self.intensitasCurahHujan)-1) 
        return result
    
    def maxCurahHujan(self):
        max = 0
        for x in range(len(self.curahHujanSimulation)):
            if (max<self.curahHujanSimulation[x]):
                max = self.curahHujanSimulation[x]
        return max
    
    def minCurahHujan(self):
        min = self.curahHujanSimulation[0]
        for x in range(len(self.curahHujanSimulation)):
            if (min>self.curahHujanSimulation[x]):
                min = self.curahHujanSimulation[x]
        return min
    
    def maxLamaHujan(self):
        max = 0
        for x in range(len(self.lamaHujanSimulation)):
            if (max<self.lamaHujanSimulation[x]):
                max = self.lamaHujanSimulation[x]
        return max
    
    def minLamaHujan(self):
        min = self.lamaHujanSimulation[0]
        for x in range(len(self.lamaHujanSimulation)):
            if (min>self.lamaHujanSimulation[x]):
                min = self.lamaHujanSimulation[x]
        return min

    def maxIntensitasCurahHujan(self):
        max = self.intensitasCurahHujan[0]
        for x in range(len(self.intensitasCurahHujan)):
            if (max<self.intensitasCurahHujan[x]):
                max = self.intensitasCurahHujan[x]
    
        return max
    
    def minIntensitasCurahHujan(self):
        min = self.intensitasCurahHujan[0]
        for x in range(len(self.intensitasCurahHujan)):
            if (min>self.intensitasCurahHujan[x]):
                min = self.intensitasCurahHujan[x]
    
        return min
    
    def showTableSimulation(self):
        simulation = self.createSimulation()
        x = PrettyTable()
        x.field_names = [
                "Simulasi Tahun ke -",
                "Curah Hujan", "Lama Hujan", "Curah Hujan (mm)", "Lama Hujan (bulan)",
                "Intensitas Curah Hujan (mm/hujan)","Status Hujan"
                        ]
            
        for j in range(self.n):
            x.add_row([
                j+1,
                simulation["curah_hujan"][j], 
                simulation["lama_hujan"][j], 
                simulation["curah_hujan_simulation"][j], 
                simulation["lama_hujan_simulation"][j], 
                simulation["intensitas_curah_hujan"][j], 
                simulation["status_hujan"][j]
                ])
                     
        print(x)

        print("HASIL ANALISIS")
        
        print("Rata rata Curah Hujan : ", self.averageCurahHujan())
        print("Rata-rata Lama Hujan  : ", self.averageLamaHujan())
        print("Rata-rata Intensitas Curah Hujan : ",self.averageIntensitasCurahHujan())
        print("Curah Hujan Tertinggi : ",self.maxCurahHujan())
        print("Lama Hujan Terlama : ",self.maxLamaHujan())
        print("Intensitas Curah Hujan Tertinggi : ",self.maxIntensitasCurahHujan())
        print("Curah Hujan Terendah : ",self.minCurahHujan())
        print("Lama Hujan Tersingkat : ",self.minLamaHujan())
        print("Intensitas Curah Hujan Terendah : ",self.minIntensitasCurahHujan())
        
       
    def showGraph(self):
        curahHujanNumbers = self.curahHujan
        category = curahHujanNumbers["category"]
        arr = []
        for x in range(len(self.intensitasCurahHujan)):
            arr.append([x])

        plt.xlabel('Tahun')
        plt.ylabel('Intensitas Curah Hujan')
        plt.title('Intensitas Curah Hujan Tahunan Bandung')     
        plt.grid(True)  
        plt.plot(arr,self.intensitasCurahHujan,'k', color='black')

        inputKey = input("Show Graph ? (y/n)")
        if (inputKey == "y"):
            plt.show()
           

app = App()
app.setRandomNumberGenerator(221,23,1201,10116347,10)
app.setApp()
app.showTableSimulation()
app.showGraph()

