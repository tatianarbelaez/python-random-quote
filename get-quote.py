import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last)
  print("first: " + quotes[rnd].rstrip())
  print("second: " + quotes[rnd1].rstrip())
  #rstrip quita todo tipo de espacios en blanco

if __name__== "__main__":
  primary()
