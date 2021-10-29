
def largest_sum(arr):
  if (len(arr) == 0):
    return
  
  max_sum = current_sum = arr[0]
  for num in arr[1:]:
    current_sum = max(current_sum + num, num)
    max_sum = max(current_sum, max_sum)

  return max_sum

print(largest_sum([7,8,4,-5,22,3,5,-9,12,15,-4]))
  