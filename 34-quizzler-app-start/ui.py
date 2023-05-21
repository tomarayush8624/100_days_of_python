from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.is_right = None

        self.window = Tk()
        self.window.title("Quizzer")
        # self.create_interface()
        self.window.config(bg=THEME_COLOR)
        self.score_label = Label(text=f"score: {self.quiz.score}", bg=THEME_COLOR, fg="#fff")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125, width=270, text=f"question", font=("Aerial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        # buttons

        right_tick = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=right_tick, highlightthickness=0, command=self.check_ans_true)
        self.true_btn.grid(row=2, column=0,pady=20)
        wrong_tick = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_tick, highlightthickness=0, command=self.check_ans_false)
        self.wrong_btn.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question, text="Quiz is over")
            self.true_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def check_ans_true(self):
        # self.is_right =
        self.feedback(self.quiz.check_answer("true"))

    def check_ans_false(self):
        # self.is_right =
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, ans):
        if ans:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)


