# Instruction Notes

I moved the comments from guessing_game.py over here and

1. Display an intro/welcome message to the player.
    - ask the player for their name
        - use the `input()` function
    - store their name in a variable
    - pass the variable to the method, `send_welcome_message`
2. Store a random number as the answer/solution.
    - import the `random` module
    - get a random, positive, whole number
    - number between `1` and `25`
    - store that number in a variable
    - pass the variable to a method?
    - who needs access to know about this number?
3. Continuously prompt the player for a guess.
    - Use a `while` loop!
    - similar to #1

    - an `if/else` block

      a. If the **guess** greater than the **solution**, 
        display to the player "It's lower".
      b. If the **guess** is less than the **solution**, 
        display to the player "It's higher".

4. Once the guess is correct, 
    - stop looping, 
    - inform the user they "Got it"
    - and show how many attempts it took them to get the correct number.

5. Let the player know the game is ending, 
   or something that indicates the game is over.