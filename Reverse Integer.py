class Solution:
    def reverse(self, x):
        self.x=x
        INT_MIN=-2147483648
        INT_MAX=2147483648
        sign=-1 if x<0 else 1
        x=abs(x)
        if x<(INT_MIN):
            print("Input is below minimum")
        elif x>(INT_MAX):
            print("Input is above maximum")
        else:
            rev=0
            while x!=0:
                d=x%10
                rev=rev*10+d
                x//=10
            rev*=sign
        rev= rev if (rev>INT_MIN and rev<INT_MAX) else 0
        return rev


        
