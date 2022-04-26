#! /usr/bin/python
# Here X is denoted as Array input
def getuserinput():
    User_data=list(map(int,input().split()))
    return User_data

# To find the missing elements in an array
class Find_Missing_Numbers:
    def __init__(self,arr):
        self.x=arr
        self.n=len(arr)

    def append(self):
        missing=[]
        for i in range(self.x[0],self.x[-1]):
            if i not in self.x:
                missing.append(i)
        return missing

    def Formo_1(self):
        total = (self.n + 1)*(self.n + 2)/2
        sum_of_A = sum(self.x)
        return int(total - sum_of_A)

    def Formo_2(self):
        i, total = 0, 1
        for i in range(2, self.n + 2):
            total += i
            total -= self.x[i - 2]
        return total
    
    def Formo_3(self):
        self.n+=1
        n_elements_sum=self.n*(self.n+1)//2
        return n_elements_sum-sum(self.x)

    def Formo_4(self):
        return [(e1+1) for e1,e2 in zip(self.x, self.x[1:]) if e2-e1 != 1]

    def Formo_5(self):
        return [self.x[i] + 1 for i in range(self.n - 1) if self.x[i] + 1 != self.x[i + 1]]
        
    def modulo(self):
        x1 = self.x[0]
        x2 = 1
        for i in range(1, self.n):
            x1 = x1 ^ self.x[i]
         
        for i in range(2, self.n + 2):
            x2 = x2 ^ i
        return x1 ^ x2
 
if __name__ == '__main__':
    x = [1,2,3,4,5,7,8,9] 
    # x=getuserinput()
    func=Find_Missing_Numbers(x)
    print(func.Formo_5())