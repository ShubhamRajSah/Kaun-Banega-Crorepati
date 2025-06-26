if __name__=="__main__":
    questions=[
        {
            "question":"which number is even ?",
            "options":['1','2','3','9'],
            "answer":"b"
        },
        {
            "question":"which number is odd ?",
            "options":['10','20','13','90'],
            "answer":"c"
        },
        {
            "question":"which number is prime ?",
            "options":['19','4','25','99'],
            "answer":"a"
        },
        {
            "question":"which number is composite ?",
            "options":['19','43','29','9'],
            "answer":"d"
        },
        {
            "question":"which country has the different flag as compared to other countries ?",
            "options":["NEPAL","EGYPT","BHUTAN","SWEDEN"],
            "answer":"a"
        },
        {
            "question":"what is the currency of Maldives ?",
            "options":["rupees","yen","rufiyaa","dollar"],
            "answer":"c"
        },
        {
            "question":"which is the GOAT cricketer ?",
            "options":["Virat Kohli","Rohit Sharma","Ms Dhoni","Jasprit Bumrah"],
            "answer":"c"
        }
    ]

    def ask_question(q_data, prize):
        print(f"\n{q_data['question']}")
        print(f"a. {q_data['options'][0]}    b. {q_data['options'][1]}")
        print(f"c. {q_data['options'][2]}    d. {q_data['options'][3]}")
        call = input("Your call (a/b/c/d): ").lower()

        if call == q_data['answer']:
            print(f"Correct answer! You won Nrs.{prize} crore")
            return True
        else:
            print(f"Wrong answer! The correct option was '{q_data['answer']}'.")
            return False
    def play_game():
        # Print the game title/introduction
        print("🎙 PRESENTING: KAUN BANEGA CROREPATI")
        
        # List of prize amounts for each question
        prizes = [1, 2, 3, 4, 5, 6, 7]
        
        # Loop through each question and its corresponding prize
        for i, q in enumerate(questions):
            # Ask the current question; if the answer is wrong, exit the loop (end the game)
            if not ask_question(q, prizes[i]):
                break
            # Ask the player if they want to continue to the next question
            play = input("Do you want to continue to the next question? (y/n): ").lower()
            # If the player chooses not to continue, thank them and exit the loop
            if play != "y":
                print("You've chosen to walk away. Winnings will be transferred. Thank you for playing!")
                break

