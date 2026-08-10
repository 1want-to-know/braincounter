import customtkinter as customtk

import windows.main_window as main_window
import windows.command_window as command_window
import windows.prepare_game as prepare_game
import windows.game as game
import windows.results as results

#start -> st
#button -> btn
#commands -> comm
#window -> wd
#game -> gm
#spinbox -> spinb
#example(math) -> ex
#amount of examples -> amou_ex

#supreme_wd
app = customtk.CTk()
app.title('BrainCounter')
app.geometry("1000x500")
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
#supreme_wd

#other_wd
main_wd = customtk.CTkFrame(app)
gm_wd = customtk.CTkFrame(app)
gm_wd_sett = customtk.CTkFrame(app)
gm_results = customtk.CTkFrame(app)
stats_wd = customtk.CTkFrame(app)
#other_wd

hide_frames = [main_wd, gm_wd, gm_wd_sett, gm_results, stats_wd]

#hiding all frames
def hide_all_frames():
    for frame in hide_frames:
        frame.grid_remove()
#hiding all frames


def launch():
    hide_all_frames()
    gmtitle, btn_gm, btn_comm, btn_quit = main_window.load_main(main_wd, prepare_game=st_gm_settings, 
                                                        stats_wd=comm, quit_btn=quit_btn)
    main_window.show_main(main_wd, prepare_game=st_gm_settings, stats_wd=comm, 
                            quit_btn=quit_btn, gmtitle=gmtitle, btn_gm=btn_gm, btn_comm=btn_comm, btn_quit=btn_quit)


def st_gm_settings():
    hide_all_frames()
    text_amou_ex, ex_spinb, text_oper, oper_spinb, text_min_num, min_spinb, text_max_num, max_spinb, btn_gm = prepare_game.load_st_gm_settings(gm_wd_sett, st_gm=st_gm)
    prepare_game.st_gm_settings(gm_wd_sett, text_amou_ex=text_amou_ex, ex_spinb=ex_spinb, text_oper=text_oper, oper_spinb=oper_spinb, 
                                text_min_num=text_min_num, min_spinb=min_spinb, text_max_num=text_max_num, 
                                max_spinb=max_spinb, btn_gm=btn_gm, st_gm=st_gm)


def st_gm(amou_ex, oper, minnum, maxnum, rnd, crt, wrg):
    hide_all_frames()
    text_ex, ans = game.upload_game(gm_wd)
    game.st_gm(gm_wd, amou_ex, oper, minnum, maxnum, rnd, crt, wrg, text_ex=text_ex, ans=ans, results_func=results_func)


def results_func(oper, crt, wrg):
    hide_all_frames()
    res_oper, res_crt, res_wrg, gm_exit = results.upload_results(gm_results, launch=launch)
    results.show_results(gm_results, oper, crt, wrg,
                            launch=launch, res_oper=res_oper, res_crt=res_crt, 
                            res_wrg=res_wrg, gm_exit=gm_exit)


def comm():
    hide_all_frames()
    btn_gm = command_window.load_comm(stats_wd, launch=launch)
    command_window.comm(stats_wd, launch=launch, btn_gm=btn_gm)


def quit_btn():
    app.destroy()


if __name__ == '__main__':
    launch()
    app.mainloop()