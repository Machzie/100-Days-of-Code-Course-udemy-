import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TEXT_COLOR = "white"
QUESTION_FONT = ('Arial', 18, 'italic')

# Create scale for number of questions
# Create listbox, or individual buttons, for topics


class SetupInterface:

    def __init__(self):

        self.num_qs = 0
        self.cat = None

        self.setupwindow = tkinter.Tk()
        self.setupwindow.title("Quizzlet Setup")
        self.setupwindow.geometry("250x300")
        self.setupwindow.config(bg=THEME_COLOR)

        self.welcome_label = tkinter.Label(text="Quizzlet", font=("Arial", 18, "bold"), bg=THEME_COLOR, fg=TEXT_COLOR)
        self.welcome_label.grid(row=0, column=0, columnspan=2, sticky="EW")

        self.num_q_label = tkinter.Label(text="No. of questions: ", pady=10, bg=THEME_COLOR, fg=TEXT_COLOR)
        self.num_q_label.grid(row=1, column=0, sticky="EW")
        self.num_q_spinbox = tkinter.Spinbox(from_=1, to=50, width=10)
        self.num_q_spinbox.grid(row=1, column=1, sticky="EW")

        self.category_label = tkinter.Label(text="Select category: ", bg=THEME_COLOR, fg=TEXT_COLOR)
        self.category_label.grid(row=2, column=0, sticky="EW")
        self.category_listbox = tkinter.Listbox()
        example_list = ["General Knowledge", "Geography", "History", "Science"]
        for item in example_list:
            self.category_listbox.insert(example_list.index(item), item)
        self.category_listbox.grid(row=2, column=1, sticky="EW")

        self.ok_button = tkinter.Button(text="Begin Quiz!", command=self.return_choices)
        self.ok_button.grid(row=3, column=1, sticky="EW", pady=20)

        self.setupwindow.mainloop()

    def return_choices(self):
        self.num_qs = self.num_q_spinbox.get()
        self.cat = self.category_listbox.get('active')
        self.setupwindow.destroy()


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.quizwindow = tkinter.Tk()
        self.quizwindow.title("Quizzlet App")
        self.quizwindow.geometry("300x400")
        self.quizwindow.config(bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.question_canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125,
                                                              text="Example text",
                                                              width=280,
                                                              fill=THEME_COLOR,
                                                              font=QUESTION_FONT)
        self.question_canvas.grid(row=1, column=0, columnspan=2)

        self.true_image = tkinter.PhotoImage(file="./images/true.png")
        self.false_image = tkinter.PhotoImage(file="./images/false.png")
        self.true_button = tkinter.Button(image=self.true_image, bg=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = tkinter.Button(image=self.false_image, bg=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.quizwindow.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.question_canvas.itemconfig(self.question_text,
                                            text=f"You've reached the end of the questions!",
                                            fill=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.question_canvas.itemconfig(self.question_text, fill="green")
        else:
            self.question_canvas.itemconfig(self.question_text, fill="red")
        self.quizwindow.after(1000, self.get_next_question)
