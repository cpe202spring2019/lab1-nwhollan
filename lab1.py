
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
      return None
   if int_list == None:
      raise ValueError
   max_val = int_list[0]
   for i in int_list:
       if i > max_val:
           max_val = i
   return max_val

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
       raise ValueError
   if len(int_list) == 0:
       return int_list
   latestnum = []
   latestnum.append(int_list[0])
   return reverse_rec(int_list[1:]) + latestnum


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
       raise ValueError
   if int_list[(high + low)//2] == target:
      return (high + low)//2
   if int_list[high] == target:
      return high
   if (high - low) == 1:
      return None
   if len(int_list) == 1:
       if int_list[0] != target:
          return None
   if int_list[(high + low)//2] > target:
      high = (high + low)//2
      return bin_search(target, low, high, int_list)
   if int_list[(high + low)//2] < target:
      low = (high + low)//2
      return bin_search(target, low, high, int_list)
