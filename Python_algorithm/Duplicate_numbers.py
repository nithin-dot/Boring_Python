#! /usr/bin/python
# Here X is denoted as Array input
def getuserinput():
    User_data=list(map(int,input().split()))
    return User_data

# To remove the duplicate methods
class remove_depulicate:
    def __init__(self,arr):
        self.x=arr
#real	0m0.156s
#user	0m0.498s
#sys	0m0.439s
    def Repeat(self):
        _size = len(self.x)
        repeated = []
        for i in range(_size):
            k = i + 1
            for j in range(k, _size):
                if self.x[i] == self.x[j] and self.x[i] not in repeated:
                    repeated.append(self.x[i])
        return repeated

#real	0m0.022s
#user	0m0.013s
#sys	0m0.009s
    def hasing(self): 
        mdict ={}
        res_List =[]
        for num in self.x:
            if num not in mdict:
                mdict[num] = 1
            else:
                mdict[num] += 1
        print(mdict)
        for key, value in mdict.items():
            if value > 1:
                res_List.append(key)
    
        return [-1] if not res_List else sorted(res_List)
#real	0m0.023s
#user	0m0.019s
#sys	0m0.004s
    def count(self):
        new = [] 
        for a in self.x: 
            n = self.x.count(a) 
            if n > 1:        
                if new.count(a) == 0: 
                    new.append(a)
        return new
    
#real	0m0.055s
#user	0m0.050s
#sys	0m0.004s
    def append(self):
        f_list=[]
        O_list=[]
        for i in self.x:
            if i not in f_list:
                f_list.append(i)
            else:
                O_list.append(i)
        return list(set(O_list))

#real	0m0.051s
#user	0m0.032s
#sys	0m0.020s
    def remove(self):
            O_list=list(set(self.x))
            for i in range(len(O_list)):
                self.x.remove(O_list[i])
            return list(set(self.x))

#real	0m0.051s
#user	0m0.047s
#sys	0m0.004s
    def dictmethod(self):
        duplicate={}
        for i in self.x:  
            duplicate[i]=duplicate.get(i,0)+1
        return [k for k,v in duplicate.items() if v>1]

#real	0m0.051s
#user	0m0.032s
#sys	0m0.020s
    def fillamb(self):
        self.x.sort()
        res=set(map(lambda a: a[0], filter(lambda a: a[0] == a[1], zip(self.x, self.x[1:]))))
        return res

if __name__ == '__main__':
    x = [1,2,1,201,201,3,4,5,1,1,2,5,6,7,8,9,9] 
    # self.x=getuserinput()
    func=remove_depulicate(x)
    print(func.hasing())