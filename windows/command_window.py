import customtkinter as customtk

def load_comm(comm_wd, launch):
    btn_gm = customtk.CTkButton(comm_wd, 
                                    text='', font=("Arial", 22),
                                    width=200, height=40,
                                    command=launch)
    btn_gm.grid(row=1, column=1, padx=0, pady=0)
    return btn_gm


def comm(comm_wd, launch, btn_gm):
    comm_wd.grid(row=0, column=0, sticky='nsew')
    comm_wd.grid_columnconfigure(1, weight=1)
    for i in range(2):
        comm_wd.grid_rowconfigure(i, weight=1)
    btn_gm.configure(text='main menu', command=launch)
