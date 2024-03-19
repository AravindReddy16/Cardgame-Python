import random
SUIT=('spade','club','diamond','heart')
RANK=('ace','2','3','4','5','6','7','8','9','10','jack','queen','king')
chances=7
def getCard(DeckListIn):
    pickCard=DeckListIn.pop()
    return pickCard
def shuffle(DeckList):
    DeckListOut=DeckList.copy()
    random.shuffle(DeckListOut)
    return DeckListOut
StartDeck=[]
for suit in SUIT:
    for value,rank in enumerate(RANK):
        cardpairs={'rank':rank,'suit':suit,'value':value+1}
        StartDeck.append(cardpairs)
while True:
    score = 50
    print(f'Your Score: {score}')
    print()
    currentCardList=shuffle(StartDeck)
    getDeckCard=getCard(currentCardList)
    currentRank=getDeckCard['rank']
    currentValue=getDeckCard['value']
    currentSuit=getDeckCard['suit']
    print(f'Current Card is "{currentRank}" of Suit "{currentSuit}"')
    print()
    for chance in range(chances+1):
        answer=input(f'Enter whether the next card is higher or lower than "{currentRank}" (h/l): ').lower()
        nextCardList=shuffle(StartDeck)
        nextDeckCard=getCard(currentCardList)
        nextRank=nextDeckCard['rank']
        nextValue=nextDeckCard['value']
        nextSuit=nextDeckCard['suit']
        print(f'Your Card is "{nextRank}" of Suit "{nextSuit}"')
        print()
        if answer=='h':
            if nextValue > currentValue:
                print(f'You got right that is high...')
                print()
                score+=20
                print(f'Your Score: {score}')
                print()
            else:
                print(f'You got wrong that is high...')
                print()
                score-=15
                print(f'Your Score: {score}')
                print()
        elif answer=='l':
            if nextValue < currentValue:
                print(f'You got right that is low...')
                print()
                score+=20
                print(f'Your Score: {score}')
                print()
            else:
                print(f'You got wrong that is low...')
                print()
                score-=15
                print(f'Your Score: {score}')
                print()
        currentRank=nextRank
        currentValue=nextValue
    gohead=input('Enter you want to continue press "enter" or not to press "q": ')
    print()
    if gohead=='q':
        break
print('Good Bye')