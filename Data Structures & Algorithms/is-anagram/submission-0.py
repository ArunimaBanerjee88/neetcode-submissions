class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      #1. Solution 1
        return sorted(s) == sorted(t) #----> SC = o(1)
        #2. Solution 2
        return Counter(s) == Counter(t) # -----> TC = O(S+T), SC = O(S+T)

        