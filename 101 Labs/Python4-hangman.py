# Ty Ridings
# CSCI 101 - Section
# 9/18/2019

sec_word1 = list(input('Enter a secret word: \nWORD> '))        #The Secret Word
i = int(input('Enter the amount of guesses allowed: \nNUM> '))  #The Number of guesses

guessed_letters = []        
dummy_word = ['_']*len(sec_word1)                                #Dummy Word with underscores
                
while i >0:               
    letter = input('\nGuess a letter: \nLETTER> ')
    guessed_letters.append(letter)
    i = i - 1
    
    if letter in sec_word1:      

        #Letter positions returns an array of places that letter occurs in Secret word
        letter_positions = [j for j, x in enumerate(sec_word1) if x == letter]
        
        for x in letter_positions:
            dummy_word[x] = letter
        
        if dummy_word == sec_word1:
            print('\nOUTPUT Congratulations! You guessed the secret word!')
            break
        else:
            print('\nOUTPUT Success! You guessed a Character in the word!')
    else:
        print('\nOUTPUT Boo! You guessed incorrectly!')
            
    print(i,' guesses remaining')
    print('Character''s Guessed: ', *guessed_letters, sep =' ')
    print('\nOUTPUT ',*dummy_word, sep =' ')

print('\nOUTPUT You''re out of guesses! Better luck next time!\n')

