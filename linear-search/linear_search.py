def linear_search(lst, to_find):
  for i in lst:
    if i==to_find: 
      return lst.index(i)
    return -1
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
