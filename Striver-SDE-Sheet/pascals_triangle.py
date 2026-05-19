class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def recfunc(n):
            if n==1:
                return [[1]]
            else:
                res = []
                tmp1 = recfunc(n-1)
                tmp = [0] + tmp1[-1] + [0]
                for i in range(len(tmp)-1):
                    res.append(tmp[i]+tmp[i+1])
                tmp1.append(res)
                return tmp1
        return recfunc(numRows)