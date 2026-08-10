import customtkinter as customtk

def upload_results(gm_results, launch):
    #RESULTS---------------------------------------------------------
    res_oper = customtk.CTkLabel(gm_results, text=f'', font=("Arial", 36))
    res_oper.grid(row=2, column=1, padx=0, pady=0)

    res_crt = customtk.CTkLabel(gm_results, text=f'', font=("Arial", 36))
    res_crt.grid(row=3, column=1, padx=0, pady=0)

    res_wrg = customtk.CTkLabel(gm_results, text=f'', font=("Arial", 36))
    res_wrg.grid(row=4, column=1, padx=0, pady=0)

    gm_exit = customtk.CTkButton(gm_results, text='', font=("Arial", 22),
                                    width=200, height=40,
                                    command=launch)
    gm_exit.grid(row=7, column=1, padx=0, pady=0)

    return res_oper, res_crt, res_wrg, gm_exit


def show_results(gm_results, oper, crt, wrg, launch, res_oper, res_crt, res_wrg, gm_exit):
    gm_results.grid(row=0, column=0, sticky='nsew')
    gm_results.grid_columnconfigure(1, weight=1)
    for i in range(8):
        gm_results.grid_rowconfigure(i, weight=1)
    res_oper.configure(text=f'operator: {oper}')
    res_crt.configure(text=f'correct: {crt}')
    res_wrg.configure(text=f'wrong: {wrg}')
    gm_exit.configure(text='main menu', command=launch)