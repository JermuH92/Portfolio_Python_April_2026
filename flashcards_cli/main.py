import json

################# FLASH CARDS - CLI GAME #################

# Simple attempt of making a flash card game. Contains two classes, one for deck and another for the card itself, with methods used in main game loop.
# Contains two game loops, one for flawless victory and another repeating until all of the answers are correct. (Can be refactored to use a single loop)
# Goal in mind with this mini-project was to practice combining I/O operations with OOP and functional programming principles.

################# CLASSES #################

class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.mastered = False

    def is_correct(self, user_answer):
        check_input = user_answer.strip().lower()
        actual_answer = self.answer.strip().lower()

        return check_input == actual_answer

class Deck:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_unmastered_cards(self):
        return list(filter(lambda card: not card.mastered, self.cards))



def main():

    with open("flashcards.json", "r") as f:
        retrieve_cards = json.load(f)

    my_deck = Deck()

    for card_data in retrieve_cards:
        card_question = card_data["question"]
        card_answer = card_data["answer"]

        new_card = Card(card_question, card_answer)

        my_deck.add_card(new_card)

    correct_answers = 0
    wrong_answers = 0

    for card in my_deck.cards:       
        print(f"\nQuestion: {card.question}")
        input_prompt = input("Your answer: ")

        if card.is_correct(input_prompt):
            card.mastered = True
            correct_answers += 1
            print("Correct")
        else:
            wrong_answers += 1    
            print("Incorrect")
    
    if correct_answers == len(my_deck.cards):
        print(f"\n*** Game finished FLAWLESSLY with all of the answers CORRECT ***")
    
    else:
        print(f"You had {correct_answers} correct answer(s) and {wrong_answers} wrong answer(s). TRY AGAIN")
        total_wrong_answers = wrong_answers
        round_number = 2

        unmastered_cards = my_deck.get_unmastered_cards()

        while len(unmastered_cards) > 0: # REFACTOR TO CONTAIN ALL CARD GAME OPERATIONS IN THE SAME WHILE LOOP, not really too "DRY" at the moment
            print(f"\n----- ROUND {round_number} -----")

            for card in unmastered_cards:
                print(f"\nQuestion: {card.question}")
                input_prompt = input("Your answer: ")

                if card.is_correct(input_prompt):
                    card.mastered = True
                    print("Correct")
                else:
                    total_wrong_answers += 1
                    print("Incorrect")
            
            unmastered_cards = my_deck.get_unmastered_cards()
            round_number += 1
    
        print(f"\n*** Congratulations... You learned all of the {len(my_deck.cards)} cards. ***")
        print(f"You answered a total of {total_wrong_answers} questions wrong.")


if __name__ == "__main__":
    main()