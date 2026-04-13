def contains_duplicate(input)-> bool:
  if len(input) != len(set(input)):
    return True
  return False
