import customtkinter

#start -> st
#button -> btn


def st_game():
    pass


def comm():
    pass


def quit_btn():
    pass


app = customtkinter.CTk()
app.title('Test')
app.geometry("1200x600")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)


gametitle = customtkinter.CTkLabel(app,
                                    text='BrainCounter',
                                    font=("Arial", 72))
gametitle.grid(row=0, column=1, padx=0, pady=0)


#BUTTONS--------------------------------------------------------
btn_game = customtkinter.CTkButton(app, 
                                    text='start a game',
                                    font=("Arial", 22),
                                    width=200,
                                    height=40,
                                    command=st_game)
btn_game.grid(row=1, column=1, padx=0, pady=(0, 100))

btn_comm = customtkinter.CTkButton(app, 
                                    text='look in "results"',
                                    font=("Arial", 22),
                                    width=200,
                                    height=40,
                                    command=comm)
btn_comm.grid(row=1, column=1, padx=0, pady=(0,0))

btn_quit = customtkinter.CTkButton(app,
                                    text='exit',
                                    font=("Arial", 22),
                                    width=200,
                                    height=40,
                                    command=quit_btn)
btn_quit.grid(row=1, column=1, padx=0, pady=(100,0))


app.mainloop()