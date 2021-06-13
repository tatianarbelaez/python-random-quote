import random
def primary():
  #print("Keep it logically awesome.")
  new_quote = input("Por favor ingresa una nueva frase:\n")

  if len(new_quote) < 10:
    print("La frase es muy corta")
    exit(1)

  if len(new_quote) > 50:
    print("La frase es muy larga")
    exit(1)

  if new_quote.count(" ") < 1:
    print("Las frases tienen más de una palabra")
    exit(1)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  last_quote = quotes[last]

  f = open("quotes.txt", "a")

  if not last_quote.endswith("\n"):
    f.write("\n")

  f.write(new_quote + "\n")
  f.close()

  print("La frase fue escrita exitosamente!")

if __name__== "__main__":
  primary()