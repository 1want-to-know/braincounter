import customtkinter as customtk
import ctk_widgets
import main
import correct_ans
import file_work #am I need it?

#start -> st
#button -> btn
#commands -> comm
#window -> wd
#game -> gm
#spinbox -> spinb
#problem(math) -> prob

#supreme_wd
app = customtk.CTk()
app.title('BrainCounter')
app.geometry("1200x600")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
#supreme_wd
#other_wd
main_wd = customtk.CTkFrame(app)
gm_wd = customtk.CTkFrame(app)
gm_wd_sett = customtk.CTkFrame(app)
comm_wd = customtk.CTkFrame(app)
#other_wd


def show_main():
    #deleting other wd
    gm_wd.grid_remove()
    gm_wd_sett.grid_remove()
    comm_wd.grid_remove()

    main_wd.grid(row=0, column=0, sticky='nsew')
    main_wd.grid_columnconfigure(1, weight=1)
    for i in range(2):
        main_wd.grid_rowconfigure(i, weight=1)
    #TITLE---------------------------------------------------------
    gmtitle = customtk.CTkLabel(main_wd,
                                    text='BrainCounter',
                                    font=("Arial", 72))
    gmtitle.grid(row=0, column=1, padx=0, pady=0)

    #BUTTONS--------------------------------------------------------
    btn_gm = customtk.CTkButton(main_wd, 
                                    text='start a game', font=("Arial", 22),
                                    width=200, height=40,
                                    command=st_gm_settings)
    btn_gm.grid(row=1, column=1, padx=0, pady=(0, 100))

    btn_comm = customtk.CTkButton(main_wd, 
                                    text='look in "results"', font=("Arial", 22),
                                    width=200, height=40,
                                    command=comm)
    btn_comm.grid(row=1, column=1, padx=0, pady=(0,0))

    btn_quit = customtk.CTkButton(main_wd,
                                    text='exit', font=("Arial", 22),
                                    width=200, height=40,
                                    command=quit_btn)
    btn_quit.grid(row=1, column=1, padx=0, pady=(100,0))


def st_gm_settings():
    main_wd.grid_remove()
    gm_wd_sett.grid(row=0, column=0, sticky='nsew')
    for i in range(5):
        gm_wd_sett.grid_columnconfigure(i, weight=1)
    for i in range(16):
        gm_wd_sett.grid_rowconfigure(i, weight=1)

    #SETTINGS--------------------------------------------------------
    text_prob = customtk.CTkLabel(gm_wd_sett,
                                        text='How many problems?',
                                        font=("Arial", 22)) # FOR PROBLEMS
    text_prob.grid(row=0, column=0, padx=0, pady=0)
    prob_spinb = ctk_widgets.IntSpinbox(gm_wd_sett, width=150, step_size=1, huge_step_size=10)
    prob_spinb.grid(row=1, column=0)


    text_oper = customtk.CTkLabel(gm_wd_sett,
                                        text='An operator: + - * /',
                                        font=("Arial", 22)) #FOR OPERATOR
    text_oper.grid(row=0, column=1, padx=0, pady=0)
    oper_spinb = ctk_widgets.OperatorSpinbox(gm_wd_sett, width=150, step_size=1, place_oper=0)
    oper_spinb.grid(row=1, column=1)


    text_min_num = customtk.CTkLabel(gm_wd_sett,
                                        text='Enter minimum num',
                                        font=("Arial", 22))  #FOR MINNUM
    text_min_num.grid(row=0, column=3, padx=0, pady=0)
    min_spinb = ctk_widgets.IntSpinbox(gm_wd_sett, width=150, step_size=1, huge_step_size=10)
    min_spinb.grid(row=1, column=3)

    text_max_num = customtk.CTkLabel(gm_wd_sett,
                                            text='Enter maximum num',
                                            font=("Arial", 22))  #FOR MAXNUM
    text_max_num.grid(row=0, column=4, padx=0, pady=0)
    max_spinb = ctk_widgets.IntSpinbox(gm_wd_sett, width=150, step_size=1, huge_step_size=10)
    max_spinb.grid(row=1, column=4)

    #START_BUTTON--------------------------------------------------------
    btn_gm = customtk.CTkButton(gm_wd_sett, 
                                    text='play', font=("Arial", 22),
                                    width=200, height=40,
                                    command=lambda: st_gm(prob_spinb.get(), oper_spinb.get(), min_spinb.get(), max_spinb.get()))
    btn_gm.grid(row=14, column=2, padx=0, pady=0)


def st_gm(prob, oper, minnum, maxnum):
    gm_wd_sett.grid_remove()
    gm_wd.grid(row=0, column=0, sticky='nsew')
    gm_wd.grid_columnconfigure(1, weight=1)
    for i in range(3):
        gm_wd.grid_rowconfigure(i, weight=1)

    #BUTTONS--------------------------------------------------------
    btn_gm = customtk.CTkButton(gm_wd, 
                                    text='main menu', font=("Arial", 22),
                                    width=200, height=40,
                                    command=show_main)
    btn_gm.grid(row=1, column=1, padx=0, pady=0)

    #TEXTBOX--------------------------------------------------------
    ans = customtk.CTkEntry(gm_wd,
                                placeholder_text='enter', font=("Arial", 22),
                                width=200, height=40)
    ans.grid(row=2, column=1, padx=0, pady=0)
    ans.bind('<Return>', lambda event: check_ans(ans))
    ans.focus()


def comm():
    main_wd.grid_remove()
    comm_wd.grid(row=0, column=0, sticky='nsew')
    comm_wd.grid_columnconfigure(1, weight=1)
    for i in range(2):
        comm_wd.grid_rowconfigure(i, weight=1)

    #BUTTONS--------------------------------------------------------
    btn_gm = customtk.CTkButton(comm_wd, 
                                    text='main menu', font=("Arial", 22),
                                    width=200, height=40,
                                    command=show_main)
    btn_gm.grid(row=1, column=1, padx=0, pady=0)


def quit_btn():
    app.destroy()


#some functions for keeping it work
def check_ans(entry_answer: customtk.CTkEntry):
    user_ans = entry_answer.get()
    print(user_ans)
    entry_answer.delete(0, 'end')
    entry_answer.focus()




show_main()

app.mainloop()