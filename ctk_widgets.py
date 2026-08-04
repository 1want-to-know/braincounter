import customtkinter
from typing import Union, Callable

class IntSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int] = 1,
                 huge_step_size: Union[int] = 10,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.huge_step_size = huge_step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 4), weight=0)  # buttons don't expand
        self.grid_columnconfigure(2, weight=1)  # entry expands

        self.huge_subtract_button = customtkinter.CTkButton(self, text="--", width=height-6, height=height-6,
                                                       command=self.huge_subtract_button_callback)
        self.huge_subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=1, padx=(3, 0), pady=3)


        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=2, columnspan=1, padx=3, pady=3, sticky="ew")


        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=3, padx=(0, 3), pady=3)

        self.huge_add_button = customtkinter.CTkButton(self, text="++", width=height-6, height=height-6,
                                                          command=self.huge_add_button_callback)
        self.huge_add_button.grid(row=0, column=4, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0")

    #ADDBUTTONS---------------------------------------------------
    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def huge_add_button_callback(self):
            if self.command is not None:
                self.command()
            try:
                value = int(self.entry.get()) + self.huge_step_size
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
            except ValueError:
                return


    #SUBSTRACTBUTTONS---------------------------------------------------
    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return
    
    def huge_subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.huge_step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))



#ANOTHERCLASS------------------------------------------------------------------------------------
all_operatores = ['+', '-', '*', '/']
class OperatorSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,
                 place_oper: int = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command
        self.place_oper = place_oper

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 4), weight=0)  # buttons don't expand
        self.grid_columnconfigure(2, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="<", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=1, padx=(3, 0), pady=3)


        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=2, columnspan=1, padx=3, pady=3, sticky="ew")


        self.add_button = customtkinter.CTkButton(self, text=">", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=3, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(place_oper, all_operatores[self.place_oper])

    #ADDBUTTONS---------------------------------------------------
    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            if self.place_oper <= 2: #there's 2 cuz if there's 3, we add him and we have 4 so it's bigger than all_operatores
                self.place_oper += self.step_size
            else:
                self.place_oper = 0 #turns from / to +
            oper = all_operatores[self.place_oper]
            self.entry.delete(0, "end")
            self.entry.insert(0, oper)
        except ValueError:
            return

    #SUBSTRACTBUTTONS---------------------------------------------------
    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            if self.place_oper >= 1: #there's 1 cuz if there's 0, we add him and we have -1 so it's smaller than all_operatores
                self.place_oper -= self.step_size
            else:
                self.place_oper = 3 #turns from + to /
            oper = all_operatores[self.place_oper]
            self.entry.delete(0, "end")
            self.entry.insert(0, oper)
        except ValueError:
            return
        

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))