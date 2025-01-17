import random

def cislice(num):
  return [int(i) for i in str(num)]


def dupcisla(num):
  num_li = cislice(num)
  if len(num_li) == len(set(num_li)):
    return True
  else:
    return False

def gencislo():
  while True:
    num = random.randint(1000, 9999)
    if dupcisla(num):
      return num

def pocetBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = cislice(num)
    guess_li = cislice(guess)

    for i,j in zip(num_li,guess_li):

        # cislice tam je
        if j in num_li:

            # presne trefena cislice
            if j == i:
                bull_cow[0] += 1

            # cislice tam je ale jina pozice
            else:
                bull_cow[1] += 1

    return bull_cow



num = gencislo()
tries =int(input('napis pocet pokusu: '))


while tries > 0:
    guess = int(input("zacni hadat: "))

    if not dupcisla(guess):
        print("cislice se nesmi opakovat")
        continue
    if guess < 1000 or guess > 9999:
        print("cislo musi obsahovat 4 cislice")
        continue

    bull_cow = pocetBullsCows(num, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1

    if bull_cow[0] == 4:
        print("Spravne!")
        break
else:
    print(f"Uz nemate zadny pokus. Cislo bylo: {num}")

