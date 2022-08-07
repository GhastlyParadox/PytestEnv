
class ValueGenerator:

    def __init__(self):
        pass

    @staticmethod
    def fibArr(n: int):
        if n < 2: 
            return n
        dp = [0, 1]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp

    @staticmethod
    def factArr(n: int):
        if n <= 2:
            return n
        dp = [1]
        for i in range(1, n + 1):
            dp.append(i * dp[i-1])
 
        return dp

