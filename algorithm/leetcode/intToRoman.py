class Solution:
    def intToRoman(self, num: int) -> str:
        roman_symbol = ['I','V','X','L','C','D','M','','']
        idx_1 = 0
        idx_5 = 1
        idx_10 = 2
        
        num_tmp=num
        roman_num=[]
        while num_tmp>0:
            remainder = num_tmp % 10
            num_tmp = num_tmp//10
            
            r_1 = roman_symbol[idx_1]
            r_5 = roman_symbol[idx_5]
            r_10=roman_symbol[idx_10]
            
            if remainder==0:
                pass
            elif remainder<4:
                # r_1 * remainder
                roman_num.append(r_1*remainder)
            elif remainder==4:
                roman_num.append('%s%s'%(r_1,r_5))
            elif remainder < 9:
                # r_5+r_1 * remainder
                roman_num.append('%s%s'%(r_5, r_1*(remainder-5)))
            else: # 9
                roman_num.append('%s%s'%(r_1,r_10))
            
            idx_1 += 2
            idx_5 += 2
            idx_10 += 2
            
        roman_num.reverse()  
        return ''.join(roman_num)
        
###

def intToRoman1(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res, i = "", 0
    while num:
        res += (num//values[i]) * numerals[i]
        num %= values[i]
        i += 1
    return res
    
def intToRoman(self, num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res
