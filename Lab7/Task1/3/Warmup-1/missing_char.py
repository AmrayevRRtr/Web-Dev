def missing_char(str, n):
  s = ""
  for i in range(len(str)):
    if i == n: continue
    s += str[i]
  return s
