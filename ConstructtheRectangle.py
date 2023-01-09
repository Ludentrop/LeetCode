class Solution:
    def is_prime(self, n):
        self.n = n
        flag = True

        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                flag = False
        if flag and n > 1:
            return True
        return False

    def constructRectangle(self, area: int) -> List[int]:
        if area < 4:
            return [area, 1]
        elif str(area ** .5)[-1] == '0':
            return [int(area**.5), int(area**.5)]
        elif self.is_prime(area):
            return [area, 1]
        else:
            sqr = int(area**.5)
            if str(area / sqr)[-1] == '0':
                return [area//sqr, sqr]
            else:
                while area % sqr != 0:
                    sqr -= 1
                return [area//sqr, sqr]
