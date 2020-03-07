#a = 3 # Variable festlegen
'''print(a) #Ausgabe Wert
if 3 > 2:
    print('It works!')
if a == 2:
    print('OK')
else:
    print('Error')    
name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja': # zusätzliche Bedingung
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

volume = 57  # "volume" ist Englisch für "Lautstärke"
if volume < 20:
    #print("Das ist etwas leise.")
elif 20 <= volume < 40:
    #print("Das ist gut für Hintergrund-Musik.")
elif 40 <= volume < 60:
    print("Perfekt, ich kann alle Details hören.")
elif 60 <= volume < 80:
    print("Gut für Partys.")
elif 80 <= volume < 100:
    print("Etwas laut!")
else:
    print("Mir tun die Ohren weh! :(")    

def hallo():
    print("Halli-hallo!")
    print("Wie geht's?")

hallo()

def hallo2(name):
    if name == 'Ola':
        print('Hallo Ola!')
    elif name == 'Sonja':
        print('Hallo Sonja!')
    else:
        print('Hallo Unbekannte(r)!')

hallo2("Ola")

hallo2("Lisa")

def hallo3(name):
    print('Hallo ' + name + '!')

#hallo3("Rachel")'''



def hallo4(name):
    print('Hallo ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'du']
for name in girls:
    hallo4(name)
    print('Nächstes Mädchen')

for i in range(1, 6):
    print(i)