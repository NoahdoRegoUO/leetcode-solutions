class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")" or s[i] == "}" or s[i] == "]":
                if stack != []:
                    popped = stack.pop()
                    if (
                        (s[i] == ")" and popped != "(")
                        or (s[i] == "}" and popped != "{")
                        or (s[i] == "]" and popped != "[")
                    ):
                        return False
                else:
                    return False
            else:
                return False

        if stack == []:
            return True
        else:
            return False
