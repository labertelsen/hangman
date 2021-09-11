#to do: format input, test for bad input, print hangman, test for repeat guesses

print("Welcome to Hangman")
#get word to be guessed
word = input("Enter one word to be guessed: ")
#turn word into array
full_array = list(word)
#create empty array
word_length = len(word)
empty_array = ["_"] * word_length
#initialize score variables
chars_left = word_length
bad_guesses = 0
bad_char = 0
#set location in empty array to 0
location = 0

#start game loop
while chars_left > 0 and bad_guesses < 6:
#variables that need to be reset each guess
    location = 0
    bad_char = 0
#start a guess
    print("Enter a one-letter guess.")
    print(" ".join(empty_array))
    guess = input()

    while location <= word_length - 1:
#if guess matches location in word, fill in the empty array. else move on to next location
        if guess == full_array[location]:
            empty_array[location] = guess
            chars_left -= 1
        else:
            bad_char += 1
        location +=1
#if guess never showed up, report a bad guess
    if bad_char >= word_length:
        bad_guesses += 1
        print("Bad guess!")
        print("Lives left:", 6 - bad_guesses)
#if guess showed up, report a good guess
    else:
        print("Good guess!")
        print("Lives left:", 6 - bad_guesses)
        
#end of game prints
print("Game Over")
if chars_left <= 0:
    print("You won!")
    print("The word was:", word)
elif bad_guesses >= 6:
    print("You lost!")
    print("The word was:", word)
else:
    print("uh oh... something went wrong :(")