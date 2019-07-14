# NIM : 10116347
# Nama : Lukmannudin
# Kelas : MOSI-08
# Catatan : Dijalankan di python versi 3
class RandomNumberLCGGenerator:
    def __init__(self, a, c, m, z0, n):
        self.a = a
        self.c = c
        self.m = m
        self.zi = z0
        self.n = n
        self.randomNumbersIntegerAndUniform = []

    def countWithLCGMethod(self,zi):
        # zi = nilai bilangan ke-i dari deretnya (RN yang baru)
        result = (self.a*zi+self.c) % self.m
        return result
    
    def resultIntegerLCGMethod(self):
        randomIntegerNumbers = []
        i=0
        while i <= self.n:
            self.zi = self.countWithLCGMethod(self.zi)
            randomIntegerNumbers.append(self.zi)
            i = i +1

        return randomIntegerNumbers

    def resultUniformLCGMethod(self):
        randomUniformNumbers = []
        randomIntegerNumbers = self.resultIntegerLCGMethod()

        for integerNumber in randomIntegerNumbers:
            resultUniform = integerNumber / self.m
            randomUniformNumbers.append(resultUniform)

        return randomUniformNumbers
    
    def getRandomNumbers(self):
            
        randomNumbersLCG = [
            self.resultIntegerLCGMethod(),
            self.resultUniformLCGMethod()
        ]
        return randomNumbersLCG


class RandomNumberGenerator: 
    # a = konstanta pengali
    # c = increment(angka konstan yang bersyarat)
    # m = modulus(modulo)
    # z0 = kunci pembangkit / seed
    # n = jumlah deret

    def __init__(self,a,c,m,z0,n):
        self.initilize(a,c,m,z0,n)
        self.LCGMethod = RandomNumberLCGGenerator(a,c,m,z0,n)
        self.RVG = RandomVariateGenerator(self.LCGMethod.resultUniformLCGMethod())
        
    def initilize(self,a,c,m,z0,n):
        self.a = a
        self.c = c
        self.m = m 
        self.z0 = m
        self.n = n
  
    def generateRandomLCGTableNumbers(self):
        if (self.a < self.m and self.c < self.m):
            n = self.n
            randomNumbers = self.LCGMethod.getRandomNumbers()
            randomNumbers.append(self.RVG.getResultCDF())
             
            ZiRandomNumbers = randomNumbers[0]
            UiRandomNumbers = randomNumbers[1]
            XiRandomNumbers = randomNumbers[2]
            ZiLoopedPosition = self.periodikCheck(ZiRandomNumbers)
            UiLoopedPosition = self.periodikCheck(UiRandomNumbers)
            XiLoopedPosition = self.periodikCheck(XiRandomNumbers)
            if (ZiLoopedPosition + UiLoopedPosition + XiLoopedPosition) > 0 :
                print("Zi terulang di posisi "+str(ZiLoopedPosition))
                print("Ui terulang di posisi "+str(UiLoopedPosition))
                print("Xi terulang di posisi "+str(XiLoopedPosition))

            print("|\ti\t|\tZi\t|\tUi\t|\tXi\t|")
            for i in range(0,n):
                print("|\t{}\t|  {:.0f}\t\t|  {:.4f}\t|  {:.4f}\t|"
                    .format(i+1, randomNumbers[0][i], randomNumbers[1][i],randomNumbers[2][i])
                    )
        else:
            print("Seharusnya a < m dan c < m")        

    def periodikCheck(self,numbers):
        loopedPosition = 0
        tempNumber = numbers[0]
        for i in range(1,len(numbers)):
            if (numbers[i] == tempNumber):
                loopedPosition = i+1
                break

        return loopedPosition

class RandomVariateGenerator:
    def __init__(self, uniformNumbers):
        self.uniformNumbers = uniformNumbers
    
    def getResultCDF(self):
        cdfNumbers = []
        for number in self.uniformNumbers:
            result = None
            result = ((9/4)*number**2)**(1/3)
            cdfNumbers.append(result)

        return cdfNumbers

    

a = 221
c = 23 
m = 1201
z0 = 10116347
n = 10
rng = RandomNumberGenerator(a,c,m,z0,n)
rng.generateRandomLCGTableNumbers()
