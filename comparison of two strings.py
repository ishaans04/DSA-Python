class Solution: 
    def compares(self,s1,s2):
        return s1==s2

if __name__=="__main__":
    s=Solution()
    s1=str(input("Enter string 1 : "))
    s2=str(input("Enter String 2 : "))

    if s.compares(s1,s2):
        print("Strings are equal")
    else:
        print("Strings not equal")