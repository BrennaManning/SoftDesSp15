from pattern.en import sentiment
import numpy as np
import matplotlib.pyplot as plt

def sentiment_of_character(filename, character):
	"""
	takes txt file and character as inputs
	returns sentiment of that character's lines
	"""
	fp = open(filename) #this file is never closed
	text =''
	for line in fp:
		if line.startswith(character):
			text = text + line
	fp.close()
	return sentiment(text)

def sentiment_towards_character(filename, character):
	"""
	takes txt file and character as inputs
	returns sentiment of lines mentioning that character
	"""
	#Having docstrings is good, but there's no need to include them if your code self-comments
    fp = open(filename)
    text = ''
    for line in fp:
    	if character in line: #ex: Don't shy from having inline comments
    		text = text + line
    return sentiment(text)

def sent_of_character_in_play(text, CharSpeaking):
	"""
	takes txt file and list of characters speaking as inputs
	prints each character name, sentiment of each character's lines
	returns list of sentiments of each character's lines
	"""
	HeightsSentOf = []
	for char in CharSpeaking:
		print char, sentiment_of_character(text, char)[0]
		HeightsSentOf.append(sentiment_of_character(text, char)[0])
	return HeightsSentOf

def sent_towards_character_in_play(text, CharName):
	"""
	takes txt file and list of character names as inputs
	prints each character name, sentiment of lines mentioning each character
	returns list of sentiments of each character's lines
	"""
	HeightsSentTowards = []
	for char in CharName:
		print char, sentiment_towards_character(text, char)[0]
		HeightsSentTowards.append(sentiment_towards_character(text, char)[0])
	return HeightsSentTowards

def bargraph(Heights,xaxislabel,title):
	"""
	Takes Heights of each bar(sentiment levels),
	xaxislabel(list oc character names), and a plot title
	Creates bargraph of sentiment analysis data
	"""
    y = Heights
    N = len( y )
    x = range( N )
    width = 1/1.5
    plt.bar( x, y, width, color="magenta" )
    plt.title(title)
    labels = xaxislabel
    ax = plt.gca()
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=70);
    plt.xlabel( 'Character' )
    plt.ylabel( 'Sentiment Level')
    plt.show()
	


#Characters from two plays - EX: Hamlet, The Importance of
HamletCharactersSpeaking = ['  Ham. ', '  Hor. ', '  Oph. ', '  Laer. ', '  King. ', '  Queen.', '  Pol. ', '  Ros. ', '  Guil. ', '  For. ']
HamletCharacterNames = ['Hamlet', 'Horatio', 'Ophelia', 'Laertes', 'King', 'Gertrude', 'Polonius', 'Rosencrantz', 'Guildenstern', 'Fortinbras']
EarnestCharactersSpeaking = ['Algernon.  ', 'Jack.  ', 'Cecily.  ', 'Gwendolen.  ', 'Lady Bracknell.  ', 'Miss Prism.  ', 'Chasuble.  ', 'Lane.  ', 'Merriman.  ']
EarnestCharacterNames = ['Algy', 'Jack', 'Cecily', 'Gwendolen', 'Lady Bracknell', 'Prism', 'Chasuble', 'Lane', 'Merriman']

#print sent_of_character_in_play('earnest.txt', EarnestCharactersSpeaking)
#bargraph(sent_of_character_in_play('hamlet.txt', HamletCharactersSpeaking), HamletCharacterNames, "Sentiment of Characters in Hamlet")
#bargraph(sent_towards_character_in_play('hamlet.txt', HamletCharacterNames), HamletCharacterNames, "Sentiment Towards Characters in Hamlet")
#bargraph(sent_of_character_in_play('earnest.txt', EarnestCharactersSpeaking), EarnestCharacterNames, "Sentiment of Characters in Importance of Being Earnest")
bargraph(sent_towards_character_in_play('earnest.txt', EarnestCharacterNames), EarnestCharacterNames, "Sentiment Towards Characters in Importance of Being Earnest")





#bargraph(HeightsSentTowards,HamletCharacterNames, "Sentiment Towards Characters")
