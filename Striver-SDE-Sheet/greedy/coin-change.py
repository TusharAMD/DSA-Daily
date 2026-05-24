class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        hashmap = {}

        def recfunc(target):
            if target == 0:
                return 0
            if target < 0:
                return 10**10
            if target in hashmap:
                return hashmap[target]
            
            min_coins = 10**10
            for coin in coins:
                res = recfunc(target - coin)
                min_coins = min(min_coins, res + 1)
            hashmap[target] = min_coins
            return min_coins

        ans = recfunc(amount)
        return -1 if ans == 10**10 else ans
