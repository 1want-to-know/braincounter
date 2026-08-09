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

def launch():
    hide_all_frames()
    main_window.show_main(main_wd, 
                            prepare_game=st_gm_settings, 
                            stats_wd=comm, 
                            quit_btn=quit_btn)


def st_gm_settings():
    hide_all_frames()
    prepare_game.st_gm_settings(gm_wd_sett,
                                st_gm=st_gm)


def st_gm(amou_ex, oper, minnum, maxnum, rnd, crt, wrg):
    hide_all_frames()
    game.st_gm(gm_wd, amou_ex, oper, minnum, maxnum, rnd, crt, wrg,
                results_func=results_func)


def results_func(oper, crt, wrg):
    hide_all_frames()
    results.show_results(gm_results, oper, crt, wrg,
                            launch=launch)


def comm():
    command_window.comm(stats_wd,
                        launch=launch)


def quit_btn():
    app.destroy()


if __name__ == '__main__':
    launch()
    app.mainloop()