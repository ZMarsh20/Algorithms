import sys

# def pdrome(pos, word):
#     e = len(word) - 1
#     longest = [word[pos]]
#     long = ''
#
#     while word[e] != word[pos]:
#         e -= 1
#     if pos == e:
#         return word[pos]
#
#     longest.append(word[e])
#     longest.insert(1, '')
#     b = pos + 1
#
#     newWord = word[b:e]
#     for c in range(len(newWord)):
#         temp = pdrome(c, newWord)
#         if len(longest[1]) < len(temp):
#             longest[1] = temp
#
#     for char in longest:
#         long += char
#     return long
#
# def palindrome(word):
#     wordsDromes = {}
#     for i in range(len(word)):
#         wordsDromes[i] = pdrome(i, word)
#
#     longest = ''
#     for key in wordsDromes:
#         if len(wordsDromes[key]) > len(longest):
#             longest = wordsDromes[key]
#     return longest

def display(array, word):
    i = 0
    j = len(word) - 1
    msg = ''
    middle = ''
    while i <= j:
        if array[i+1][j-1] == 0:
            middle = word[j]
            if array[i][j] == 2:
                middle += word[j]
            break
        elif array[i][j] == array[i+1][j-1]:
            i += 1
            j -= 1
            continue
        if array[i][j-1] != array[i+1][j]:
            if array[i][j-1] == array[i][j]:
                j -= 1
                continue
            elif array[i+1][j] == array[i][j]:
                i += 1
                continue
        msg += word[j]
        i += 1
        j -= 1

    rev = ''
    for x in range(len(msg)-1, -1, -1):
        rev += msg[x]

    msg = msg + middle + rev
    return msg


def Palindrome(word):
    array = [[0 for _ in range(len(word))] for _ in range(len(word))]
    for i in range(len(word)):
        for j in range(len(word)-1, -1, -1):
            if j > i:
                continue
            if i == j:
                array[j][i] = 1
                continue
            if word[j] == word[i]:
                if word[j+1] == word[j]:
                    array[j][i] = array[j][i-1] + 1
                else:
                    array[j][i] = array[j+1][i-1] + 2
            else:
                array[j][i] = array[j+1][i]

            if array[j][i-1] > array[j][i]:
                array[j][i] = array[j][i-1]
            if array[j+1][i] > array[j][i-1]:
                array[j][i] = array[j+1][i]

    return display(array,word)



file = sys.argv[-1]
f = open(file, 'r')
s = f.readline().strip()
while (s != "#hw3_2a"):
    s = f.readline().strip()
words = f.readline().strip().replace(' ', '').upper().split(',')
for word in words:
    print("word: ", word, "\n\tpalin: ", Palindrome(word))
#    print("\tpalin: ", palindrome(word), "\n")
