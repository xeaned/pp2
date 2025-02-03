def permute(s, l=''):
    if len(s) == 0:
        print(l)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i+1:]
            permute(remaining, l + s[i])

input_str = input("string: ")
permute(input_str)