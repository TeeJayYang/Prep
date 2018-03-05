class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = {'(', '{', '['}
        stack = []
        for i in s:
            # if it's a opening character then push onto stack
            if i in open: stack.append(i)
            # if it's a closing character and there's some opening
            # character before that hasn't been closed yet
            elif len(stack):
                if i == ')':
                    if stack[-1] != '(': return False
                elif i == '}':
                    if stack[-1] != '{': return False
                elif i == ']':
                    if stack[-1] != '[': return False
                stack.pop()
            # can't have a closing character without an opening first
            else: return False
        # if the stack still contains something that means
        # that there is an opening character without its partner
        return False if len(stack) else True
