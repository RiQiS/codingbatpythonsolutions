def round_sum(a, b, c):
  return(round10(a)+round10(b)+round10(c))
  
def round10(num):
  quot, rem = divmod(num, 10)
  if rem>=5:
    quot+=1
  return quot * 10
