mcq_file = open("mcq.txt","r")

total_score = 0

correct_answer = ['b','c','b','c','b','c','c','b','c','b']
user_answer = []

def score():
    global total_score
    if len(user_answer) != 0:
        for i in range(len(correct_answer)):
            if user_answer[i] == correct_answer[i]:
                total_score += 1
    print("You got "+str(total_score)+" correct "+" out of "+str(len(correct_answer)))


for i in mcq_file:
    if "Answer" in i:
        while True:
            ans = input("Enter your answer: ").lower()
            if ans in ('a','b','c','d'):
                user_answer.append(ans)
                break
            else:
                print("Enter again")
    else:
        print(i,end=" ")
        

mcq_file.close()

score()


