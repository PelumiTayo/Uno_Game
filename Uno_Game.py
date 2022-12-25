
#Pelumi Tayo-Orisadare

#Three goals or areas of focus
#input(player1 vs player2), dictionary(for the decks),  and (Functions with in functions (ex. playgame())


import random

newdeck = {}
num = [0,1,2,3,4,5,6,7,8,9]
c = ['red','blue','yellow','green']

def deck():
    '''
sig: list--> dic
created a deck with in a dictionary. Assigns colors to numbers. Making the number values and the colors the keys
'''
    global newdeck #global variable of the main deck
    newdeck = {}
    for colours in c:
	    for numbers in num:
		    if colours not in newdeck:
			    newdeck[colours] = []
		    newdeck[colours].append(numbers)
    return newdeck

def shuffle():
    '''
sig: shuffles the deck
'''
    for colours in c:
        random.shuffle(newdeck[colours])
    return newdeck

def createhand():
    '''
sig: assigning 7 random cards from the global new deck to each player and adding them to a new dictionary
'''
    deck = {}
    i=0
    while i<7:
        randcolor = random.randint (0, len(c)-1)
        index = random.randint(0, len(newdeck[c[randcolor]])-1)#gives a random number from the deck and gives it to the players. (-1) serves to equal lens to the index
        if c[randcolor] not in deck:
            deck[c[randcolor]] = [] 
        deck[c[randcolor]].append(newdeck[c[randcolor]][index])
        del newdeck[c[randcolor]][index]
        i += 1
    return deck

def printrules():
    '''
sig: printing th erules of the game
'''
    print('The rules of the game are as follows:''\n\n''Each players have 7 cards to start\n\nPlayer 1 will '
          +'put down their first cards then player 2 will put down a card that is either the same color or number'
          +'\n\nYou can only play with the cards you have in your deck\n\n'
          +'After 5 rounds the player with the least amount of cards wins\n')
printrules()

#Ingame
def createfirstcard():
    '''
sig: creating randomly a first card from the global deck to start off the game.
'''
    firstcard= {}
    randomcolor= random.randint(0,len(c)-1) #gives us a random color of the index c for the top card
    randomindex= random.randint(0,len(newdeck[c[randomcolor]])-1) # this is to find out how many value the color holds. In return gives us a random interger from that number
    firstcard[c[randomcolor]]= newdeck[c[randomcolor]][randomindex]
    del newdeck[c[randomcolor]][randomindex]
    return firstcard

def inputthecard(deck,firstcard): #first picking the color then number
    '''
sig: asking the player player what card number and color they would want to put down. Which gets added to a new pile
'''
    pile= {}
    while pile.keys() != firstcard.keys() and list(pile.values())!= list(firstcard.values()): # comparing the first card and the palyers first card
        playercolorcard= input('What color would you like to put down? Write none if you do not have the right color? ')#asking the players what card they would like to put down
        while playercolorcard not in deck.keys(): #player colors entered colors that is not in their deck. the game will ask them to put down colors they have already
            if playercolorcard== 'none':
                return firstcard #keeping the fist card the same
            else: #keeps asking the color they would like to put down
                playercolorcard= input('What color would you like to put down? Write none if you do not have the right color? ')
        playercolornumber= int(input('what number would like to pick from your deck. Pick -1 if you dont have the number? '))#asking for -1 because it is never in the deck, when player do not have the number
        while playercolornumber not in deck[playercolorcard]: #if number is not in color
            if playercolornumber == -1 :
                return firstcard
            else:
                playercolornumber= int(input('what number would like to pick from your deck. Pick -1 if you dont have the number? '))

        pile[playercolorcard]= playercolornumber
    return pile
def printvalues(deck):
    '''
sig: prints the values of the deck as list
'''
    i=0
    for key in deck.keys():
        deckvalues=list(deck.values())
        b= 0
        while (b<len(deckvalues[i])):
                     for element in deckvalues[i]:
                         print(str(key)+': '+str(element)+',', end =' ')
                         b+=1

        i+=1
    print('\n')

def Computerplay(deck,firstcard):
    '''
    sig: computer vs player 1 game
    '''
    firstcardspastin= list(firstcard.keys())
    deckcardvalue= sum(list(deck.values()),[])
    newfirstcard= {}
    value= list(firstcard.values())
    keys= list(deck.keys())
    if firstcardspastin[0] in keys and len(deck[firstcardspastin[0]]) != 0:
        value= len(deck[firstcardspastin[0]])
        index= random.randint(0,value-1)
        newfirstcard[firstcardspastin[0]]= deck[firstcardspastin[0]][index]
        return newfirstcard
    elif value[0] in deckcardvalue:
        c= list(deck.values())
        for x in range (len(c)):
            for y in range (len(c[x])):
                if value[0]== c[x][y]:
                    newfirstcard[keys[x]]= value[0]
        return newfirstcard

    else:
        return firstcard #if there is no number or color return firstcard
        
        
    
                
def playgame():
    '''
sig: starting the game of uno which takes on all the previus function
'''
    while True: #while the game is still going on
        printrules()
        deck()
        shuffle()
        players1hand=createhand()
        players2hand=createhand()
        firstcard= createfirstcard()
        roundcounter= 0
        counterplayer1cards= 0
        counterplayer2cards= 0
        countercomputercards=0 
        activeplayer= ('player1')
        playeranswer= input('Would you like to play with a computer or another player?\nType Yes if you want to play with a computer,'
                            +'or No if you want to play with another player. ')
        while playeranswer!= 'Yes' and playeranswer != 'No':
            playeranswer= input('Would you like to play with a computer or another player?\nType Yes if you want to play with a computer,'
                            +'or No if you want to play with another player. ')
            
        if playeranswer== 'Yes':
            while roundcounter < 10: #each players goes once in the round of 5, collectively 10
                if activeplayer== ('player1'):
                    print ("This is the first card:")
                    for key,value in firstcard.items():
                        print(key+': '+ str(value))
                    print ("Player 1 these are your cards")
                    printvalues(players1hand)
                    tempfirstcard= inputthecard(players1hand,firstcard)
                    if tempfirstcard != firstcard:
                        for key, value in tempfirstcard.items():
                            players1hand[key].remove(value)
                        counterplayer1cards +=1
                    firstcard= tempfirstcard
                    activeplayer= ('computer')
                elif activeplayer== 'computer':
                    print ("This is the first card:")
                    for key,value in firstcard.items():
                        print(key+': '+ str(value))
                    print('computer is playing...')
                    tempfirstcard= Computerplay(players2hand,firstcard)
                    
                    if tempfirstcard != firstcard:
                        for key, value in tempfirstcard.items():
                            players2hand[key].remove(value)
                        countercomputercards +=1
                    firstcard= tempfirstcard
                    activeplayer= ('player1')
                roundcounter +=1
            if counterplayer1cards > countercomputercards :
                print ('Congrats player 1 you won!! Thank you for playing this Uno Game')

            elif countercomputercards  > counterplayer1cards:
                print ('The computer won!! Thank you for playing this Uno Game')
            elif counterplayer1cards == countercomputercards :
                print ('It is a tie!! Thank you for playing this Uno Game')

            response= input('Would you like to play again? Type Yes or No. ')
            while response != 'Yes' and response != 'No':
                response= input('Would you like to play again? Type Yes or No. ')

            if response == ('No'):
                break
                
                    

        elif playeranswer== 'No':
            while roundcounter < 10: #each players goes once in the round of 5, collectively 10
                if activeplayer== ('player1'):
                    print ("This is the first card:")
                    for key,value in firstcard.items():
                        print(key+': '+ str(value))
                    print ("Player 1 these are your cards")
                    printvalues(players1hand)
                    tempfirstcard= inputthecard(players1hand,firstcard)
                    if tempfirstcard != firstcard:
                        for key, value in tempfirstcard.items():
                            players1hand[key].remove(value)
                        counterplayer1cards +=1
                    firstcard= tempfirstcard
                    activeplayer= ('player2')
                elif activeplayer==('player2'):
                    print ("This is the first card:")
                    for key,value in firstcard.items():
                        print(key+': '+ str(value))
                    print ("Player 2 these are your cards")
                    printvalues(players2hand)
                    tempfirstcard= inputthecard(players2hand,firstcard)
                    if tempfirstcard != firstcard:
                        for key, value in tempfirstcard.items():
                            players2hand[key].remove(value)
                        counterplayer2cards +=1
                    firstcard= tempfirstcard
                    activeplayer= ('player1')
                roundcounter +=1
            if counterplayer1cards > counterplayer2cards:
                print ('Congrats player 1 you won!! Thank you for playing this Uno Game')

            elif counterplayer2cards > counterplayer1cards:
                print ('Congrats player 2 you won!! Thank you for playing this Uno Game')
            elif counterplayer1cards == counterplayer2cards:
                print ('It is a tie!! Thank you for playing this Uno Game')

            response= input('Would you like to play again? Type Yes or No. ')
            while response != 'Yes' and response != 'No':
                response= input('Would you like to play again? Type Yes or No. ')
            if response == ('No'):
                print("Thank you for playing Uno!")
                break
        
        #player vs computer give em an option
        
        
playgame()



