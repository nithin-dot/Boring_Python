class pyramid:
    def __init__(self,n):
        self.n=n
    def half_pyramid(self):
        for no_rows in range(self.n):
            for no_columns in range(no_rows+1):
                    print('* ',end="")
            print("\r")
    def Right_Start_Pattern(self):
        self.half_pyramid()
        for no_rows in range(self.n,1,-1):
            for no_columns in range(no_rows-1):
                print('* ',end="")
            print("\r")
    def pyramid_pattern(self):
        k = 2 * self.n - 2
        for no_rows in range(self.n):
           for no_columns in range(k):
               print(end=" ")
           k = k - 1
           for no_columns in range(no_rows+1):
                print("*", end=" ")
           print("\r")
    def reverse_pyramid_pattern(self):
        k = 2 * self.n - 2
        for no_rows in range(self.n,-1,-1):
           for no_columns in range(k,0,-1):
               print(end=" ")
           k = k + 1
           for no_columns in range(no_rows+1):
                print("*", end=" ")
           print("\r")
    def reverse_half_pyramid(self):
        k=2*self.n-2
        for no_rows in range(self.n):
            for no_columns in range(k):
                    print(end=" ")
            k=k-2
            for no_columns in range(no_rows+1):
                  print("*",end=" ")
            print("\r")
    def reverse_Right_Start_Pattern(self):
        self.reverse_half_pyramid()
        k=-1
        for no_rows in range(self.n-1,-1,-1):
            for no_columns in range(k,-1,-1):
                    print(end=" ")
            k=k+2
            for no_columns in range(no_rows+1):
                  print("*",end=" ")
            print("\r")
if __name__ == "__main__" :
    pyramid=pyramid(5)
    pyramid.reverse_Right_Start_Pattern()