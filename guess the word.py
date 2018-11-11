# Biésów Smãtk
# Computer gets random word from list and then shuffle letters in it.
# Player got to guess, what was the original word.

import random

WORDS = ('szańdara', 'jinfòrmatik', 'kùch', 'wôrzta', 'prowadnik', 'kòmpùter', 'Żid', 'Kaszëba', 'gracz', 'czôłwiek', 'môłpa', 'szkòła', 'kluczplata', 'kam', 'grzib', 'rëba', 'rëbôk', 'zós', 'sér', 'wiéchrz', 'góra', 'kóń', 'bùla', 'knaga', 'proscé') #list of words used in game

input('Wcëskôj Enter, żebë kòmpùter pòcygnął kawel i nalôzł dlô Ce słowò.') #waiting for player to start

word = random.choice(WORDS) #seeking for random word from list

print ('Kòmpùter wëlosowôł słowò i mô pòprzestawióné w nim lëtre.\nMùsysz wëzgôdnąc, co to bëło za słowò.\nJeżlë wpiszesz \"end\", to skùńczisz jigrã rëchli.\n') #instructions for player

randomWord = word #gets the word for changes
end = len(randomWord) #checking words length
newRandomWord = ''

for i in range(end): #takes every letter in random order and place it as new string
	end = len(randomWord)
	letter = random.randrange(0,end)
	newRandomWord += randomWord[letter]
	randomWord = randomWord[:letter] + randomWord[letter+1:]
	
print (newRandomWord) #shows player shuffled letters
playersWord = input('\n') #player shoots until he guess or type 'end'
end = 'end'
while playersWord.lower() != word.lower():
	if playersWord.lower() == end.lower():
		input('\nDo ùzdrzeniégò!')
		exit()
	print('\nNié môsz zgadłé.')
	playersWord = input('\n')
print('\nJes wëzgôdł richtich.')

input('\nWcëskôj Enter,' #żebë wëlosowac pòsobné słowò abò Escape,
' żebë skùńczëc.')
