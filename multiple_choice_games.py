from question import Question

question_prompts = [
    "What is the highest mountain in the world?\n(a) Mount Everest\n(b) Mount Elburus\n(c) Mount Blanc\n\n",
    "Which of these 3 capitals are not situated in Asia?\n(a) Seoul\n(b) Tokyo\n(c) London\n\n",
    "Which of these animal names are the name of a coding language?\n(a) Anaconda\n(b) Python\n(c) Cobras\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")


]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
