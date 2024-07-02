import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego")
        
        # Ventana de inicio
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack()
        
        self.start_button = tk.Button(self.start_frame, text="Jugar", command=self.ask_name)
        self.start_button.pack()

        # Inicialización del puntaje
        self.score = 0

    def ask_name(self):
        self.start_frame.pack_forget()
        
        self.name_frame = tk.Frame(self.root)
        self.name_frame.pack()
        
        self.name_label = tk.Label(self.name_frame, text="Ingrese su nombre:")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self.name_frame)
        self.name_entry.pack()
        
        self.name_button = tk.Button(self.name_frame, text="OK", command=self.show_instructions)
        self.name_button.pack()

    def show_instructions(self):
        self.user_name = self.name_entry.get()
        self.name_frame.pack_forget()
        
        self.instructions_frame = tk.Frame(self.root)
        self.instructions_frame.pack()
        
        self.instructions_label = tk.Label(self.instructions_frame, text="Hola")
        self.instructions_label.pack()
        
        self.instructions_button = tk.Button(self.instructions_frame, text="OK", command=self.start_game)
        self.instructions_button.pack()

    def start_game(self):
        self.instructions_frame.pack_forget()
        self.current_question = 0
        self.questions = [
            {"image": "caballo.jpg", "options": ["Perro", "Caballo", "Cebra", "Elefante"], "answer": "Caballo"},
            {"image": "carro.jpg", "options": ["Carro", "Avión", "Moto", "Barco"], "answer": "Carro"}
        ]
        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        
        self.question_frame = tk.Frame(self.root)
        self.question_frame.pack()
        
        self.image = Image.open(question["image"])
        self.image = ImageOps.expand(self.image.resize((200, 200), Image.LANCZOS), border=2, fill='black')
        self.photo = ImageTk.PhotoImage(self.image)
        
        self.image_label = tk.Label(self.question_frame, image=self.photo)
        self.image_label.pack(side="left", padx=10, pady=10)
        
        self.options_frame = tk.Frame(self.question_frame)
        self.options_frame.pack(side="right", padx=10, pady=10)
        
        for option in question["options"]:
            btn = tk.Button(self.options_frame, text=option, command=lambda opt=option: self.check_answer(opt))
            btn.pack(anchor="center", pady=5)
        
        self.next_button = tk.Button(self.root, text="Siguiente", command=self.next_question)
        self.next_button.pack(pady=20)

    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question]["answer"]
        if answer == correct_answer:
            messagebox.showinfo("Resultado", "CORRECTO")
            self.score += 1
        else:
            messagebox.showinfo("Resultado", f"INCORRECTO\nLa respuesta correcta es: {correct_answer}")
            self.score -= 1

    def next_question(self):
        self.question_frame.pack_forget()
        self.next_button.pack_forget()
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.end_game()

    def end_game(self):
        self.end_frame = tk.Frame(self.root)
        self.end_frame.pack()
        
        self.end_label = tk.Label(self.end_frame, text=f"Gracias por jugar, {self.user_name}.\nTu puntaje final es: {self.score}")
        self.end_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()