import random
num=random.randint(1,10)
nums=[1,2,3,4,5,6,7,8,9,10]
wronguesses=0



while True:
    guess=int(input(f"Guess a number from 1 to 10. You have " +str(3-wronguesses)+ " guesses."))

    if guess in nums:
        if wronguesses<2:    
            if guess==num:
                print("Correct.")
                break
            else:
                print("Incorrect, try again.")
                wronguesses+=1
                continue
        else:
            print("You lost. The answer was " +str(num)+ ".")
            break
    else:
        print("Invalid input. Try again.")
    
        
