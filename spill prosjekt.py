from random import *
ordene = ['sushi', 'nudler', 'ramen', 'dumplings', 'taco', 'pizza', 'salat']

"""for å få et randomt ord spilleren kan gjette"""
def getword(ordliste):
    n = randint(0,len(ordene)-1)
    return ordliste[n]


"""spill displayet"""
print('Jeg tenker på en type mat, kan du gjette hva det er? \n ') 
def display(word, wrongletters, rightletters, chance):
    print('Du har {:n} sjanser igjen'.format(chance).center(40,'-'))
    print('Bokstaver du har gjettet feil: ', wrongletters)
    print()
    blanks = '_' * len(word) #slik at den viser like mange understrek som ordet den har valgt
    for i in range(len(word)):
        if word[i] in rightletters:
            blanks = blanks[:i] + word[i] + blanks[i+1:]    #gjør strekene om til bokstaver for de bokstavene man gjetter riktig
    for i in blanks:
        print(i + ' ', end = ' ')
    print()
    print()
    
    
""""få en bokstav av spilleren"""
def getletter(alreadyguessed):
    while True:
        print('Gjett en bokstav: ')
        guess = input()
        guess = guess.lower()
        if guess[0] in alreadyguessed:
            print('Du har allerede gjettet denne bokstaven!')
        else:
            return guess[0]
        
"""spille igjen?"""
def playagain():
    print('Vil du spille ijgen? (y/n) ')
    s = input()
    s = s.lower()
    if s[0] == 'y':
        return 1
    return 0

"""spillet"""
wrongletters = ' '
rightletters = ' '
word = getword(ordene)
chance = 6 #starter med 6 sjanser
done = False

while True:
    display(word, wrongletters, rightletters, chance) #gir instruksjoner, velger et ord og viser hvor mange bokstaver det består av
    
    guess = getletter(wrongletters + rightletters) #gjør at spilleren kan begynne å gjette
    
    if guess in word: 
        rightletters = rightletters + guess #legger til riktig bokstav i rightletters hvis det er gjettet riktig
        foundall = True #loopen går
        for i in range(len(word)): #slik at det sjekker for hver og en bokstav i ordet
            if word[i] not in rightletters: #hvis man gjetter en bokstav som ikke er i ordet
                foundall = False #slik at loopen slutter der når det er feil, og gjette igjen
                break
        if foundall: 
            print('Så flink du var, ordet er ', word, ', du greide det!') #hvis det finner alle 
            done = True
            
    else:
        wrongletters = wrongletters + guess
        chance = chance - 1 #en mindre sjanse hvis man gjetter feil
        if chance == 0: #når man har brukt opp alle sjansene
            display(word, wrongletters, rightletters, chance)
            print('Du har ikke flere sjanser, du har gjettet feil', str(len(wrongletters)), 'ganger, riktig', str(len(rightletters)), 'ganger, riktig ord er: ' , word)
            done = True #ferdig
            
    if done:
        if playagain():
            wrongletters = ' ' #setter wrong og right letters lik ingenting igjen
            rightletters = ' '
            word = getword(ordene) #velger et nytt ord
            chance = 6
            done = 0
        else:
            print('Takk for spillet! ')
            break


































