def multstring(s,n):
    concatena_s = ''
    for i in range(n):
        concatena_s += s
    return concatena_s

def array_count9(nums):
   cont = 0
   for i in nums:
      if i == 9: 
        cont +=1
   return cont

def string_splosion(s):
   splosion =''
   tam = len(s)
   for i in range(tam):
      splosion +=s[:i+1]
   return splosion

def array_front9(nums):
   for i in nums[:4]:
      if i==9:
         return True
   return False

def hello_name(name):
   ola = 'Hello '
   concatena = ola + str(name) +'!'
   return concatena

def make_tags(tab, word):
  return '<' + tab + '>' + word + '</' + tab + '>'

def extra_end(s):
  concatena = ''
  for i in range(3):
        concatena +=s[-2:]
  return concatena

def first_half(s):
  tam = len(s)
  metade = tam//2
  concatena = ''
  for i in range(metade):
   concatena +=s[i]
  return concatena

def sem_pontas(s):
  return s[1:-1]

def roda2(s):
  roda = s[:2]
  final = s[2:]
  return final + roda


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Multstring')
  test(multstring('Hi', 2), 'HiHi')
  test(multstring('Hi', 3), 'HiHiHi')
  test(multstring('Hi', 1), 'Hi')
  test(multstring('Hi', 0), '')
  test(multstring('Hi', 5), 'HiHiHiHiHi')
  test(multstring('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
  test(multstring('x', 4), 'xxxx')
  test(multstring('', 4), '')
  test(multstring('code', 2), 'codecode')
  test(multstring('code', 3), 'codecodecode')

  print ()
  print ('Array count 9')
  test(array_count9([1, 99, 9]), 1)
  test(array_count9([1, 9, 9]), 2)
  test(array_count9([1, 9, 9, 3, 9]), 3)
  test(array_count9([1, 2, 3]), 0)
  test(array_count9([]), 0)
  test(array_count9([4, 2, 4, 3, 1]), 0)
  test(array_count9([9, 2, 99, 3, 1]), 1)


  print ()
  print ('String Explosion')
  test(string_splosion('Code'), 'CCoCodCode')
  test(string_splosion('abc'), 'aababc')
  test(string_splosion('ab'), 'aab')
  test(string_splosion('x'), 'x')
  test(string_splosion('fade'), 'ffafadfade')
  test(string_splosion('There'), 'TThTheTherThere')
  test(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
  test(string_splosion('Bye'), 'BByBye')
  test(string_splosion('Good'), 'GGoGooGood')
  test(string_splosion('Bad'), 'BBaBad')

  print ()
  print ('Hello Name')
  test(hello_name('Bob'), 'Hello Bob!')
  test(hello_name('Alice'), 'Hello Alice!')
  test(hello_name('X'), 'Hello X!')
  test(hello_name('Hello'), 'Hello Hello!')

  print ()
  print ('Make Tags')
  test(make_tags('i', 'Yay'), '<i>Yay</i>')
  test(make_tags('i', 'Hello'), '<i>Hello</i>')
  test(make_tags('cite', 'Yay'), '<cite>Yay</cite>')
  test(make_tags('address', 'here'), '<address>here</address>')
  test(make_tags('body', 'Heart'), '<body>Heart</body>')
  test(make_tags('i', 'i'), '<i>i</i>')
  test(make_tags('i', ''), '<i></i>')

  print ()
  print ('Extra End')
  test(extra_end('Hello'), 'lololo')
  test(extra_end('ab'), 'ababab')
  test(extra_end('Hi'), 'HiHiHi')
  test(extra_end('Candy'), 'dydydy')
  test(extra_end('Code'), 'dedede')


  print ()
  print ('First Half')
  test(first_half('WooHoo'), 'Woo')
  test(first_half('HelloThere'), 'Hello')
  test(first_half('abcdef'), 'abc')
  test(first_half('ab'), 'a')
  test(first_half(''), '')
  test(first_half('0123456789'), '01234')
  test(first_half('kitten'), 'kit')

  print ()
  print ('Sem Pontas')
  test(sem_pontas('Hello'), 'ell')
  test(sem_pontas('Python'), 'ytho')
  test(sem_pontas('coding'), 'odin')
  test(sem_pontas('code'), 'od')
  test(sem_pontas('ab'), '')
  test(sem_pontas('Chocolate!'), 'hocolate')
  test(sem_pontas('kitten'), 'itte')
  test(sem_pontas('woohoo'), 'ooho')


  print ()
  print ('Roda 2')
  test(roda2('Hello'), 'lloHe')
  test(roda2('python'), 'thonpy')
  test(roda2('Hi'), 'Hi')
  test(roda2('code'), 'deco')
  test(roda2('cat'), 'tca')
  test(roda2('12345'), '34512')
  test(roda2('Chocolate'), 'ocolateCh')
  test(roda2('bricks'), 'icksbr')


if __name__ == '__main__':
  main()