from random import randrange
n = int(input('Введите количество строк '))

def fill_file():
    with open('Data.txt','w') as file:
        for _ in range(n):
            cnt = randrange(10, 30 + 1)
            s = ''.join([chr(randrange(ord('A'), ord('Z') + 1)) for _ in range(cnt)])
            file.write(s + '\n')

def find_number_char():
    with open('Data.txt','r') as file:
        max_len = 0
        line, number = 0, 0
        for s in file:
            line = line + 1
            curr = 1
            for i in range(len(s)):
                if s[i] < s[i-1]:
                    curr += 1
                    if curr > max_len:
                        max_len = curr
                        number = line
                        p = s
                else:
                    curr = 1

        frequency = {}
        max_freq = 0
        most_common_char = ''

        for i in range(1, len(p) - 1):
            if p[i - 1] == p[i + 1]:
                if p[i] in frequency:
                    frequency[p[i]] += 1
                else:
                    frequency[p[i]] = 1
                if frequency[p[i]] > max_freq:
                    max_freq = frequency[p[i]]
                    most_common_char = p[i]
                elif frequency[p[i]] == max_freq:
                    most_common_char = max(most_common_char, p[i])
    print(max_len, max_freq, p)
    return number, most_common_char

def write_results(number, most_common_char):
    with open('Result.txt','w') as file:
        if number == 0:
            file.write('В файле нет строк, содержащих убывающую последовательность.\n')
        else:
            file.write('Искомая строка - {}.\n'.format(number))
            file.write('Искомый символ - {}.\n'.format(most_common_char))


fill_file()
number, most_common_char = find_number_char()
print(number,most_common_char)
write_results(number, most_common_char)