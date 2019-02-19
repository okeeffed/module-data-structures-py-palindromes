import re


def isPalindrome(string):
    reStr = re.sub("[^a-zA-Z]", "", string).strip().lower()
    return reStr[::-1] == reStr
