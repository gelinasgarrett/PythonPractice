
# Pair sum problem: Find all pair sums within the array that are equivalent to 'n' total
def pair_sum(n, array):
  #In case the array is too small, return
  if (len(array) < 2):
    return
  
  #Track the currently viewed numbers in the array to compare to other values
  peeked = set()
  #Track the pairs found and store them in their own tuple
  pairs = set()

  #Iterate through the array, tar is the 'n' value minus the current array value
  for number in array:
    tar = n - number
    #If the target number is not in peeked(), add it as checked
    if tar not in peeked:
      peeked.add(number)
    else:
      #Add the two found values totaling 'n' together in order of smallest to largest numbers
      pairs.add((min(number, tar), max(number, tar)))

  #Print each couple on a new line from the pairs() list
  print('\n'.join(map(str, list(pairs))))

# Sample test case to run
pair_sum(10, [5,2,5,3,7,1,3,8])