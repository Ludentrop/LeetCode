class Solution:
    def intToRoman(self, data: int) -> str:
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thous = ["","M","MM","MMM","MMMM"]

        t = thous[data // 1000]
        h = hunds[data // 100 % 10]
        te = tens[data // 10 % 10]
        o =  ones[data % 10]

        return t+h+te+o
