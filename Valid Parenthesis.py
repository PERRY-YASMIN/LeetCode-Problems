class Solution:
    def isValid(self, s):
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping.keys():
                if not stack or mapping[i] != stack.pop():
                    return False
        
        return not stack
