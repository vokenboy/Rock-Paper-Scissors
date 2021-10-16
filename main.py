import random



while True:
    random_choise = ['r', 'p', 's']
    computer_guess = (random.choice(random_choise))

    usser_input = input("Write 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

    if usser_input == 's' and computer_guess == 'p':
        print(f"User won! {usser_input} wins vs {computer_guess}")
    elif usser_input == 'r' and computer_guess == 's':
        print(f"User won! {usser_input} wins vs {computer_guess}")
    elif usser_input == 'p' and computer_guess == 'r':
        print(f"User won! {usser_input} wins vs {computer_guess}")
    elif computer_guess == 's' and usser_input == 'p':
        print(f"Computer won! {computer_guess} wins vs {usser_input}")
    elif computer_guess == 'r' and usser_input == 's':
        print(f"Computer won! {computer_guess} wins vs {usser_input}")
    elif computer_guess == 'p' and usser_input == 'r':
        print(f"Computer won! {computer_guess} wins vs {usser_input}")
    elif usser_input == computer_guess:
        print("Draw!")

    continue_in = input("To continue press 'c' if you wish to quit press 'q' ")
    if continue_in == 'c':
        pass
    elif continue_in == 'q':
        break
        
