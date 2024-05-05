from random import choice
import random
import time

#create list of animes

titleLists = [
        #sad            #happy          #chill
    ['sadTitle 1', 'happyTitle 1', 'chillTitle 1'],
    ['sadTitle 2', 'happyTitle 2', 'chillTitle 2'],
    ['sadTitle 3', 'happyTitle 3', 'chillTitle 3'],
]

# title = choice(titleLists)

moodFiltered = []
result = ''

print("Some mood preferences?")
mood = input()

for item in titleLists:
    if mood == 'sad':
        moodFiltered.append(item[0])
    if mood == 'happy':
        moodFiltered.append(item[1])
    if mood == 'chill':
        moodFiltered.append(item[2])
    else:
        print('Let the destiny decide')
        row = random.randint(0, len(titleLists)-1)
        column = choice(titleLists[row])
        result = column
        time.sleep(2)
        print('Our winner is ---> ' + result)
        break

if result == '':
    print('Here are our results: ')
    for item in moodFiltered:
        print(item)
    print('Are you ready to spin the wheel?!')
    input()
    print('Here is our winner: ' + choice(moodFiltered).upper())
