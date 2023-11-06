import random
import sys
from functools import reduce



class sketch:
    
    def __init__(self, f, k, w):
        self.f = f
        self.k = k
        self.w = w

        self.counters = [[0 for i in range(self.w)] for i in range(self.k)]

        self.data = []
        self.hc = []
        self.actual = []
        self.estim = []
        self.error = []
        self.avg = 0

        self.final_result = []

    def reading(self):
        
        file = open("./project3input.txt", 'r')
        for line in file:
            line = line.split()
            self.data.append(line)
        self.data = self.data[1:]
        file.close()
        i=0
        while(i<self.f):
            
            self.actual.append(int(self.data[i][1]))
            i=i+1

    def gen2(self):
        i=0
        while(i<self.f):
            
            self.hc.append(hash(self.data[i][0]))
            i=i+1

    def hash(self):

        self.s = random.sample(range(0, 10000000000000), self.k)

    def recording(self):
        i,j=0,0
        while(i<self.f):
            
            while(j<len(self.s)):
                
                l=[self.hc[i],self.s[j]]
                res = reduce(lambda x, y: x ^ y, l)
                ind = res % self.w

                str = bin(res)
                if str[0] != '0':
                    self.counters[j][abs(ind)] -= self.actual[i]
                    
                else:
                    self.counters[j][abs(ind)] += self.actual[i]

                j=j+1
            i=i+1
            j=0
                    

    def query(self):
        i,j=0,0
        while(i<self.f):
            
            est_temp = []
            while(j<len(self.s)):

                l=[self.hc[i],self.s[j]]
                res = reduce(lambda x, y: x ^ y, l)
                ind = res % self.w

                
                str = bin(res)
                if str[0] != '0':
                    est_temp.append(-self.counters[j][abs(ind)])
                    
                else:
                    est_temp.append(self.counters[j][abs(ind)])
                    
                j=j+1

            est_temp = sorted(est_temp)
            if len(est_temp) % 2 != 0:
                med = est_temp[int(len(est_temp)/2)]
                self.estim.append(med)
                
            else:
                mean = int((est_temp[int(len(est_temp)/2)]+ est_temp[int(len(est_temp)/2 - 1)]) / 2)
                self.estim.append(mean)
                
            i=i+1
            j=0
            

    def cal_error(self):
        sum = 0
        i,j=0,0
        while(i<self.f):
            
            self.error.append(abs(self.estim[i] - self.actual[i]))
            i=i+1

        while(j<self.f):
            
            sum += self.error[j]
            j=j+1
        self.avg = float(sum / self.f)


    def answer(self):
        
        for i in range(self.f):
            self.final_result.append([self.data[i][0], self.estim[i], int(self.data[i][1])])

    

if __name__ == "__main__":

   
    n=10000
    k=3
    w=3000
    Cs = sketch(n,k,w)
    val=100
    Cs.reading()
    Cs.gen2()
    Cs.hash()
    Cs.recording()
    Cs.query()
    Cs.cal_error()
    Cs.answer()
    Cs.final_result = sorted(Cs.final_result, key=lambda list: list[1], reverse=True)

    doc = open("output2.txt", 'w')
    print(str(Cs.avg),file= doc)

    i=0
    while(i<val):
        
        print(Cs.final_result[i], file=doc)
        i=i+1