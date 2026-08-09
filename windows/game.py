import customtkinter as customtk
import main

def upload_game(gm_wd):
    text_ex = customtk.CTkLabel(gm_wd, text='', font=("Arial", 144))
    text_ex.grid(row=0, column=1, padx=0, pady=0)
    ans = customtk.CTkEntry(gm_wd,
                                placeholder_text='enter', font=("Arial", 22),
                                width=200, height=40)
    ans.grid(row=2, column=1, padx=0, pady=0)
    return text_ex, ans

def st_gm(gm_wd, amou_ex, oper, minnum, maxnum, rnd, crt, wrg, results_func):
    text_ex, ans = upload_game(gm_wd)
    gm_wd.grid(row=0, column=0, sticky='nsew')
    gm_wd.grid_columnconfigure(1, weight=1)
    for i in range(3):
        gm_wd.grid_rowconfigure(i, weight=1)
    
    #GENERATE_EXAMPLE------------------------------------------------
    a, b, corr_val = main.gen_ex(minnum, maxnum, oper)

    #TEXT_EXAMPLE----------------------------------------------------
    text_ex.configure(text=f'{a} {oper} {b} = ?')

    #TEXTBOX--------------------------------------------------------
    ans.unbind('<Return>')
    ans.bind('<Return>', lambda event: check_ans(gm_wd, ans, amou_ex, corr_val, oper, minnum, maxnum, rnd, crt, wrg, results_func))
    ans.focus()

def check_ans(gm_wd, entry_answer: customtk.CTkEntry, amou_ex, corr_val: int, oper, minnum, maxnum, rnd, crt, wrg, results_func):
    user_ans = int(entry_answer.get())
    crt, wrg, amou_ex = main.answer(user_ans, corr_val, crt, wrg, amou_ex)
    entry_answer.delete(0, 'end')
    if amou_ex >= 1:
        st_gm(gm_wd, amou_ex, oper, minnum, maxnum, rnd, crt, wrg, results_func)
    else:
        results_func(oper, crt, wrg)