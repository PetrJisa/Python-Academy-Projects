TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# Vytvoření listu s uživatelskými jmény a jejich hesly + vytvoření oddělovače
users = ('bob','ann','mike','liz')
passwords = ('123','pass123','password123','pass123')
up_dict = dict(zip(users,passwords))        #Nebylo by třeba tvořit dict a for loop se dal napsat s listy, ale mám rád funkci zip :-)
oddelovac = 20*'-'

# Přihlašovací dialog s uživatelem
# Přestože zadání neobsahuje tento prvek, dávám uživateli možnost 3 pokusů k přihlášení
for i in range(3):
    user = input('Please, enter your username: ')
    password = input('Enter your password: ')
    if  user not in up_dict.keys() or up_dict[user] != password:
        print('This is not a valid combination of username and password. Please, try again')
        print('Remaining attempts: ', 3-i-1)
    else:
        break
else:
    print('Maximal amount of log-in attempts was exceeded!')
    print('The program must be aborted!')
    exit()

# Uvítání uživatele v případě, že se úspěšně přihlásil
print(oddelovac)
print('Welcome to the app ', user)
print('We have 3 texts to be analysed')
print(oddelovac)

# Volba textu, který bude analyzován. Zde dávám uživateli 1 pokus na opravu
for i in range(2):
    volba_textu = int(input('Enter a number btw. 1 and 3 to select: '))
    if volba_textu not in range(1, 4):
        print('You did not provide a valid input. Please try once again')
    else:
        print(oddelovac)
        break
else:
    print('We are sorry but the program must be finished due to repeatable occurence of the improper input')

# Pokud se uživateli povedlo vybrat text, pokračuje se převodem textu na list a očištěním jeho jednotlivých prvků
text = TEXTS[volba_textu-1]
text_list = [slovo.strip('.,?!') for slovo in text.split()]

# Získání jednotlivých charakteristik textu
words_count = len(text_list)
numbers_sum = 0
numeric_strings = 0
titlecase = 0
uppercase = 0
lowercase = 0
for slovo in text_list:
    if slovo.isdigit():
        numbers_sum += int(slovo)
        numeric_strings += 1
    elif slovo.istitle():
        titlecase += 1
    elif slovo.isupper():
        uppercase += 1
    elif slovo.islower():
        lowercase += 1

# Tisk výsledků rozboru textu (kromě histogramu slov podle jejich délky)
print('There are ', words_count, ' words in the text.')
print('There are ', titlecase, ' titlecase words.')
print('There are ', uppercase, ' uppercase words.')
print('There are ', lowercase, ' lowercase words.')
print('There are ', numeric_strings, ' numeric strings.')
print('There sum of all numbers is ', numbers_sum)

# Proměnné pro tisk histogramu
delka_dict = {}
for slovo in text_list:
    delka_dict[len(slovo)] = delka_dict.get(len(slovo),0) + 1
max_delka = max(delka_dict.values())

# Tisk histogramu
print(oddelovac)
print('LEN', ' COUNT', (max_delka - 4)*' ', ' NO.')
for delka in sorted(delka_dict):
    pocet = delka_dict[delka]
    if delka < 10:
        print(delka, ' |', pocet * '*', (max_delka-pocet)*' ', '|', delka_dict[delka])
    else:
        print(delka, '|', pocet * '*', (max_delka - pocet) * ' ', '|', delka_dict[delka])


