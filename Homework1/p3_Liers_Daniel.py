# Finds a duplicate substring of a given length
def find_dup_str(s, n):
    # Any string with a duplicate length of 4 or more will not show
    if n >= 4:
      return ""

    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        for j in range(i + n, len(s) - n + 1):
            other = s[j:j + n]
        if substring == other:
         return substring
    return ""
# Finds the longest duplicate substring
def find_max_dup(s):
    n = len(s)
    while n > 0:
        result = find_dup_str(s, n)
        if result != "":
            return result
        n = n - 1
    return ""

# This is be the terminal input and will show results
s = input("Enter a string: ")
result = find_max_dup(s)
print(result)