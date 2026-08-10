import customtkinter as customtk
import windows.ctk_widgets as ctk_widgets
import main

def load_st_gm_settings(gm_wd_sett, st_gm):
    gm_wd_sett.grid(row=0, column=0, sticky='nsew')
    for i in range(5):
        gm_wd_sett.grid_columnconfigure(i, weight=1)
    for i in range(16):
        gm_wd_sett.grid_rowconfigure(i, weight=1)

    #SETTINGS--------------------------------------------------------
    text_amou_ex = customtk.CTkLabel(gm_wd_sett,
                                        text='How many examples?',
                                        font=("Arial", 22)) #FOR EXAMPLES
    text_amou_ex.grid(row=0, column=0, padx=0, pady=0)
    ex_spinb = ctk_widgets.IntSpinbox(gm_wd_sett, width=150, min_size=True, step_size=1, huge_step_size=10)
    ex_spinb.set(1)
    ex_spinb.grid(row=1, column=0)

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
    rnd = main.open_last_round()
    crt = 0 #correct answers
    wrg = 0 #wrong answers
    btn_gm = customtk.CTkButton(gm_wd_sett, 
                                    text='play', font=("Arial", 22),
                                    width=200, height=40,
                                    command=lambda: st_gm(ex_spinb.get(), oper_spinb.get(), min_spinb.get(), max_spinb.get(), rnd, crt, wrg))
    btn_gm.grid(row=14, column=2, padx=0, pady=0)

    return text_amou_ex, ex_spinb, text_oper, oper_spinb, text_min_num, min_spinb, text_max_num, max_spinb, btn_gm

#TODO: WTF IS THIS??? HOW SO MANY DATA?? I HAVE TO FIX THAT!
def st_gm_settings(gm_wd_sett, text_amou_ex, ex_spinb, text_oper, oper_spinb, text_min_num, min_spinb, text_max_num, max_spinb, btn_gm, st_gm):
    gm_wd_sett.grid(row=0, column=0, sticky='nsew')
    for i in range(5):
        gm_wd_sett.grid_columnconfigure(i, weight=1)
    for i in range(16):
        gm_wd_sett.grid_rowconfigure(i, weight=1)
    text_amou_ex.configure(text='How many examples?')
    text_oper.configure(text='An operator: + - * /')
    text_min_num.configure(text='Enter minimum num')
    text_max_num.configure(text='Enter maximum num')
    btn_gm.configure(text='play')
