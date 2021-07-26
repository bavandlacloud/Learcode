

#tree cups game

mylist=[' ','O',' ']

def myshuffle(listofnum):
    from random import shuffle
    shuffle(listofnum)
    return listofnum

def takeinput():
    guess=''
    while guess not in ['0','1','2']:
        
        guess = input("pick a number 0,1 or 2")
    return int(guess)


def check_for_bingo(game,indexgiven):
    if game[indexgiven]=='O':
        print("bingo guess is correct")
    else:
        print("try next time")
        print(game)

myshuffled_list = myshuffle(mylist)
payer_input=takeinput()
check_for_bingo(myshuffled_list,payer_input)


