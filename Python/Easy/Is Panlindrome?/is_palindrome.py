def isPalindrome(phrase):
  clean_phrase = "".join(char for char in phrase if char.isalnum())
  clean_phrase = clean_phrase.lower()
  temp = clean_phrase[::-1]
  if temp == clean_phrase:
    return True
  return False
