class Solution(object):
    def longestCommonPrefix(self, strs):
        no=""
        strs=sorted(strs)
        v1=strs[0]
        vl=strs[-1]
        for i in range(min(len(v1),len(vl))):
         if (v1[i] != vl[i]):
            return no
         no+=v1[i]
        return no
