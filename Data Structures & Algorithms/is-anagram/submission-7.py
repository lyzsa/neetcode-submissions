class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {};
        d2 = {};
        if (len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            if s[i] not in t:
                return False;
            
            if s[i] not in d1:
                d1[s[i]] = 0;
            else:
                d1[s[i]] += 1;

            if t[i] not in d2:
                d2[t[i]] = 0;
            else:
                d2[t[i]] += 1;
            
        for key in d1:
            if(d1[key] != d2[key]):
                return False
                
        return True




            
        