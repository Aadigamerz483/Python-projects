import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

def show_question():
    question=quiz_data[current_question]
    qs_label.config(text=question["question"])
    choices=question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")
    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question=quiz_data[current_question]
    selected_choice=choice_btns[choice].cget("text")  

    if selected_choice==question["answer"]:
        global score
        score+=1
        score_label.config(text="Score: {}/{}".format(score,len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question+=1
    
    if current_question<len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed","Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        window.destroy()

quiz_data=[
    {
        "question" : "Q1. What is the sum of 130+125+191?",
        "choices" : ["A. 335","B. 456","C. 446","D. 426"],
        "answer" : "C. 446"
    },
    {
        "question" : "Q2. If we minus 712 from 1500, how much do we get?",
        "choices" : ["A. 788","B. 778","C. 768","D. 758"],
        "answer" : "A. 788"
    },
    {
        "question" : "Q3. 50 time of 8 is equal to:",
        "choices" : ["A. 80","B. 400","C. 800","D. 4000"],
        "answer" : "B. 400"
    },
    {
        "question" : "Q4. 110 divided by 10 is:",
        "choices" : ["A. 11","B. 10","C. 5","D. None of These"],
        "answer" : "A. 11"
    },
    {
        "question" : "Q5. 20+(90/2) is equal to:",
        "choices" : ["A. 50","B. 55","C. 65","D. 60"],
        "answer" : "C. 65"
    }
]

window=tk.Tk()
window.title("Quiz App")
window.geometry("600x500")
window.configure(bg="black")
style=Style(theme="flatly")

style.configure("TLabel", font=('consolas', 20))
style.configure("TButton", font=('consolas', 16))

qs_label=ttk.Label(window, anchor="center", wraplength=500, padding=10)
qs_label.pack(pady=10)

choice_btns=[]
for i in range(4):
    button=ttk.Button(window, command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label=ttk.Label(window, anchor="center", padding=10)
feedback_label.pack(pady=10)

score=0
score_label=ttk.Label(window, text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10)
score_label.pack(pady=10)

next_btn=ttk.Button(window, text="Next", command=next_question, state="disable")
next_btn.pack(pady=10)

current_question=0

show_question()

window.mainloop()
