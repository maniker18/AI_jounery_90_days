from que import question

question_prompt=["what is color of sky?\n(a)blue\n(b)red\n(c)green\n(d)yellow\n",
                 "what is color of grass?\n(a)blue\n(b)red\n(c)green\n(d)yellow\n",
                 "what is color of blood?\n(a)blue\n(b)red\n(c) green\n(d)yellow\n"]

questions=[question(question_prompt[0],"a"),
           question(question_prompt[1],"c"),
           question(question_prompt[2],"b"),]

def mul_choice(que):
    score = 0
    for question in questions:
        answer=input(question.question)
        if answer == question.answer:
            score +=1
        
    print("your score is : "+str(score) + "/"+str(len(questions)))
    
mul_choice(questions)