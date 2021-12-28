# Function to find permutations of a given string
from itertools import permutations
  
def allPermutations(data):
       
     # Get all permutations of string
     permList = permutations(data)
     out =[]
     for perm in list(permList):
         out.append((''.join(perm)))
  
     return(out)
# Driver program
if __name__ == "__main__":
    testCases = int(input())
    for _ in range (testCases):
      case = input()
      text = input()  
      perms = allPermutations(case)
      out = 'NO'
      for i in perms:
        if i in text:
          out = 'YES'
          break
      print(out)