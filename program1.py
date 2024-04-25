class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = list.pop() if list else '#'
                if mapping[char] != top_element:
                    return False
            else:
                list.append(char)
        return not list
    



  

