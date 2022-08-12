#! /usr/bin/python
# Here X is denoted as Array input
def getuserinput():
    User_data=list(map(int,input().split()))
    return User_data

# To find the missing elements in an array
class Find_Missing_Numbers:
    def __init__(self,arr):
        self.x=sorted(arr)
        self.f=self.x[0]
        self.l=self.x[-1]
    #unarrange
    #find take index 0 and index n and check wheather the number is in the list
    def append(self):
        missing=[]
        for i in range(self.f,self.l):
            if i not in self.x:
                missing.append(i)
        return missing
    #unarrange
    #only valid if size is within element max 
    def Formo_1(self):
        total= ((self.l-1 + 1)*(self.l-1 + 2)/2)-((self.f-2 + 1)*(self.f-2 + 2)/2)
        sum_of_A = sum(self.x)
        return int(total - sum_of_A)
    #unarrange
    # but range shoud be in order 1..10
    def Formo_2(self):
        i, total = 0, 1
        for i in range(2,len(self.x)+2):
            total += i
            # print(total)
            total -= self.x[i-2]
            # print(total,end=" ")
        return total
    #unarrange
    def Formo_3(self):
        self.n+=1
        n_elements_sum=self.n*(self.n+1)//2
        return n_elements_sum-sum(self.x)

    def Formo_4(self):
        return [(e1+1) for e1,e2 in zip(self.x, self.x[1:]) if e2-e1 != 1]

    def Formo_5(self):
        return [self.x[i] + 1 for i in range(self.n - 1) if self.x[i] + 1 != self.x[i + 1]]
    #unarrange  
    def modulo(self):
        x1 = self.x[0]
        x2 = 1
        for i in range(1, self.n):
            x1 = x1 ^ self.x[i]
         
        for i in range(2, self.n + 2):
            x2 = x2 ^ i
        return x1 ^ x2

if __name__ == '__main__':
    x = [1,3,4,5] 
    # x=getuserinput()
    func=Find_Missing_Numbers(x)
    print(func.Formo_2())