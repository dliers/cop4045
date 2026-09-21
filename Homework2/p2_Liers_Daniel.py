"""
@author: Daniel Liers
ZNumber: 23716566
"""
#Part A
result_a = [(a, b, c, d)
            for a in range(1, 11)
            for b in range(1, 11)
            for c in range(1, 11)
            for d in range(1, 11)
            if a != b and a != c and a != d
            and b != c and b != d and c != d
            and a**2 + b**2 == c**2 + d**2]

print("a)", result_a)
#Part B
strings = ['One', 'SEVEN', 'three', 'two', 'Ten']
result_b = [(word.lower(), len(word))
            for word in strings
            if len(word) < 5]

print("b)", result_b)
#Part C
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
result_c = [name.split()[0] + " " + name.split()[1][0] + ". " + name.split()[2]
            for name in names]

print("c)", result_c)
#Part D
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

result_d = [(w1, w2)
            for w1 in lst1
            for w2 in lst2
            if sorted(w1.lower()) == sorted(w2.lower())]

print("d)", result_d)
#Part E
s = ['one', 'two', 'three']

result_e = {word: len(word) for word in s}

print("e)", result_e)
#Part F
text = "Hello world"

result_f = {}
i = 0

for c in text:
    if c.lower() in "aeiou":
        result_f[i] = c
    i = i + 1

print("f)", result_f)