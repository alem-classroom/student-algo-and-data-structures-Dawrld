def linear_search(lst, to_find):
  for i in range(lst):
    if lst[i]==to_find:
      return i
  else:
    return -1
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
