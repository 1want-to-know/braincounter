import customtkinter as customtk


def show_results(gm_results, oper, crt, wrg, launch):
    gm_results.grid(row=0, column=0, sticky='nsew')
    gm_results.grid_columnconfigure(1, weight=1)
    for i in range(8):
        gm_results.grid_rowconfigure(i, weight=1)
    
    #RESULTS---------------------------------------------------------
    res_oper = customtk.CTkLabel(gm_results, text=f'operator: {oper}', font=("Arial", 36))
    res_oper.grid(row=2, column=1, padx=0, pady=0)

    res_crt = customtk.CTkLabel(gm_results, text=f'correct: {crt}', font=("Arial", 36))
    res_crt.grid(row=3, column=1, padx=0, pady=0)

    res_wrg = customtk.CTkLabel(gm_results, text=f'wrong: {wrg}', font=("Arial", 36))
    res_wrg.grid(row=4, column=1, padx=0, pady=0)


    gm_exit = customtk.CTkButton(gm_results, 
                                    text='main menu', font=("Arial", 22),
                                    width=200, height=40,
                                    command=launch)
    gm_exit.grid(row=7, column=1, padx=0, pady=0)