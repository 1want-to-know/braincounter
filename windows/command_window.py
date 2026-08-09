import customtkinter as customtk

def comm(comm_wd, launch):
    comm_wd.grid(row=0, column=0, sticky='nsew')
    comm_wd.grid_columnconfigure(1, weight=1)
    for i in range(2):
        comm_wd.grid_rowconfigure(i, weight=1)

    #BUTTONS--------------------------------------------------------
    btn_gm = customtk.CTkButton(comm_wd, 
                                    text='main menu', font=("Arial", 22),
                                    width=200, height=40,
                                    command=launch)
    btn_gm.grid(row=1, column=1, padx=0, pady=0)

