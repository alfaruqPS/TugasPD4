print('Nama:Abu Nur Al-Faruq')
print('Kelas:Ti22E')
print('Nim:20220040223')

X = 16
Y = 32
print('X =', X, '=', format(X, '08b')) 
print('Y =', Y, '=', format(Y, '08b'), '\n')

print('[and]') 
print('X & Y =', X & Y) 
print(format(X, '08b'), '^', format(Y, '08b'), '=', format(X & Y, '08b'), '\n')

print('[or]') 
print('X | Y =', X | Y) 
print(format(X, '08b'), '|', format(Y, '08b'), '=', format(X | Y, '08b'), '\n')

print('[not]') 
print('~X ~Y =', ~X, ~Y) 
print('~' + format(X, '08b'), '~' + format(Y, '08b'), '=', format(~X, '08b'), format(~Y, '08b'), '\n')