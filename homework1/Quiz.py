i = 0
q = raw_input('1. Kakoy yazyk my uchim?:')
if q.upper() == 'PYTHON':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('2. Kak pishetsya funksiya vvoda?')
if q.upper() == 'INPUT()':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('3. Kak pishetsya funksiya vyvoda?')
if q.upper() == 'PRINT()':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')

q = raw_input('4. Kak nazivayutsya chisla s plavayushey tochkoy?')
if q.upper() == 'FLOAT':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('5. Kakoy operator konkatenacii?')
if q == '+':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('6. Sokrashenniy sintaksis else if:')
if q.upper() == 'ELIF':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('7. Strokoviy tip peremennih v python (sintaksis):')
if q.upper() == 'STR':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('8. Nazovite tsikl s predusloviem:')
if q.upper() == 'FOR':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('9. Nazovite tsikl s postusloviem:')
if q.upper() == 'WHILE':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
q = raw_input('10. Chislovoy tip peremennih v python (sintaksis):')
if q.upper() == 'INT':
    print('Verno!')
    i+=1
else:
    print ('Neverno!')
    
print ('Parvilnih otvetov: '+str(i)+' iz 10')
input()
