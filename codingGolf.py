def cap(S):
  S = S.split()
  t = ""
  for w in S:
    t = t + w[0].upper()
    for i in range(1,len(w)):
      t = t + w[i]
    if w != S[-1]:
      t = t + " "
  return t