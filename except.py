questions_dict = {
    "How are you?" : "Fine!",
    "Where are you from?" : "I'm from Moscow",
    "What do you do for a living?" : "I'm a programmer",
    "How old are you?" : "I'm 30",
    "Do you like chocolate?": "I love it!"
        }
while True:
    try: 
        question = input("Ask me something \n")
        question in questions_dict.keys()
        print(questions_dict[question])

    except KeyboardInterrupt:
        print("Bye!")
        break
        
