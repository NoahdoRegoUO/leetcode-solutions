class Solution:
    def isValid(self, s: str) -> bool:
        while s != "":
            if len(s) % 2 != 0:
                return False
            else:
                if s == "()" or s == "{}" or s == "[]":
                    return True
                elif "()" in s:
                    s = s.replace("()", "")
                    if s == "":
                        return True
                elif "{}" in s:
                    s = s.replace("{}", "")
                    if s == "":
                        return True
                elif "[]" in s:
                    s = s.replace("[]", "")
                    if s == "":
                        return True
                else:
                    return False
        return False
