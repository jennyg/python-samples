#This is an English to Pig Latin translator I wrote in a Codecademy tutorial.
#todo, this followed the rules of the exercise, but it should really be first consonant(s) before a vowel, not first consonant

original = raw_input('Type a word: ') #Declares a variable for a word entered by a user.
#First, it validates the word -- no characters besides letters, and at least one letter.
if (len(original) > 0 and original.isalpha()) == True: 
	#These are the rest of the variables:
	word = original.lower() #Makes the word lowercase so it's easier to translate.
	first = word[0] #Grabs the first letter of the user's word.
	ay = 'ay' #The two letters that are the heart and soul of Pig Latin :)
	vowel_translation = word + ay
	consonant_translation = word[1:] + first + ay
	#This is the translator.
    	#Checks whether the word begin with a vowel or a consonant.
    	if first in 'aeiou':
        	print vowel_translation
    	else:
        	print consonant_translation
else:
	print 'Sorry, that won\'t work.'
