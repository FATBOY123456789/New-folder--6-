class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
print('Welcome')
while True:
    word=input('Enter a word: ')
    meaning=input('Enter its meaning: ')
    flash.append(flashcard(word,meaning))
    option=int(input('Do you wish to continue? 1 for YES, 0 for NO: '))
    if not option:
     break

print('Your flashcard(s) is: ')
for c in flash:
    print('>',c)