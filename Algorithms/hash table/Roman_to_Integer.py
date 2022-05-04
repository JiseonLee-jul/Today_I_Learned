class Solution:
    def romanToInt(self, s: str) -> int:
        out_list = []
        roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(len(s)):
            out_list.append(roman_dict[s[i]])
        for i in range(len(out_list)-1):
            if out_list[i] < out_list[i+1]:
                out_list[i+1] = out_list[i+1] - out_list[i]
                out_list[i] = 0
        
        return sum(out_list)
