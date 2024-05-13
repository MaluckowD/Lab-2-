s = 'FGFBFHJKFNFBFBNNNNN'
max_el_count = 0
max_char = ''
for i in range(1,len(s)):
    if s[i - 1] == s[i + 1]:
        max_el_count += 1
        max_char = s[i]
print(max_el_count,max_char)