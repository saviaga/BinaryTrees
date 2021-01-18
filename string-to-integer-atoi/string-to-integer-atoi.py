class Solution:
    def myAtoi(self, s: str) -> int:
        signs = '+-'
        numbers = '0123456789'
        final_number = ''
        i=0
        s = s.lstrip(' ')  #remove spaces
        if s=='' or s=='+' or s=='-': #this gets rid empty quotes right off the bat
            return 0
            
       
        if s[i] in '+-': # 2:Check next char is -/+ (if not already at the end of str) 
            if s[i+1] in '+-':
                return 0 
        
        if s[i] in '+-':
            final_number = final_number+ s[i]
            i+=1
        while i < len(s) and s[i] in numbers:
            final_number = final_number + s[i]
            i+=1            
            
        #Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0
        try:
            final_number = int(final_number)
        except:
            final_number = 0
        if int(final_number) <= -2**31:
            return -2**31
        elif int(final_number) > 2**31-1:
            return 2**31-1
        else:    
            return int(final_number)
        
            
​
                
            
                
            
        
