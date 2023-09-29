class Solution:
    def intToRoman(self, num: int) -> str:
        d={
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        ans=""
        d=dict(reversed(list(d.items())))
        for i,j in d.items():
            if num//j:
                ans+=(i*(num//j))
                num=num%j
        return ans

        