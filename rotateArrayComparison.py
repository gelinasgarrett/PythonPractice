
#Takes in two lists that could or could not be equal when rotated either direction
def rotateArrComparison(list1, list2):
  # Cancel comparison if list lengths are different, inner elements could never be the same once rotated
  if(len(list1) != len(list2)):
    return False

  # Mark the first element of the first list as a starting point
  start_mark = list1[0]
  start_index = 0

  #Loop through the range of list 2, find the common element matching 'start_mark'
  for i in range(len(list2)):
    if list2[i] == start_mark:
      start_index = i
      break
  
  #If the index has not changed, then there is no matching element to compare to list one
  if start_index == 0:
    return False

  #Otherwise, begin looping through list 1 to compare to list 2
  for x in range(len(list1)):
    #Finds the current index of list 2 by adding the start_index to the current x iteration, using the remainder to 
    # make sure it starts at the beginning in the event one list is ahead of the other
    list2_index = ((start_index + x) % (len(list1)))

    #If there is an occurance where the two list elements no longer match, immediately return False
    if list1[x] != list2[list2_index]:
      return False

  #If all conditions are met, return True
  return True

# Returns True
print(rotateArrComparison([1,3,5,7,9,0], [9,0,1,3,5,7]))
# Returns False
print(rotateArrComparison([1,3,5,5,5,0], [9,2,1,3,5,7]))
