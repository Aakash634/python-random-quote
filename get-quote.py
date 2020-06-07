import random
def main2():
 #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=13
  rnd=random.randint(0,last+1)
  s=sum([rnd]+[rnd])
  
  print(rnd)
  print([s])
  print(quotes[rnd])
  print(quotes[14])

if __name__== "__main__":
  main2()
