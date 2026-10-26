class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        array=[]
        for i in s:
            if i in '({[':
                array.append(i)
            elif len(array)==0:
                return False
            elif len(array)>0:
                if i==')' and array[-1]=='(':
                    array.pop()
                elif i==']' and array[-1]=='[':
                    array.pop()
                elif i=='}' and array[-1]=='{':
                    array.pop()
                else:
                    return False
        return len(array)==0
           


        