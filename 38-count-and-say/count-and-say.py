class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Base case
        s = "1"
        for _ in range(n - 1):
            next_s = ""
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                next_s += str(count) + s[i]
                i += 1
            s = next_s
        return s
