import string

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alp = {char: index + 1 for index, char in enumerate(string.ascii_lowercase)}
        t = ''
        for x in s:
            t += str(alp[x])
        while k:
            ds = sum(int(x) for x in t)
            t = str(ds)
            k -= 1
        return ds
