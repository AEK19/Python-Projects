# Multiple Choice Quiz
# one of the errors I had before changing it was that you need to name the file EXACTLY how it is so the import works
# for example you may get the message ModuleNotFoundError: No module named 'question' so i switched the file name to
# ... 'Question'
# I spent about 15 mins trying to figure out why my rule wasn't working, but all i had to do was spell __init__ correct

from Question import Question

questions_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Tangerines?\n(a) Teal\n(b) Purple\n(c) Orange\n\n",
    "What color are strawberries?\n(a) Red\n(b) Black\n(c) Blue\n\n"
]

 questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "a"),
 ]

 def run_test(questions):
     score = 0
     for question in questions:
         answer = input(question.prompt)
         if answer == question.answer:
             score += 1
       print("You got " + str(score) + "/" + str(len(questions)) + "correct")
run_test(questions)
