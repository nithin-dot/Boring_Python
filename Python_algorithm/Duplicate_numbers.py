#! /usr/bin/python
def getuserinput():
    User_data=list(map(int,input().split()))
    return User_data

# To remove the duplicate methods
class remove_depulicate:

#real	0m0.156s
#user	0m0.498s
#sys	0m0.439s
    def Repeat(x):
        _size = len(x)
        repeated = []
        for i in range(_size):
            k = i + 1
            for j in range(k, _size):
                if x[i] == x[j] and x[i] not in repeated:
                    repeated.append(x[i])
        return repeated

#real	0m0.023s
#user	0m0.019s
#sys	0m0.004s
    def count(x):
        new = [] 
        for a in x: 
            n = x.count(a) 
            if n > 1:        
                if new.count(a) == 0: 
                    new.append(a)
        return new
    
#real	0m0.055s
#user	0m0.050s
#sys	0m0.004s
    def append(x):
        f_list=[]
        O_list=[]
        for i in x:
            if i not in f_list:
                f_list.append(i)
            else:
                O_list.append(i)
        return list(set(O_list))

#real	0m0.051s
#user	0m0.032s
#sys	0m0.020s
    def remove(x):
            O_list=list(set(x))
            for i in range(len(O_list)):
                x.remove(O_list[i])
            return list(set(x))

#real	0m0.051s
#user	0m0.047s
#sys	0m0.004s
    def dictmethod(x):
        duplicate={}
        for i in x:  
            duplicate[i]=duplicate.get(i,0)+1
        return [k for k,v in duplicate.items() if v>1]

#real	0m0.051s
#user	0m0.032s
#sys	0m0.020s
    def fillamb(x):
        x.sort()
        res=set(map(lambda a: a[0], filter(lambda a: a[0] == a[1], zip(x, x[1:]))))
        return res

if __name__ == '__main__':
    x = [1,2,1,201,201,3,4,5,1,1,2,5,6,7,8,9,9] 
    # x=getuserinput()
    func=remove_depulicate
    print(func.append(x))