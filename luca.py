import tkinter as tk

def say_hello():
    label.config(text=" feliz dias dos pais !")

root = tk.Tk()
root.title("Hello, World!")

label = tk.Label(root, text="Clique no botão para ver a mensagem.")
label.pack(padx=40, pady=40)

button = tk.Button(root, text="Clique aqui", command=say_hello)
button.pack(padx=40, pady=20)

root.mainloop()