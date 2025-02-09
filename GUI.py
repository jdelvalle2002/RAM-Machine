import tkinter
import tkinter.ttk as ttk

from ram import run_program, input_to_program


class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tkinter.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

    def get_input(self):
        input = self.txt.get('1.0', 'end')
        return input


def my_click():
    input = combo.get_input()
    mem = memoria.get()
    program = input_to_program(input, mem)
    output = run_program(program)

    my_label.configure(text='OUTPUT: ' + str(output))


main_window = tkinter.Tk()


combo = TextScrollCombo(main_window)
combo.pack(fill="both", expand=True)
combo.config(width=600, height=600)

combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
combo.txt.config(borderwidth=3, relief="sunken")

style = ttk.Style()
style.theme_use('clam')

memoria = tkinter.StringVar()
nameEntered = tkinter.Entry(main_window, width=15, textvariable=memoria)
nameEntered.pack()

button = tkinter.Button(main_window, text='START', command=my_click)
button.pack()

my_label = tkinter.Label(main_window, text='Aqui estara tu output')
my_label.pack()


main_window.mainloop()
