def linear_search(lst, to_find):
  for i in range(len(lst)):
    if i == to_find:
      return i
  else:
    return -1
