import random
import sys
import os
from numpy import array
from functools import reduce



class CountMin:
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
        self.p = 0.5

    def reading(self):
        file = open("project3input.txt", 'r')
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
        while(i<int(self.f)):
            self.hc.append(abs(hash(self.data[i][0])))
            i=i+1

    def hash(self):

        self.s = random.sample(range(0, 10000000000000), self.k)


    def recording(self):
        i,j,k=0,0,0
        while(i<self.f):
            while(j<len(self.s)):
                l=[self.hc[i],self.s[j]]
                res = reduce(lambda x, y: x ^ y, l)
                hash_index = res % self.w
                while(k<self.actual[i]):
                    rand = random.randint(1, 10000)
                    if rand > 5000:
                        pass
                    else:
                        self.counters[j][hash_index] += 1
                    k=k+1
                j=j+1
                k=0
            i=i+1
            j=0

    def query(self):
        min = sys.maxsize
        i,j=0,0
        while(i<self.f):
            while (j<len(self.s)):
                l=[self.hc[i],self.s[j]]
                res = reduce(lambda x, y: x ^ y, l)
                hash_index = res % self.w

                if min <= self.counters[j][hash_index]:
                    pass
                else:
                    min = self.counters[j][hash_index]
                j=j+1
            self.estim.append(min * (1 / self.p))
            min = sys.maxsize

            i=i+1
            j=0

    def compute_error(self):
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
        i=0
        while(i<self.f):
            self.final_result.append([self.data[i][0], self.estim[i], int(self.data[i][1])])
            i=i+1


if __name__ == "__main__":

    n=10000
    k=3
    w=3000
    
    count_min = CountMin(n,k,w)
    count_min.reading()
    count_min.gen2()
    count_min.hash()
    count_min.recording()
    count_min.query()
    count_min.compute_error()
    count_min.answer()
    count_min.final_result = sorted(count_min.final_result, key=lambda list:list[1], reverse=True)

    doc = open("output1.txt", 'w')
    print(str(count_min.avg), file=doc)
    i=0
    ans=100
    while(i<ans):
        print(count_min.final_result[i],file=doc)
        i=i+1













