# Function that will return a list with tuples (a,b,c)
def find_Pythagorean(n):

    triples = []
    for a in range(1, n + 1):
     for b in range(1, n + 1):
      for c in range(1, n + 1):
          
          # This will check if a, b, and c satisfy the Pythagorean theorem
          if a**2 + b**2 == c**2:
           triples.append((a, b, c))
    return triples
# We are going to use a while loop to create an infinite loop to test multiple values
while True:
    n = input("Enter n: ")
    if n == "":
        break

    n = int(n)
    triples = find_Pythagorean(n)
    print(triples)