import customtkinter as customtk

def load_main(main_wd, prepare_game, stats_wd, quit_btn):
        #TITLE---------------------------------------------------------
    gmtitle = customtk.CTkLabel(main_wd,
                                    text='',
                                    font=("Arial", 72))
    gmtitle.grid(row=0, column=1, padx=0, pady=0)

    #BUTTONS--------------------------------------------------------
    btn_gm = customtk.CTkButton(main_wd, 
                                    text='', font=("Arial", 22),
                                    width=200, height=40,
                                    command=prepare_game)
    btn_gm.grid(row=1, column=1, padx=0, pady=(0, 100))
    #lambda: main_window.start_game(main_wd, app)

    btn_comm = customtk.CTkButton(main_wd, 
                                    text='', font=("Arial", 22),
                                    width=200, height=40,
                                    command=stats_wd)
    btn_comm.grid(row=1, column=1, padx=0, pady=(0,0))

    btn_quit = customtk.CTkButton(main_wd,
                                    text='', font=("Arial", 22),
                                    width=200, height=40,
                                    command=quit_btn)
    btn_quit.grid(row=1, column=1, padx=0, pady=(100,0))

    return gmtitle, btn_gm, btn_comm, btn_quit

def show_main(main_wd, prepare_game, stats_wd, quit_btn, gmtitle, btn_gm, btn_comm, btn_quit):
    main_wd.grid(row=0, column=0, sticky='nsew')
    main_wd.grid_columnconfigure(1, weight=1)
    for i in range(2):
        main_wd.grid_rowconfigure(i, weight=1)
    gmtitle.configure(text='BrainCounter')
    btn_gm.configure(text='start a game', command=prepare_game)
    btn_comm.configure(text='look in "statictics"', command=stats_wd)
    btn_quit.configure(text='exit', command=quit_btn)
    
#it's main_window