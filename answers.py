answers = {
    "How are you?" : "Fine!",
    "Where are you from?" : "I'm from Moscow",
    "What do you do for a living?" : "I'm a programmer",
    "How old are you?" : "I'm 30",
    "Do you like chocolate?": "I love it!"

}
def get_answer(question, answers):
    return answers.get(question)

def user_question(answers): 
    while True:
        new_question = input("Ask me something ")
        answer = get_answer(new_question, answers)
        print(answer)

        if new_question == "Bye":
            break

if __name__ == "__main__":
    get_answer