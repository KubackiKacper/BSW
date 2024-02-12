import customtkinter as ctk
import tkinter as tk
import numpy as np
import ipaddress
import netmiko
import os
import re

from tkinter import *
from tkinter import filedialog
from stringsPL import *
from stringsENG import *
from scipy import constants
from PIL import Image
from netmiko import ConnectHandler

#?______________________________________________________________________________________________________________________

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()

app.title("Menadżer skryptów dla mostów bezprzewodowych - Bridge Script Wizard")
app.geometry("800x500+580+300")
app.resizable(False,False)
app.iconbitmap("wifi-16.ico")

app_frame=ctk.CTkFrame(master=app, width=800, height=500,fg_color="transparent",corner_radius=0)
app_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

main_frame=ctk.CTkFrame(master=app_frame,width=650,height=499,fg_color="transparent",corner_radius=0)

options_frame=ctk.CTkFrame(master=app_frame,width=150,height=499,border_width=1,border_color="#006633",corner_radius=0)

#?__________________________________________________________________________________________________________________________________

pl=PhotoImage(file="Flag_of_Poland.png")
eng=PhotoImage(file="Flag-United-Kingdom.png")

#?__________________________________________________________________________________________________________________________________  

def delete_app_frame():
    for frame in app_frame.winfo_children():
        frame.destroy()
        
#?__________________________________________________________________________________________________________________________________

def delete_main_frame():
    for frame1 in main_frame.winfo_children():
        frame1.destroy()
        
#?__________________________________________________________________________________________________________________________________    
   
def set_text(language):
    global language_value
    language_value=language
    return language_value

#?__________________________________________________________________________________________________________________________________ 

def hide_indicate():
    start_btn.configure(border_width=0)
    link_budget_calculator_btn.configure(border_width=0)
    page1_btn.configure(border_width=0)
    page3_btn.configure(border_width=0)
    page4_btn.configure(border_width=0)
    page2_btn.configure(border_width=0)
    page5_btn.configure(border_width=0)
    page6_btn.configure(border_width=0)
    page7_btn.configure(border_width=0)
    
#?__________________________________________________________________________________________________________________________________

def indicate(button):
    hide_indicate()
    button.configure(border_width=1,border_color="green")

#?__________________________________________________________________________________________________________________________________

def switch_event():
    if(switch_var.get() == "on"):
        if(language_value=='polish'):
            switch.configure(text=polish_strings['dark_mode'], text_color="white")
            start_btn.configure(text_color="white")
            link_budget_calculator_btn.configure(text_color="white")
            page1_btn.configure(text_color="white")
            page3_btn.configure(text_color="white")
            page4_btn.configure(text_color="white")
            page2_btn.configure(text_color="white")
            page5_btn.configure(text_color="white")
            page6_btn.configure(text_color="white")
            page7_btn.configure(text_color="white")
            ctk.set_appearance_mode("dark")
            
        else:
            switch.configure(text=english_strings['dark_mode'], text_color="white")
            start_btn.configure(text_color="white")
            link_budget_calculator_btn.configure(text_color="white")
            page1_btn.configure(text_color="white")
            page3_btn.configure(text_color="white")
            page4_btn.configure(text_color="white")
            page2_btn.configure(text_color="white")
            page5_btn.configure(text_color="white")
            page6_btn.configure(text_color="white")
            page7_btn.configure(text_color="white")
            ctk.set_appearance_mode("dark")
            
    elif(switch_var.get() == "off"):
        if(language_value=='polish'):
            switch.configure(text=polish_strings['light_mode'], text_color="black")
            start_btn.configure(text_color="black")
            link_budget_calculator_btn.configure(text_color="black")
            page1_btn.configure(text_color="black")
            page3_btn.configure(text_color="black")
            page4_btn.configure(text_color="black")
            page2_btn.configure(text_color="black")
            page5_btn.configure(text_color="black")
            page6_btn.configure(text_color="black")
            page7_btn.configure(text_color="black")
            ctk.set_appearance_mode("light")
        else:
            switch.configure(text=english_strings['light_mode'], text_color="black")
            start_btn.configure(text_color="black")
            link_budget_calculator_btn.configure(text_color="black")
            page1_btn.configure(text_color="black")
            page3_btn.configure(text_color="black")
            page4_btn.configure(text_color="black")
            page2_btn.configure(text_color="black")
            page5_btn.configure(text_color="black")
            page6_btn.configure(text_color="black")
            page7_btn.configure(text_color="black")
            ctk.set_appearance_mode("light")
            
switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(master=options_frame,command=switch_event,variable=switch_var, 
                               onvalue="on", offvalue="off")

#?__________________________________________________________________________________________________________________________________

def select_language():
    delete_main_frame()
    main_frame.configure(border_width=0)

    select_language_lbl = ctk.CTkLabel(master=main_frame, fg_color="transparent", font=("", 30), text=select_language_string)
    buttonPL = ctk.CTkButton(master=main_frame, 
                             command=lambda:[set_text('polish'),switch.configure(text=polish_strings['dark_mode']),welcome_page()], 
                             text="", image=pl, fg_color="transparent", hover=DISABLED,)
    buttonENG = ctk.CTkButton(master=main_frame, 
                              command=lambda:[set_text('english'),switch.configure(text=english_strings['dark_mode']),welcome_page()],
                              text="", image=eng, fg_color="transparent", hover=DISABLED)

    
    main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    select_language_lbl.place(relx=0.49, rely=0.3, anchor=tk.CENTER)
    buttonPL.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
    buttonENG.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
   
#?__________________________________________________________________________________________________________________________________ 

def welcome_page():
    delete_main_frame()
    
    main_frame.configure(border_width=1,border_color="#006633")
    main_frame.place(relx=0.594,rely=0.5,anchor=tk.CENTER)
    options_frame.place(relx=0.095,rely=0.5,anchor=tk.CENTER)
    global start_btn
    global link_budget_calculator_btn
    global page1_btn
    global page2_btn
    global page3_btn 
    global page4_btn 
    global page5_btn
    global page6_btn
    global page7_btn

    start_btn=None
    link_budget_calculator_btn=None
    page1_btn=None
    page2_btn=None
    page3_btn =None
    page4_btn =None
    page5_btn=None
    page6_btn=None
    page7_btn=None
    
    if (language_value=='polish' and switch_var.get() == "on"):
        
        start_btn=ctk.CTkButton(master=options_frame,text=polish_strings['start_str'],fg_color="transparent",
                                 border_width=1,hover="disabled",
                                border_color="green", text_color="white")
        
        
        link_budget_calculator_btn=ctk.CTkButton(master=options_frame,text=polish_strings['lbc_str'],fg_color="transparent",
                                 text_color="white", hover="disabled")
        
        page1_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page1_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page3_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page3_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page4_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page4_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page2_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page2_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page5_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page5_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page6_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page6_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page7_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page7_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        
        label_1=ctk.CTkLabel(master=main_frame,text=polish_strings['welcome_string'],justify="center",wraplength=600, font=("",24))
        label_2=ctk.CTkLabel(master=main_frame,text=polish_strings[ 'welcome_desc'],justify="left",wraplength=650, font=("",22))
        

        next_pageBTN=ctk.CTkButton(master=main_frame,command=lambda:[link_budget_calculator(),indicate(link_budget_calculator_btn)],
                                   text=polish_strings['next_button'],width=80,fg_color="#006633")
        back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[options_frame.place_forget(),select_language(),],fg_color="grey",
                               text=polish_strings['back_button'],width=80)
    elif (language_value=='polish' and switch_var.get() == "off"):
        

        start_btn=ctk.CTkButton(master=options_frame,text=polish_strings['start_str'],fg_color="transparent"
                                ,hover="disabled", border_width=1,
                                border_color="green", text_color="black")
        link_budget_calculator_btn=ctk.CTkButton(master=options_frame,text=polish_strings['lbc_str'],fg_color="transparent",
                                hover="disabled", text_color="black")
        page1_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page1_str'],fg_color="transparent"
                                ,hover="disabled",text_color="black")
        page3_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page3_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        page4_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page4_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        page2_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page2_str'],fg_color="transparent",
                                hover="disabled",text_color="black")
        page5_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page5_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        page6_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page6_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        page7_btn=ctk.CTkButton(master=options_frame,text=polish_strings['page7_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        label_1=ctk.CTkLabel(master=main_frame,text=polish_strings['welcome_string'],justify="center", wraplength=600, font=("",24))
        label_2=ctk.CTkLabel(master=main_frame,text=polish_strings[ 'welcome_desc'],justify="left",wraplength=650, font=("",22))
        

        next_pageBTN=ctk.CTkButton(master=main_frame,command=lambda:[link_budget_calculator(),indicate(link_budget_calculator_btn)],
                                   text=polish_strings['next_button'],width=80,fg_color="#006633")
        back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[options_frame.place_forget(),select_language(),],fg_color="grey",
                               text=polish_strings['back_button'],width=80)
        
    elif (language_value=='english' and switch_var.get() == "on"):
        start_btn=ctk.CTkButton(master=options_frame,text=english_strings['start_str'],fg_color="transparent"
                                ,hover="disabled", border_width=1,
                                border_color="green", text_color="white")
        link_budget_calculator_btn=ctk.CTkButton(master=options_frame,text=english_strings['lbc_str'],fg_color="transparent"
                                ,hover="disabled", text_color="white")
        page1_btn=ctk.CTkButton(master=options_frame,text=english_strings['page1_str'],fg_color="transparent"
                                ,hover="disabled",text_color="white")
        page3_btn=ctk.CTkButton(master=options_frame,text=english_strings['page3_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page4_btn=ctk.CTkButton(master=options_frame,text=english_strings['page4_str'],fg_color="transparent",
                                text_color="white",hover="disabled")
        page2_btn=ctk.CTkButton(master=options_frame,text=english_strings['page2_str'],fg_color="transparent"
                                ,hover="disabled",text_color="white")
        page5_btn=ctk.CTkButton(master=options_frame,text=english_strings['page5_str'],fg_color="transparent"
                                ,hover="disabled",text_color="white")
        page6_btn=ctk.CTkButton(master=options_frame,text=english_strings['page6_str'],fg_color="transparent"
                                ,hover="disabled",text_color="white")
        page7_btn=ctk.CTkButton(master=options_frame,text=english_strings['page7_str'],fg_color="transparent"
                                ,hover="disabled",text_color="white")
        
        label_1=ctk.CTkLabel(master=main_frame,text=english_strings['welcome_string'],justify="center", wraplength=600, font=("",24))
        label_2=ctk.CTkLabel(master=main_frame,text=english_strings[ 'welcome_desc'],justify="left", wraplength=650,font=("",22))
        

        next_pageBTN=ctk.CTkButton(master=main_frame,command=lambda:[link_budget_calculator(),indicate(link_budget_calculator_btn)],
                                   text=english_strings['next_button'],width=80,fg_color="#006633")
        back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[options_frame.place_forget(),select_language(),],fg_color="grey",
                               text=english_strings['back_button'],width=80)
                               
    elif (language_value=='english' and switch_var.get() == "off"):
        start_btn=ctk.CTkButton(master=options_frame,text=english_strings['start_str'],fg_color="transparent"
                                ,hover="disabled", border_width=1,
                                border_color="green", text_color="black")
        link_budget_calculator_btn=ctk.CTkButton(master=options_frame,text=english_strings['lbc_str'],fg_color="transparent"
                                ,hover="disabled", text_color="black")
        page1_btn=ctk.CTkButton(master=options_frame,text=english_strings['page1_str'],fg_color="transparent"
                                ,hover="disabled",text_color="black")
        page3_btn=ctk.CTkButton(master=options_frame,text=english_strings['page3_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        page4_btn=ctk.CTkButton(master=options_frame,text=english_strings['page4_str'],fg_color="transparent",
                                text_color="black",hover="disabled")
        page2_btn=ctk.CTkButton(master=options_frame,text=english_strings['page2_str'],fg_color="transparent"
                                ,hover="disabled",text_color="black")
        page5_btn=ctk.CTkButton(master=options_frame,text=english_strings['page5_str'],fg_color="transparent"
                                ,hover="disabled",text_color="black")
        page6_btn=ctk.CTkButton(master=options_frame,text=english_strings['page6_str'],fg_color="transparent"
                                ,hover="disabled",text_color="black")
        page7_btn=ctk.CTkButton(master=options_frame,text=english_strings['page7_str'],fg_color="transparent"
                                ,hover="disabled",text_color="black")
        
        label_1=ctk.CTkLabel(master=main_frame,text=english_strings['welcome_string'],justify="center", wraplength=600, font=("",24))
        label_2=ctk.CTkLabel(master=main_frame,text=english_strings[ 'welcome_desc'],justify="left", wraplength=650, font=("",22))
        

        next_pageBTN=ctk.CTkButton(master=main_frame,command=lambda:[link_budget_calculator(),indicate(link_budget_calculator_btn)],
                                   text=english_strings['next_button'],width=80,fg_color="#006633")
        back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[options_frame.place_forget(),select_language(),],fg_color="grey",
                               text=english_strings['back_button'],width=80)

    
    switch.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    start_btn.place(relx=0.5,rely=0.05,anchor=tk.CENTER)
    link_budget_calculator_btn.place(relx=0.5,rely=0.11,anchor=tk.CENTER)
    page1_btn.place(relx=0.5,rely=0.18,anchor=tk.CENTER)
    page3_btn.place(relx=0.5,rely=0.26,anchor=tk.CENTER)
    page4_btn.place(relx=0.5,rely=0.35,anchor=tk.CENTER)
    page2_btn.place(relx=0.5,rely=0.44,anchor=tk.CENTER)
    page5_btn.place(relx=0.5,rely=0.54,anchor=tk.CENTER)
    page6_btn.place(relx=0.5,rely=0.64,anchor=tk.CENTER)
    page7_btn.place(relx=0.5,rely=0.72,anchor=tk.CENTER)
    label_1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
    label_2.place(relx=0.5,rely=0.45,anchor=tk.CENTER)
    next_pageBTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
    
#?__________________________________________________________________________________________________________________________________

global float_value
def wrong_value_entered():
    help_window = ctk.CTkToplevel(master=main_frame)
    help_window.title("")
    help_window.geometry("350x75+780+500")
    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    help_window.resizable(False, False)
    if language_value=="polish":
        help_lbl=ctk.CTkLabel(master=help_window, text=polish_strings['wrong_value_entered_str'],justify="center", wraplength=450)
    else:
        help_lbl=ctk.CTkLabel(master=help_window, text=english_strings['wrong_value_entered_str'],justify="center", wraplength=450)
    
    close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    help_lbl.pack(anchor="center",padx=5,pady=15)
    close_btn.place(relx=0.5,rely=0.8,anchor=tk.CENTER)

    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def validate_entry_widgets(new_value): 
    global ptx,gtx,ltx,lfs,lm,grx,lrx
    try:
        if not new_value.strip():

            ptx = 0
            gtx = 0
            ltx = 0
            lfs = 0
            lm  = 0
            grx = 0
            lrx = 0

            return True

        float_value = float(new_value)


        if new_value.count('.') > 1:
            raise ValueError

        return True
    except ValueError:

        Result_entry.delete(0, tk.END)  
        wrong_value_entered()
        return False

#?__________________________________________________________________________________________________________________________________

    
def not_all_values_entered():
    help_window = ctk.CTkToplevel(master=main_frame)
    help_window.title("")
    help_window.geometry("350x75+780+500")
    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    help_window.resizable(False, False)

    if language_value=="polish":
        help_lbl=ctk.CTkLabel(master=help_window, text=polish_strings['not_all_values_entered_str'],justify="center", wraplength=450)
    else:
        help_lbl=ctk.CTkLabel(master=help_window, text=english_strings['not_all_values_entered_str'],justify="center", wraplength=450)
    
    close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    help_lbl.pack(anchor="center",padx=5,pady=15)
    close_btn.place(relx=0.5,rely=0.8,anchor=tk.CENTER)

    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def calculate_result():
    global ptx, gtx, ltx, lfs, lm, grx, lrx
    Result_entry.configure(state="normal")
    ptx_str = Ptx_entry.get()
    gtx_str = Gtx_entry.get()
    ltx_str = Ltx_entry.get()
    lfs_str = Lfs_entry.get()
    lm_str = Lm_entry.get()
    grx_str = Grx_entry.get()
    lrx_str = Lrx_entry.get()


    try:
        ptx = float(ptx_str)
        gtx = float(gtx_str)
        ltx = float(ltx_str)
        lfs = float(lfs_str)
        lm =  float(lm_str)
        grx = float(grx_str)
        lrx = float(lrx_str)
    except ValueError:
        Result_entry.delete(0, tk.END)
        not_all_values_entered()
        return

    result = np.round(ptx + gtx - ltx - lfs - lm + grx - lrx,3)
    Result_entry.delete(0, tk.END)
    Result_entry.insert(0, result)
    Result_entry.configure(state="disabled")

#?__________________________________________________________________________________________________________________________________

def reset_values():
    Result_entry.configure(state="normal")
    Ptx_entry.configure(validate="none")
    Gtx_entry.configure(validate="none")
    Ltx_entry.configure(validate="none")
    Lfs_entry.configure(validate="none")
    Lm_entry.configure (validate="none")
    Grx_entry.configure(validate="none")
    Lrx_entry.configure(validate="none")


    Ptx_entry.delete(0, tk.END)
    Gtx_entry.delete(0, tk.END)
    Ltx_entry.delete(0, tk.END)
    Lfs_entry.delete(0, tk.END)
    Lm_entry.delete (0, tk.END)
    Grx_entry.delete(0, tk.END)
    Lrx_entry.delete(0, tk.END)
    Result_entry.delete(0, tk.END)
    Result_entry.configure(state="disabled")


    Ptx_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Gtx_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Ltx_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Lfs_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Lm_entry.configure (validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Grx_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Lrx_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))

#?__________________________________________________________________________________________________________________________________

def calculate_lfs_values():
    global distance, frequency, lfs_tg, lfs_rg
    
    lfs_Result_entry.configure(state="normal")
    distance_str=distance_entry.get()
    frequency_str=frequency_entry.get()
    lfs_th_str=lfs_tg_entry.get()
    lfs_rg_str=lfs_rg_entry.get()
    
    try:
        distance=float(distance_str)
        frequency=float(frequency_str)
        lfs_tg=float(lfs_th_str)
        lfs_rg=float(lfs_rg_str)
    except ValueError:
        Result_entry.delete(0, tk.END)
        not_all_values_entered()
        return
    result = np.round((20 * np.log10(distance)) + (20 * np.log10(frequency * 1e9)) + (20 * np.log10((4*constants.pi)/constants.speed_of_light)) - lfs_tg - lfs_rg,3)
    lfs_Result_entry.delete(0, tk.END)
    Lfs_entry.delete(0, tk.END)
    
    lfs_Result_entry.insert(0, result)
    Lfs_entry.insert(0, result)
    
    lfs_Result_entry.configure(state="disabled")
    
#?__________________________________________________________________________________________________________________________________

def reset_lfs_values():
    lfs_Result_entry.configure(state="normal")
    
    distance_entry.configure(validate="none")
    frequency_entry.configure(validate="none")
    lfs_tg_entry.configure(validate="none")
    lfs_rg_entry.configure(validate="none")
    Lfs_entry.configure(validate="none")


    lfs_Result_entry.delete(0, tk.END)
    Lfs_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)
    frequency_entry.delete(0, tk.END)
    lfs_tg_entry.delete(0, tk.END)
    lfs_rg_entry.delete (0, tk.END)
    
    Result_entry.configure(state="disabled")


    Lfs_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    distance_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    frequency_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    lfs_tg_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    lfs_rg_entry.configure (validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    Lfs_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    
#?__________________________________________________________________________________________________________________________________   

def calculate_lfs_result():
    global distance, frequency, lfs_tg, lfs_rg, distance_entry, frequency_entry,lfs_tg_entry,lfs_rg_entry,lfs_Result_entry
    lfs_calculate_window = ctk.CTkToplevel(master=main_frame)
    lfs_calculate_window.title("")
    lfs_calculate_window.geometry("350x350+780+400")
    lfs_calculate_window.after(300, lambda: lfs_calculate_window.iconbitmap("help.ico"))
    lfs_calculate_window.resizable(False, False)
    
    if language_value=="polish":
        distance_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=polish_strings['distance_str'],justify="left",font=("",18))
        distance_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        frequency_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=polish_strings['frequency_str'],justify="left",font=("",18))
        frequency_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        lfs_tg_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=polish_strings['lfs_tg_str'],justify="left",font=("",18))
        lfs_tg_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        lfs_rg_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=polish_strings['lfs_rg_str'],justify="left",font=("",18))
        lfs_rg_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        Result_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=polish_strings['result_lbl'],justify="left",font=("",18))
        lfs_Result_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        lfs_Result_entry.configure(state="disabled")
        calculate_button=ctk.CTkButton(master=lfs_calculate_window,command=lambda:[calculate_lfs_values()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=polish_strings['calculate_button_str'])
        reset_button=ctk.CTkButton(master=lfs_calculate_window,command=lambda:[reset_lfs_values()],
                                       height=25,width=80,fg_color="grey",corner_radius=0,
                                       text=polish_strings['reset_button_str'])
        close_btn=ctk.CTkButton(master=lfs_calculate_window, command=lambda:[lfs_calculate_window.destroy(),lfs_calculate_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    else:
        distance_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=english_strings['distance_str'],justify="left",font=("",18))
        distance_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        frequency_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=english_strings['frequency_str'],justify="left",font=("",18))
        frequency_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        lfs_tg_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=english_strings['lfs_tg_str'],justify="left",font=("",18))
        lfs_tg_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        lfs_rg_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=english_strings['lfs_rg_str'],justify="left",font=("",18))
        lfs_rg_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        Result_lbl=ctk.CTkLabel(master=lfs_calculate_window, text=english_strings['result_lbl'],justify="left",font=("",18))
        lfs_Result_entry=ctk.CTkEntry(master=lfs_calculate_window,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        lfs_Result_entry.configure(state="disabled")
        calculate_button=ctk.CTkButton(master=lfs_calculate_window,command=lambda:[calculate_lfs_values()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=english_strings['calculate_button_str'])
        reset_button=ctk.CTkButton(master=lfs_calculate_window,command=lambda:[reset_lfs_values()],
                                       height=25,width=80,fg_color="grey",corner_radius=0,
                                       text=english_strings['reset_button_str'])
        close_btn=ctk.CTkButton(master=lfs_calculate_window, command=lambda:[lfs_calculate_window.destroy(),lfs_calculate_window.update()],
                                text='OK', fg_color="#006633",width=40,height=20)
    
    distance_lbl.pack(anchor="center")
    distance_entry.pack(anchor="center",pady=1)
    
    frequency_lbl.pack(anchor="center")
    frequency_entry.pack(anchor="center",pady=1)
    
    lfs_tg_lbl.pack(anchor="center")
    lfs_tg_entry.pack(anchor="center",pady=1)
    
    lfs_rg_lbl.pack(anchor="center")
    lfs_rg_entry.pack(anchor="center",pady=1)
    
    Result_lbl.pack(anchor="center")
    lfs_Result_entry.pack(anchor="center",pady=1)
    
    calculate_button.place(relx=0.385,rely=0.85,anchor=tk.CENTER)
    reset_button.place(relx=0.625,rely=0.85,anchor=tk.CENTER)
    close_btn.place(relx=0.5,rely=0.93,anchor=tk.CENTER)
    lfs_calculate_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def lbc_help_page():
    help_window = ctk.CTkToplevel(master=main_frame)
    scroll_frame=ctk.CTkScrollableFrame(master=help_window,width=600,height=299,fg_color="transparent")
    help_window.title("")
    help_window.geometry("615x300+750+350")
    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    help_window.resizable(False, False)
    
    testowe_zdjecie=ctk.CTkImage(light_image=Image.open("diagram.png"),dark_image=Image.open("diagram.png"),size=(360,137))
    img_lbl=ctk.CTkLabel(master=scroll_frame,image=testowe_zdjecie,text="")
    if language_value=="polish":
        help_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['link_budget_help_str'],justify="left", wraplength=587)
        help_lbl2=ctk.CTkLabel(master=scroll_frame, text=polish_strings['link_budget_help_str2'],justify="left", wraplength=587)
    else:
        help_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['link_budget_help_str'],justify="left", wraplength=587)
        help_lbl2=ctk.CTkLabel(master=scroll_frame, text=english_strings['link_budget_help_str2'],justify="left", wraplength=587)
        
    close_btn=ctk.CTkButton(master=scroll_frame, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    scroll_frame.pack()
    
    help_lbl.pack(anchor="w",padx=5)
    img_lbl.pack()
    help_lbl2.pack(anchor="w",padx=5)
    close_btn.pack()

    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def calculate_eirp_values():
    global power, cable, lencable, gain
    
    eirp_Result_entry.configure(state="normal")
    power_str=eirp_power_entry.get()
    cable_str=eirp_cable_entry.get()
    lencable_str=eirp_lencable_entry.get()
    gain_str=eirp_antenna_entry.get()
    
    try:
        power=float(power_str)
        cable=float(cable_str)
        lencable=float(lencable_str)
        gain=float(gain_str)
    except ValueError:
        Result_entry.delete(0, tk.END)
        not_all_values_entered()
        return
    result = power - (cable * lencable) + gain
    
    eirp_Result_entry.insert(0, result)
    
    
    eirp_Result_entry.configure(state="disabled")
    
#?__________________________________________________________________________________________________________________________________

def reset_eirp_values():
    eirp_Result_entry.configure(state="normal")
    
    eirp_power_entry.configure(validate="none")
    eirp_cable_entry.configure(validate="none")
    eirp_lencable_entry.configure(validate="none")
    eirp_antenna_entry.configure(validate="none")



    eirp_Result_entry.delete(0, tk.END)
    eirp_power_entry.delete(0, tk.END)
    eirp_cable_entry.delete(0, tk.END)
    eirp_lencable_entry.delete(0, tk.END)
    eirp_antenna_entry.delete (0, tk.END)
    
    eirp_Result_entry.configure(state="disabled")


    
    eirp_power_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    eirp_cable_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    eirp_lencable_entry.configure(validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    eirp_antenna_entry.configure (validate="key", validatecommand=(app.register(validate_entry_widgets), '%P'))
    
#?__________________________________________________________________________________________________________________________________

def lbc_devices():
    help_window = ctk.CTkToplevel(master=main_frame)
    scroll_frame=ctk.CTkScrollableFrame(master=help_window,width=650,height=299,fg_color="transparent")
    help_window.title("")
    help_window.geometry("650x300+750+350")
    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    help_window.resizable(False, False)
    
    global eirp_power_entry, eirp_antenna_entry, eirp_cable_entry, eirp_antenna_entry, eirp_Result_entry,eirp_lencable_entry
    if language_value=="polish":
        help_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['devices_str1'],justify="left", wraplength=630)

        eirp_power_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['eirp_power'],justify="left",font=("",18))
        eirp_power_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        eirp_cable_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['eirp_cable'],justify="left",font=("",18))
        eirp_cable_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        eirp_lencable_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['eirp_lencable'],justify="left",font=("",18))
        eirp_lencable_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        eirp_antenna_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['eirp_antenna'],justify="left",font=("",18))
        eirp_antenna_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        Result_lbl=ctk.CTkLabel(master=scroll_frame, text=polish_strings['result_lbl'],justify="left",font=("",18))
        eirp_Result_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'), justify="center")
        eirp_Result_entry.configure(state="disabled")
        calculate_button=ctk.CTkButton(master=scroll_frame,command=lambda:[calculate_eirp_values()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=polish_strings['calculate_button_str'])
        reset_button=ctk.CTkButton(master=scroll_frame,command=lambda:[reset_eirp_values()],
                                       height=25,width=80,fg_color="grey",corner_radius=0,
                                       text=polish_strings['reset_button_str'])
    else:
        help_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['devices_str1'],justify="left", wraplength=630)

        eirp_power_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['eirp_power'],justify="left",font=("",18))
        eirp_power_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        eirp_cable_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['eirp_cable'],justify="left",font=("",18))
        eirp_cable_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        eirp_lencable_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['eirp_lencable'],justify="left",font=("",18))
        eirp_lencable_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        eirp_antenna_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['eirp_antenna'],justify="left",font=("",18))
        eirp_antenna_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        Result_lbl=ctk.CTkLabel(master=scroll_frame, text=english_strings['result_lbl'],justify="left",font=("",18))
        eirp_Result_entry=ctk.CTkEntry(master=scroll_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'), justify="center")
        eirp_Result_entry.configure(state="disabled")
        calculate_button=ctk.CTkButton(master=scroll_frame,command=lambda:[calculate_eirp_values()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=english_strings['calculate_button_str'])
        reset_button=ctk.CTkButton(master=scroll_frame,command=lambda:[reset_eirp_values()],
                                       height=25,width=80,fg_color="grey",corner_radius=0,
                                       text=english_strings['reset_button_str'])
        
    close_btn=ctk.CTkButton(master=scroll_frame, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    scroll_frame.pack()
    
    help_lbl.pack(anchor=tk.W)

    eirp_power_lbl.pack(anchor="center")
    eirp_power_entry.pack(anchor="center",pady=1)
    
    eirp_cable_lbl.pack(anchor="center")
    eirp_cable_entry.pack(anchor="center",pady=1)
    
    eirp_lencable_lbl.pack(anchor="center")
    eirp_lencable_entry.pack(anchor="center",pady=1)
    
    eirp_antenna_lbl.pack(anchor="center")
    eirp_antenna_entry.pack(anchor="center",pady=1)
    
    Result_lbl.pack(anchor="center")
    eirp_Result_entry.pack(anchor="center",pady=1)


    calculate_button.pack(pady=2)
    reset_button.pack(pady=2)
    close_btn.pack(pady=2)

    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def link_budget_calculator():
    delete_main_frame()
    global ptx,gtx,ltx,lfs,lm,grx,lrx,Ptx_entry,Gtx_entry,Ltx_entry,Lfs_entry,Lm_entry,Grx_entry,Lrx_entry,Result_entry
    if language_value=='polish':
        
        lbc_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_1(),indicate(page1_btn)],
                                   text=polish_strings['next_button'],width=80,fg_color="#006633") 
    
        lbc_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[welcome_page()],
                                 fg_color="grey",text=polish_strings['back_button'],width=80)
        lbc_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[lbc_help_page()],
                                 fg_color="#606060",text=polish_strings['help_button'],width=80)
        lbc_devices_BTN=ctk.CTkButton(master=main_frame,command=lambda:[lbc_devices()],
                                 fg_color="#606060",text=polish_strings['devices_btn_str'],width=80)

        link_budget_label=ctk.CTkLabel(master=main_frame,text=polish_strings['link_budget_label_str'],
                                       justify="center",wraplength=650,font=("",24))

        Ptx_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Ptx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Ptx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        
        Gtx_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Gtx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Gtx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P')
                                     )
        
        Ltx_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Ltx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Ltx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P')
                                     )
        
        Lfs_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Lfs_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Lfs_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        
        Lm_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Lm_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Lm_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        
        Grx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        Grx_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Grx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        
        Lrx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P')
                                     )
        
        Lrx_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['Lrx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        
        Result_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     justify="center", state="disabled")
        
        

        lfs_calculate_button=ctk.CTkButton(master=main_frame,command=lambda:[calculate_lfs_result()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=polish_strings['calculate_button_str'])
        
        calculate_button=ctk.CTkButton(master=main_frame,command=lambda:[calculate_result()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=polish_strings['calculate_button_str'])
        reset_button=ctk.CTkButton(master=main_frame,command=lambda:[reset_values()],
                                       height=25,width=80,fg_color="grey",corner_radius=0,
                                       text=polish_strings['reset_button_str'])
        result_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['result_lbl'],
                                       justify="left",wraplength=650,font=("",16))
    elif language_value =='english':
        lbc_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_1(),indicate(page1_btn)],
                                   text=english_strings['next_button'],width=80,fg_color="#006633") 
    
        lbc_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[welcome_page()],
                                 fg_color="grey",text=english_strings['back_button'],width=80)
        lbc_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[lbc_help_page()],
                                 fg_color="#606060",text=english_strings['help_button'],width=80)
        lbc_devices_BTN=ctk.CTkButton(master=main_frame,command=lambda:[lbc_devices()],
                                 fg_color="#606060",text=english_strings['devices_btn_str'],width=80)

        link_budget_label=ctk.CTkLabel(master=main_frame,text=english_strings['link_budget_label_str'],
                                       justify="center",wraplength=650,font=("",24))

        Ptx_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Ptx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Ptx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        
        Gtx_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Gtx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Gtx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P')
                                     )
        
        Ltx_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Ltx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Ltx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P')
                                     )
        
        Lfs_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Lfs_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Lfs_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        
        Lm_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Lm_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        Lm_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        
        Grx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P'))
        Grx_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Grx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        
        Lrx_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     validate="key",validatecommand=(app.register(validate_entry_widgets), '%P')
                                     )
        
        Lrx_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['Lrx_entry_str'],
                                       justify="left",wraplength=650,font=("",16))
        
        Result_entry=ctk.CTkEntry(master=main_frame,width=300,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",16),
                                     justify="center", state="disabled")
        
        

        lfs_calculate_button=ctk.CTkButton(master=main_frame,command=lambda:[calculate_lfs_result()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=english_strings['calculate_button_str'])
        
        calculate_button=ctk.CTkButton(master=main_frame,command=lambda:[calculate_result()],
                                       height=25,width=80,fg_color="#006633",corner_radius=0,
                                       text=english_strings['calculate_button_str'])
        reset_button=ctk.CTkButton(master=main_frame,command=lambda:[reset_values()],
                                       height=25,width=80,fg_color="grey",corner_radius=0,
                                       text=english_strings['reset_button_str'])
        result_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['result_lbl'],
                                       justify="left",wraplength=650,font=("",16))
        
    lbc_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    lbc_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
    lbc_help_BTN.place(relx=0.1,rely=0.95, anchor=tk.CENTER)
    lbc_devices_BTN.place(relx=0.25,rely=0.95,anchor=tk.CENTER)
    link_budget_label.place(relx=0.5,rely=0.05, anchor=tk.CENTER)

    if language_value=="polish":  
        Ptx_lbl.place(relx=0.225,rely=0.14,anchor=tk.CENTER)
        Ltx_lbl.place(relx=0.165,rely=0.29,anchor=tk.CENTER)
        Lfs_lbl.place(relx=0.685,rely=0.29,anchor=tk.CENTER)
        Lm_lbl.place(relx=0.14,rely=0.44,anchor=tk.CENTER)
        Lrx_lbl.place(relx=0.175,rely=0.59,anchor=tk.CENTER)
        Grx_lbl.place(relx=0.67,rely=0.44,anchor=tk.CENTER)
        Gtx_lbl.place(relx=0.66,rely=0.14,anchor=tk.CENTER)
    else:
        Ptx_lbl.place(relx=0.22,rely=0.14,anchor=tk.CENTER)
        Ltx_lbl.place(relx=0.18,rely=0.29,anchor=tk.CENTER)
        Lfs_lbl.place(relx=0.645,rely=0.29,anchor=tk.CENTER)
        Lm_lbl.place(relx=0.19,rely=0.44,anchor=tk.CENTER)
        Lrx_lbl.place(relx=0.165,rely=0.59,anchor=tk.CENTER)
        Grx_lbl.place(relx=0.67,rely=0.44,anchor=tk.CENTER)
        Gtx_lbl.place(relx=0.68,rely=0.14,anchor=tk.CENTER)
        
    Ptx_entry.place(relx=0.25,rely=0.2,anchor=tk.CENTER)
    Ltx_entry.place(relx=0.25,rely=0.35, anchor=tk.CENTER)
    Lfs_entry.place(relx=0.72,rely=0.35, anchor=tk.CENTER)
    Lm_entry.place(relx=0.25,rely=0.5, anchor=tk.CENTER)
    Grx_entry.place(relx=0.72,rely=0.5, anchor=tk.CENTER)
    Lrx_entry.place(relx=0.25,rely=0.65, anchor=tk.CENTER)
    Gtx_entry.place(relx=0.72,rely=0.2, anchor=tk.CENTER)

    Result_entry.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
    result_lbl.place(relx=0.5,rely=0.745,anchor=tk.CENTER)
    calculate_button.place(relx=0.55,rely=0.65,anchor=tk.CENTER)
    lfs_calculate_button.place(relx=0.89,rely=0.35, anchor=tk.CENTER)
    reset_button.place(relx=0.68,rely=0.65,anchor=tk.CENTER)
    
    
#?__________________________________________________________________________________________________________________________________

def page1_show_help():
    help_window = ctk.CTkToplevel(master=main_frame)
    help_window.title("")
    help_window.geometry("455x200+700+450")
    help_window.resizable(False, False)

    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    if language_value=='polish':
        help_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['help_lbl_str'],justify="left", wraplength=450)
        help2_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['help2_lbl_str'],justify="left", wraplength=450)
    elif language_value=='english':
        help_lbl = ctk.CTkLabel(master=help_window, text=english_strings['help_lbl_str'],justify="left",wraplength=450)
        help2_lbl = ctk.CTkLabel(master=help_window, text=english_strings['help2_lbl_str'],justify="left", wraplength=450)
    close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)

    help_lbl.pack(anchor="w",padx=5,pady=10)
    help2_lbl.pack(anchor="w",padx=5,pady=5)
    close_btn.place(relx=0.5,rely=0.85,anchor=tk.CENTER)
    
    help_window.grab_set()
    
#?__________________________________________________________________________________________________________________________________

inputval = None

def validate_file_name(new_value):
    global inputval
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value=="polish":
                file_name_validate_lbl.configure(text=polish_strings['no_null_file_name'], text_color="gray")
            else:
                file_name_validate_lbl.configure(text=english_strings['no_null_file_name'], text_color="gray")
            inputval = None
        else:
            if language_value=="polish":
                file_name_validate_lbl.configure(text=polish_strings['correct_file_name'], text_color="#006633")
            else:
                file_name_validate_lbl.configure(text=english_strings['correct_file_name'], text_color="#006633")
            inputval = new_value
        return True
    else:
        if language_value=="polish":
            file_name_validate_lbl.configure(text=polish_strings['incorrect_file_name'], text_color="red")
        else:
            file_name_validate_lbl.configure(text=english_strings['incorrect_file_name'], text_color="red")
        return False
    
#?__________________________________________________________________________________________________________________________________   
 
selected_path= os.getcwd()

def select_path():
    global selected_path
    file_path_entry.configure(state='normal')
    path = filedialog.askdirectory()
    if path:
        selected_path=path
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, path)
        file_path_entry.configure(state='disabled')
     
#?__________________________________________________________________________________________________________________________________

def page_1():
    delete_main_frame()
    global inputval, selected_path, file_name_entry, file_name_validate_lbl, file_path_entry

    inputval = None
    selected_path= os.getcwd()
    
    if language_value=='polish':
        
        page1_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[link_budget_calculator(),indicate(link_budget_calculator_btn)],
                                 fg_color="grey",text=polish_strings['back_button'],width=80)
        page1_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[check_file_name()],
                                 fg_color="#006633",text=polish_strings['next_button'],width=80)
        
        file_name_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['file_name_lbl_str'],justify="left", font=("",25))
        
        path_entry_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['path_entry_lbl_str'],justify="left", font=("",25))
        
        help_button=ctk.CTkButton(master=main_frame,command=lambda:[page1_show_help()],
                                  text=polish_strings['help_button'], width=80, fg_color="#606060")
        
        file_name_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24), validate="key",
                                        validatecommand=(app.register(validate_file_name), '%P'))
         
        file_name_validate_lbl=ctk.CTkLabel(master=main_frame,text='',fg_color="transparent",font=("",18))
 
        file_path_entry=ctk.CTkEntry(master=main_frame,width=500,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),placeholder_text=selected_path, 
                                     placeholder_text_color="grey")
        file_path_entry.configure(state='disabled')


        select_path_button = ctk.CTkButton(
        master=main_frame,
        command=lambda:[select_path()],
        text=polish_strings['select_path_button'],
        width=80,
        fg_color="#006633"
    )
    else:
        page1_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[link_budget_calculator(),indicate(link_budget_calculator_btn)],
                                 fg_color="grey",text=english_strings['back_button'],width=80)
        
        page1_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[check_file_name()],
                                 fg_color="#006633",text=english_strings['next_button'],width=80)
        
        file_name_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['file_name_lbl_str'],justify="left", font=("",25))
        
        path_entry_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['path_entry_lbl_str'],justify="left", font=("",25))
        
        help_button=ctk.CTkButton(master=main_frame,command=lambda:[page1_show_help(),validate_file_name()],
                                  text=english_strings['help_button'], width=80, fg_color="#606060")
        
        file_name_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24), validate="key",
                                        validatecommand=(app.register(validate_file_name), '%P'))
        
        file_name_validate_lbl=ctk.CTkLabel(master=main_frame,text='',fg_color="transparent",font=("",18))

        file_path_entry=ctk.CTkEntry(master=main_frame,width=500,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),placeholder_text=selected_path, 
                                     placeholder_text_color="grey")
        file_path_entry.configure(state='disabled')



        select_path_button = ctk.CTkButton(
        master=main_frame,
        command=lambda:[select_path()],
        text=english_strings['select_path_button'],
        width=80,
        fg_color="#006633"
    )
    
    page1_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    page1_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
    
    help_button.place(relx=0.1,rely=0.95, anchor=tk.CENTER)
    file_name_lbl.place(relx=0.5,rely=0.1, anchor=tk.CENTER)
    path_entry_lbl.place(relx=0.5,rely=0.35,anchor=tk.CENTER)

    file_name_entry.place(relx=0.5,rely=0.2, anchor=tk.CENTER)
    file_name_validate_lbl.place(relx=0.5,rely=0.26, anchor=tk.CENTER)

    file_path_entry.place(relx=0.425,rely=0.45,anchor=tk.CENTER)
    select_path_button.place(relx=0.9,rely=0.45,anchor=tk.CENTER)
    
#?__________________________________________________________________________________________________________________________________

def check_file_name():
    if inputval is None:
        help_window = ctk.CTkToplevel(master=main_frame)
        help_window.title("")
        help_window.geometry("350x110+780+500")
        help_window.resizable(False, False)

        help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['warning_filename_str'],justify="left", wraplength=350)
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=help_window, text=english_strings['warning_filename_str'],justify="left",wraplength=350)
        close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)

        help_lbl.pack(anchor="w",padx=5,pady=10)
        close_btn.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
    
        help_window.grab_set()
    else:
        page_3()
        toggle_visibility_password_start_root()
        toggle_visibility_password_secret_start_root()
        indicate(page3_btn)

#?__________________________________________________________________________________________________________________________________

def delete_file1():
    if os.path.exists(file_path1):
        os.remove(file_path1)

#?__________________________________________________________________________________________________________________________________        

def delete_file2():
    if os.path.exists(file_path2):
        os.remove(file_path2)

#?__________________________________________________________________________________________________________________________________

def on_wap_click(checkbox1, checkbox2):
    global  wap_checkbox, wifi_checkbox
    if checkbox1.get() == 'on':
        checkbox2.deselect()
        
    if checkbox2.get() == 'on':
        checkbox1.deselect()

#?__________________________________________________________________________________________________________________________________
        
def selected_checkbox_value(checkbox):
    global selected_checkbox
    selected_checkbox = checkbox.cget("text")
    return selected_checkbox

selected_checkbox = None

#?__________________________________________________________________________________________________________________________________

def validate_ip_address_root(ip_str):
    global ipaddr_start_val
    try:
        ipaddress.IPv4Address(ip_str)
        return True
    except ipaddress.AddressValueError:
        return False

#?__________________________________________________________________________________________________________________________________

def validate_ipaddr_start_root(new_value):
    global ipaddr_start_val
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value=="polish":
                ip_device_start_validate_lbl.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ip_device_start_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr_start_val = None
        elif len(new_value)>=15:
            if(language_value=='polish'):
                ip_device_start_validate_lbl.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ip_device_start_validate_lbl.configure(text=english_strings['ip_morethan15'], text_color="gray")
        elif new_value.count('.')>3:
            if(language_value=='polish'):
                ip_device_start_validate_lbl.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ip_device_start_validate_lbl.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ip_device_start_validate_lbl.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ip_device_start_validate_lbl.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr_start_val = new_value
        return True
    else:
        if language_value=="polish":
            ip_device_start_validate_lbl.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ip_device_start_validate_lbl.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def validate_username_start(new_value):
    global username_root_val,username_start_validate_lbl
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value=="polish":
                username_start_validate_lbl.configure(text=polish_strings['username_null'], text_color="gray")
            else:
                username_start_validate_lbl.configure(text=english_strings['username_null'], text_color="gray")
            username_root_val = None 
        else:
            if language_value=="polish":
                username_start_validate_lbl.configure(text=polish_strings['username_ok'], text_color="#006633")
            else:
                username_start_validate_lbl.configure(text=english_strings['username_ok'], text_color="#006633")
            username_root_val = new_value
        return True
    else:
        if language_value=="polish":
            username_start_validate_lbl.configure(text=polish_strings['username_bad'], text_color="red")
        else:
            username_start_validate_lbl.configure(text=english_strings['username_bad'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________
    
def validate_password_start(new_value):
    global password_root_val,password_start_validate_lbl
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value=="polish":
                password_start_validate_lbl.configure(text=polish_strings['password_start_null'], text_color="gray")
            else:
                password_start_validate_lbl.configure(text=english_strings['password_start_null'], text_color="gray")
            password_root_val = None
        else:
            if language_value=="polish":
                password_start_validate_lbl.configure(text=polish_strings['password_start_ok'], text_color="#006633")
            else:
                password_start_validate_lbl.configure(text=english_strings['password_start_ok'], text_color="#006633")
            password_root_val = new_value
        return True
    else:
        if language_value=="polish":
            password_start_validate_lbl.configure(text=polish_strings['password_start_bad'], text_color="red")
        else:
            password_start_validate_lbl.configure(text=english_strings['password_start_bad'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________
    
def validate_password_secret_start(new_value):
    global password_secret_root_val,password_secret_start_validate_lbl
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value=="polish":
                password_secret_start_validate_lbl.configure(text='', text_color="gray")
            else:
                password_secret_start_validate_lbl.configure(text='', text_color="gray")
            password_secret_root_val = ''
        else:
            if language_value=="polish":
                password_secret_start_validate_lbl.configure(text=polish_strings['password_secret_start_ok'], text_color="#006633")
            else:
                password_secret_start_validate_lbl.configure(text=english_strings['password_secret_start_ok'], text_color="#006633")
            password_secret_root_val = new_value
        return True
    else:
        if language_value=="polish":
            password_secret_start_validate_lbl.configure(text=polish_strings['password_secret_start_bad'], text_color="red")
        else:
            password_secret_start_validate_lbl.configure(text=english_strings['password_secret_start_bad'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def toggle_visibility_password_start_root():
    if password_start_entry.cget("show") == "*":
        password_start_entry.configure(show="")
        if language_value=='polish':
            show_hide_button.configure(text=polish_strings['button_root_hide'])
        else:
            show_hide_button.configure(text=english_strings['button_root_hide'])
    else:
        password_start_entry.configure(show="*")
        if language_value=='polish':
            show_hide_button.configure(text=polish_strings['button_root_show'])
        else:
            show_hide_button.configure(text=english_strings['button_root_show'])

#?__________________________________________________________________________________________________________________________________

def toggle_visibility_password_secret_start_root():
    if password_secret_start_entry.cget("show") == "*":
        password_secret_start_entry.configure(show="")
        if language_value=='polish':
            show_hide_secret_button.configure(text=polish_strings['button_root_hide'])
        else:
            show_hide_secret_button.configure(text=english_strings['button_root_hide'])
    else:
        password_secret_start_entry.configure(show="*")
        if language_value=='polish':
            show_hide_secret_button.configure(text=polish_strings['button_root_show'])
        else:
            show_hide_secret_button.configure(text=english_strings['button_root_show'])

#?__________________________________________________________________________________________________________________________________

def page_3():
    delete_main_frame()
    global file_path1, file_path2, wap_checkbox, wifi_checkbox, selected_checkbox,ip_device_start_lbl, ipaddr_start_val
    global ip_device_start_entry, validate_ipaddr_start_root,username_start_validate_lbl,password_start_lbl,password_start_entry
    global ip_device_start_validate_lbl,password_start_validate_lbl,password_secret_start_entry,show_hide_secret_button,root_config_commands
    global username_root_val,password_root_val, show_hide_button,password_secret_root_val,password_secret_start_validate_lbl,testowawartosc
    
    selected_checkbox=None
    ipaddr_start_val=None
    username_root_val=None
    password_root_val=None
    password_secret_root_val=''
    
    root_device_script = inputval + "_AP_root" + ".txt"
    

    file_path1 = os.path.join(selected_path, root_device_script)
    

    if language_value=='polish':
        page3_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_1(),delete_file1(),indicate(page1_btn)],
                                 fg_color="grey",text=polish_strings['back_button'],width=80)
        
        page3_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[check_page3_conditions(),validate_ip_address_root(ipaddr_start_val),
                                                                       ],
                                 fg_color="#006633",text=polish_strings['next_button'],width=80)
        page3_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page3_show_help()],
                                 fg_color="#606060",text=polish_strings['help_button'],width=80)
        bridge_type_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['bridge_type_lbl'],justify="left",font=('',25),wraplength=650)
        wifi_checkbox=ctk.CTkCheckBox(master=main_frame,text=polish_strings['wifi_bridge_str'], onvalue='on', offvalue='off',
                                      fg_color="#006633",font=('',18),command=lambda:[on_wap_click(wifi_checkbox,wap_checkbox),
                                                                                      selected_checkbox_value(wifi_checkbox)])
        
        wap_checkbox=ctk.CTkCheckBox(master=main_frame,text=polish_strings['wap_str'],onvalue='on', offvalue='off',
                                      fg_color="#006633",font=('',18),
                                      command=lambda:[on_wap_click(wap_checkbox,wifi_checkbox),selected_checkbox_value(wap_checkbox)])
        
        ip_device_start_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ip_start'],justify="left", font=("",20),wraplength=600)
        ip_device_start_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24), 
                                     validate="key", validatecommand=(app.register(validate_ipaddr_start_root), '%P'))
        ip_device_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        username_start_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['username_start_str'],justify="left", font=("",20),wraplength=600)
        username_start_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_username_start), '%P'))
        username_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_start_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['password_start_lbl_str'],justify="left", font=("",20),wraplength=600)
        password_start_entry=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_start), '%P'))
        password_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_secret_start_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['password_secret_start_lbl_str'],justify="left", font=("",20),
                                               wraplength=600)
        password_secret_start_entry=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_secret_start), '%P'))
        password_secret_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        


        show_hide_button = ctk.CTkButton(master=main_frame, text=polish_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_start_root()],corner_radius=0)
        show_hide_secret_button = ctk.CTkButton(master=main_frame, text=polish_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_secret_start_root()],corner_radius=0)
    
    else:
        page3_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_1(),delete_file1(),indicate(page1_btn)],
                                 fg_color="grey",text=english_strings['back_button'],width=80)
        
        page3_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[check_page3_conditions(),validate_ip_address_root(ipaddr_start_val),
                                                                       ],
                                 fg_color="#006633",text=english_strings['next_button'],width=80)
        page3_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page3_show_help()],
                                 fg_color="#606060",text=english_strings['help_button'],width=80)
        bridge_type_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['bridge_type_lbl'],justify="left",font=('',25),wraplength=650)
        wifi_checkbox=ctk.CTkCheckBox(master=main_frame,text=english_strings['wifi_bridge_str'], onvalue='on', offvalue='off',
                                      fg_color="#006633",font=('',18),command=lambda:[on_wap_click(wifi_checkbox,wap_checkbox),
                                                                                      selected_checkbox_value(wifi_checkbox)])
        
        wap_checkbox=ctk.CTkCheckBox(master=main_frame,text=english_strings['wap_str'],onvalue='on', offvalue='off',
                                      fg_color="#006633",font=('',18),
                                      command=lambda:[on_wap_click(wap_checkbox,wifi_checkbox),selected_checkbox_value(wap_checkbox)])
        
        ip_device_start_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ip_start'],justify="left", font=("",20),wraplength=600)
        ip_device_start_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24), 
                                     validate="key", validatecommand=(app.register(validate_ipaddr_start_root), '%P'))
        ip_device_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        username_start_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['username_start_str'],justify="left", font=("",20),wraplength=600)
        username_start_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_username_start), '%P'))
        username_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_start_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['password_start_lbl_str'],justify="left", font=("",16),wraplength=600)
        password_start_entry=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_start), '%P'))
        password_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_secret_start_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['password_secret_start_lbl_str'],justify="left", font=("",16),
                                               wraplength=600)
        password_secret_start_entry=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_secret_start), '%P'))
        password_secret_start_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        


        show_hide_button = ctk.CTkButton(master=main_frame, text=english_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_start_root()],corner_radius=0)
        show_hide_secret_button = ctk.CTkButton(master=main_frame, text=english_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_secret_start_root()],corner_radius=0)

    page3_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    page3_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
    page3_help_BTN.place(relx=0.1,rely=0.95, anchor=tk.CENTER)

    bridge_type_lbl.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
    wifi_checkbox.place(relx=0.2,rely=0.2,anchor=tk.CENTER)
    wap_checkbox.place(relx=0.7,rely=0.2,anchor=tk.CENTER)
    
    ip_device_start_lbl.place(relx=0.04,rely=0.3,anchor=tk.W)
    ip_device_start_entry.place(relx=0.5,rely=0.37,anchor=tk.CENTER)
    ip_device_start_validate_lbl.place(relx=0.5,rely=0.44,anchor=tk.CENTER)
    
    username_start_lbl.place(relx=0.04,rely=0.5,anchor=tk.W)
    username_start_entry.place(relx=0.5,rely=0.57,anchor=tk.CENTER)
    username_start_validate_lbl.place(relx=0.5,rely=0.64,anchor=tk.CENTER)
    
    password_start_lbl.place(relx=0.04,rely=0.7,anchor=tk.W)
    password_start_entry.place(relx=0.27,rely=0.77,anchor=tk.CENTER)
    password_start_validate_lbl.place(relx=0.25,rely=0.86,anchor=tk.CENTER)
    show_hide_button.place(relx=0.469,rely=0.77,anchor=tk.CENTER)
    
    password_secret_start_lbl.place(relx=0.96,rely=0.7,anchor=tk.E)
    password_secret_start_entry.place(relx=0.73,rely=0.77,anchor=tk.CENTER)
    password_secret_start_validate_lbl.place(relx=0.75,rely=0.86,anchor=tk.CENTER)
    show_hide_secret_button.place(relx=0.9298,rely=0.77,anchor=tk.CENTER)

#?__________________________________________________________________________________________________________________________________
    
def page3_show_help():

    help_window = ctk.CTkToplevel(master=main_frame)
    scroll_frame=ctk.CTkScrollableFrame(master=help_window,width=549,height=299,fg_color="transparent")
    help_window.title("")
    help_window.geometry("550x300+780+500")
    help_window.resizable(False, False)

    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    testowe_zdjecie=ctk.CTkImage(light_image=Image.open("schemat1.png"),dark_image=Image.open("schemat1.png"),size=(360,137))
    img_lbl=ctk.CTkLabel(master=scroll_frame,image=testowe_zdjecie,text="")
    
    testowe_zdjecie2=ctk.CTkImage(light_image=Image.open("schemat2.png"),dark_image=Image.open("schemat2.png"),size=(360,137))
    img_lbl2=ctk.CTkLabel(master=scroll_frame,image=testowe_zdjecie2,text="")
    
    if language_value=='polish':
        help_lbl = ctk.CTkLabel(master=scroll_frame, text=polish_strings['page3_help_str'],justify="left", wraplength=520)
        help_lbl2 = ctk.CTkLabel(master=scroll_frame, text=polish_strings['page3_help_str1'],justify="left", wraplength=520)
    elif language_value=='english':
        help_lbl = ctk.CTkLabel(master=scroll_frame, text=english_strings['page3_help_str'],justify="left",wraplength=520)
        help_lbl2 = ctk.CTkLabel(master=scroll_frame, text=english_strings['page3_help_str1'],justify="left",wraplength=520)
    close_btn=ctk.CTkButton(master=scroll_frame, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    scroll_frame.pack()
    help_lbl.pack(anchor="w",padx=5)
    img_lbl.pack(padx=5)
    help_lbl2.pack(padx=5)
    img_lbl2.pack(padx=5)
    close_btn.pack()
    
    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def page3_invalid_values():
        help_window = ctk.CTkToplevel(master=main_frame)
        help_window.title("")
        help_window.geometry("360x140+780+500")
        help_window.resizable(False, False)

        help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['page3_invalid_str'],justify="left", wraplength=350)
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=help_window, text=english_strings['page3_invalid_str'],justify="left",wraplength=350)
        close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)

        help_lbl.pack(anchor="w",padx=5,pady=10)
        close_btn.pack()
    
        help_window.grab_set()

#?__________________________________________________________________________________________________________________________________        

def check_page3_conditions():
    global ipaddr_start_val,username_root_val,password_root_val,password_secret_root_val,root_config_commands,selected_checkbox,file1,root_device_info
    if selected_checkbox is None or validate_ip_address_root(ipaddr_start_val) == False or username_root_val is None or password_root_val is None:
        page3_invalid_values()
        return
    else:
        
        indicate(page4_btn)
        ipaddr_start_val=str(ipaddr_start_val)
        username_root_val=str(username_root_val)
        password_root_val=str(password_root_val)
        password_secret_root_val=str(password_secret_root_val)

        root_device_info = {
            'device_type': 'cisco_ios',
            'ip': ipaddr_start_val,
            'username': username_root_val,
            'password': password_root_val,
            'secret': password_secret_root_val,

        }
        
        
        page_4()
        toggle_visibility_password_start_root2() 
        toggle_visibility_password_secret_start_root2()
    
#?__________________________________________________________________________________________________________________________________

def validate_ip_address_root2(ip_str2):
    global ipaddr_start_val2
    try:
        ipaddress.IPv4Address(ip_str2)
        return True
    except ipaddress.AddressValueError:
        return False

#?__________________________________________________________________________________________________________________________________

def validate_ipaddr_start_root2(new_value2):
    global ipaddr_start_val2
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value2):
        if len(new_value2) == 0:
            if language_value=="polish":
                ip_device_start_validate_lbl2.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ip_device_start_validate_lbl2.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr_start_val2 = None
        elif len(new_value2)>=15:
            if(language_value=='polish'):
                ip_device_start_validate_lbl2.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ip_device_start_validate_lbl2.configure(text=english_strings['ip_morethan15'], text_color="gray")
        elif new_value2.count('.')>3:
            if(language_value=='polish'):
                ip_device_start_validate_lbl2.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ip_device_start_validate_lbl2.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ip_device_start_validate_lbl2.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ip_device_start_validate_lbl2.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr_start_val2 = new_value2
        return True
    else:
        if language_value=="polish":
            ip_device_start_validate_lbl2.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ip_device_start_validate_lbl2.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def validate_username_start2(new_value2):
    global username_root_val2,username_start_validate_lbl2
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value2):
        if len(new_value2) == 0:
            if language_value=="polish":
                username_start_validate_lbl2.configure(text=polish_strings['username_null'], text_color="gray")
            else:
                username_start_validate_lbl2.configure(text=english_strings['username_null'], text_color="gray")
            username_root_val2 = None
        else:
            if language_value=="polish":
                username_start_validate_lbl2.configure(text=polish_strings['username_ok'], text_color="#006633")
            else:
                username_start_validate_lbl2.configure(text=english_strings['username_ok'], text_color="#006633")
            username_root_val2 = new_value2
        return True
    else:
        if language_value=="polish":
            username_start_validate_lbl2.configure(text=polish_strings['username_bad'], text_color="red")
        else:
            username_start_validate_lbl2.configure(text=english_strings['username_bad'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________
    
def validate_password_start2(new_value2):
    global password_root_val2,password_start_validate_lbl2
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value2):
        if len(new_value2) == 0:
            if language_value=="polish":
                password_start_validate_lbl2.configure(text=polish_strings['password_start_null'], text_color="gray")
            else:
                password_start_validate_lbl2.configure(text=english_strings['password_start_null'], text_color="gray")
            password_root_val2 = None
        else:
            if language_value=="polish":
                password_start_validate_lbl2.configure(text=polish_strings['password_start_ok'], text_color="#006633")
            else:
                password_start_validate_lbl2.configure(text=english_strings['password_start_ok'], text_color="#006633")
            password_root_val2 = new_value2
        return True
    else:
        if language_value=="polish":
            password_start_validate_lbl2.configure(text=polish_strings['password_start_bad'], text_color="red")
        else:
            password_start_validate_lbl2.configure(text=english_strings['password_start_bad'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________
    
def validate_password_secret_start2(new_value2):
    global password_secret_root_val2,password_secret_start_validate_lbl2
    pattern = re.compile(r'^[a-zA-Z0-9_]*$')
    
    if pattern.match(new_value2):
        if len(new_value2) == 0:
            if language_value=="polish":
                password_secret_start_validate_lbl2.configure(text='', text_color="gray")
            else:
                password_secret_start_validate_lbl2.configure(text='', text_color="gray")
            password_secret_root_val2 = ''
        else:
            if language_value=="polish":
                password_secret_start_validate_lbl2.configure(text=polish_strings['password_secret_start_ok'], text_color="#006633")
            else:
                password_secret_start_validate_lbl2.configure(text=english_strings['password_secret_start_ok'], text_color="#006633")
            password_secret_root_val2 = new_value2
        return True
    else:
        if language_value=="polish":
            password_secret_start_validate_lbl2.configure(text=polish_strings['password_secret_start_bad'], text_color="red")
        else:
            password_secret_start_validate_lbl2.configure(text=english_strings['password_secret_start_bad'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def toggle_visibility_password_start_root2():
    if password_start_entry2.cget("show") == "*":
        password_start_entry2.configure(show="")
        if language_value=='polish':
            show_hide_button2.configure(text=polish_strings['button_root_hide'])
        else:
            show_hide_button2.configure(text=english_strings['button_root_hide'])
    else:
        password_start_entry2.configure(show="*")
        if language_value=='polish':
            show_hide_button2.configure(text=polish_strings['button_root_show'])
        else:
            show_hide_button2.configure(text=english_strings['button_root_show'])

#?__________________________________________________________________________________________________________________________________

def toggle_visibility_password_secret_start_root2():
    if password_secret_start_entry2.cget("show") == "*":
        password_secret_start_entry2.configure(show="")
        if language_value=='polish':
            show_hide_secret_button2.configure(text=polish_strings['button_root_hide'])
        else:
            show_hide_secret_button2.configure(text=english_strings['button_root_hide'])
    else:
        password_secret_start_entry2.configure(show="*")
        if language_value=='polish':
            show_hide_secret_button2.configure(text=polish_strings['button_root_show'])
        else:
            show_hide_secret_button2.configure(text=english_strings['button_root_show'])

#?__________________________________________________________________________________________________________________________________

def page4_show_help():

    help_window = ctk.CTkToplevel(master=main_frame)
    scroll_frame=ctk.CTkScrollableFrame(master=help_window,width=549,height=199,fg_color="transparent")
    help_window.title("")
    help_window.geometry("550x200+780+500")
    help_window.resizable(False, False)

    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    if language_value=='polish':
        help_lbl = ctk.CTkLabel(master=scroll_frame, text=polish_strings['page4_help_str'],justify="left", wraplength=520)
    elif language_value=='english':
        help_lbl = ctk.CTkLabel(master=scroll_frame, text=english_strings['page4_help_str'],justify="left",wraplength=520)
    close_btn=ctk.CTkButton(master=scroll_frame, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    scroll_frame.pack()
    help_lbl.pack(anchor="w",padx=5)
    close_btn.pack()
    
    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def page_4():
    delete_main_frame()
    global file_path1, file_path2, wap_checkbox2, wifi_checkbox2, selected_checkbox,ip_device_start_lbl2, ipaddr_start_val2
    global ip_device_start_entry2, validate_ipaddr_start_root2,username_start_validate_lbl2,password_start_lbl2,password_start_entry2,password_entry
    global ip_device_start_validate_lbl2,password_start_validate_lbl2,password_secret_start_entry2,show_hide_secret_button2
    global username_root_val2,password_root_val2, show_hide_button2,password_secret_root_val2,password_secret_start_validate_lbl2,root_device_info
    
    
    ipaddr_start_val2=None
    username_root_val2=None
    password_root_val2=None
    password_secret_root_val2=''
    
    
    repeater_device_script = inputval + "_AP_non_root" + ".txt"

    
    file_path2 = os.path.join(selected_path, repeater_device_script)

    if language_value=='polish':
        page4_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_3(),delete_file2(),indicate(page3_btn),
                                                    toggle_visibility_password_start_root(),toggle_visibility_password_secret_start_root()],
                                 fg_color="grey",text=polish_strings['back_button'],width=80)
        
        page4_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[check_page4_conditions(),validate_ip_address_root2(ipaddr_start_val2)],
                                 fg_color="#006633",text=polish_strings['next_button'],width=80)
        
        page4_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page4_show_help()],
                                 fg_color="#606060",text=polish_strings['help_button'],width=80)
        
        
        
        ip_device_start_lbl2=ctk.CTkLabel(master=main_frame, text=polish_strings['ip_start'],justify="left", font=("",20),wraplength=600)
        ip_device_start_entry2=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24), 
                                     validate="key", validatecommand=(app.register(validate_ipaddr_start_root2), '%P'))
        ip_device_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        username_start_lbl2=ctk.CTkLabel(master=main_frame, text=polish_strings['username_start_str'],justify="left", font=("",20),wraplength=600)
        username_start_entry2=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_username_start2), '%P'))
        username_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_start_lbl2=ctk.CTkLabel(master=main_frame, text=polish_strings['password_start_lbl_str'],justify="left", font=("",20),wraplength=600)
        password_start_entry2=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_start2), '%P'))
        password_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_secret_start_lbl2=ctk.CTkLabel(master=main_frame, text=polish_strings['password_secret_start_lbl_str'],justify="left", font=("",20),
                                                wraplength=600)
        password_secret_start_entry2=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_secret_start2), '%P'))
        password_secret_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,
                                                         fg_color="transparent")
        

        show_hide_button2 = ctk.CTkButton(master=main_frame, text=polish_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_start_root2()],corner_radius=0)
        show_hide_secret_button2 = ctk.CTkButton(master=main_frame, text=polish_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_secret_start_root2()],corner_radius=0)
    else:
        page4_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_3(),delete_file2(),indicate(page3_btn),
                                                    toggle_visibility_password_start_root(),toggle_visibility_password_secret_start_root()],
                                 fg_color="grey",text=english_strings['back_button'],width=80)
        
        page4_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[check_page4_conditions(),validate_ip_address_root2(ipaddr_start_val2)],
                                 fg_color="#006633",text=english_strings['next_button'],width=80)
        
        page4_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page4_show_help()],
                                 fg_color="#606060",text=english_strings['help_button'],width=80)
        
        
        
        ip_device_start_lbl2=ctk.CTkLabel(master=main_frame, text=english_strings['ip_start'],justify="left", font=("",20),wraplength=600)
        ip_device_start_entry2=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24), 
                                     validate="key", validatecommand=(app.register(validate_ipaddr_start_root2), '%P'))
        ip_device_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        username_start_lbl2=ctk.CTkLabel(master=main_frame, text=english_strings['username_start_str'],justify="left", font=("",20),wraplength=600)
        username_start_entry2=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_username_start2), '%P'))
        username_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_start_lbl2=ctk.CTkLabel(master=main_frame, text=english_strings['password_start_lbl_str'],justify="left", font=("",20),wraplength=600)
        password_start_entry2=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_start2), '%P'))
        password_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        
        password_secret_start_lbl2=ctk.CTkLabel(master=main_frame, text=english_strings['password_secret_start_lbl_str'],justify="left", font=("",20),
                                                wraplength=600)
        password_secret_start_entry2=ctk.CTkEntry(master=main_frame,width=299,height=25, corner_radius=0,
                                     border_color="#006633",border_width=1,font=("",24),
                                    validate="key", validatecommand=(app.register(validate_password_secret_start2), '%P'))
        password_secret_start_validate_lbl2=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
        

        show_hide_button2 = ctk.CTkButton(master=main_frame, text=english_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_start_root2()],corner_radius=0)
        show_hide_secret_button2 = ctk.CTkButton(master=main_frame, text=english_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_secret_start_root2()],corner_radius=0)

    page4_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    page4_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
    page4_help_BTN.place(relx=0.1,rely=0.95, anchor=tk.CENTER)

    
    
    ip_device_start_lbl2.place(relx=0.04,rely=0.2,anchor=tk.W)
    ip_device_start_entry2.place(relx=0.5,rely=0.27,anchor=tk.CENTER)
    ip_device_start_validate_lbl2.place(relx=0.5,rely=0.34,anchor=tk.CENTER)
    
    username_start_lbl2.place(relx=0.04,rely=0.41,anchor=tk.W)
    username_start_entry2.place(relx=0.5,rely=0.48,anchor=tk.CENTER)
    username_start_validate_lbl2.place(relx=0.5,rely=0.55,anchor=tk.CENTER)
    
    password_start_lbl2.place(relx=0.04,rely=0.62,anchor=tk.W)
    password_start_entry2.place(relx=0.27,rely=0.69,anchor=tk.CENTER)
    password_start_validate_lbl2.place(relx=0.25,rely=0.79,anchor=tk.CENTER)
    show_hide_button2.place(relx=0.469,rely=0.69,anchor=tk.CENTER)
    
    password_secret_start_lbl2.place(relx=0.96,rely=0.62,anchor=tk.E)
    password_secret_start_entry2.place(relx=0.73,rely=0.69,anchor=tk.CENTER)
    password_secret_start_validate_lbl2.place(relx=0.75,rely=0.79,anchor=tk.CENTER)
    show_hide_secret_button2.place(relx=0.9298,rely=0.69,anchor=tk.CENTER)
    
#?__________________________________________________________________________________________________________________________________

def page4_invalid_values():
        help_window = ctk.CTkToplevel(master=main_frame)
        help_window.title("")
        help_window.geometry("360x165+780+500")
        help_window.resizable(False, False)

        help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['page4_invalid_str'],justify="left", wraplength=350)
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=help_window, text=english_strings['page4_invalid_str'],justify="left",wraplength=350)
        close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)

        help_lbl.pack(anchor="w",padx=5,pady=10)
        close_btn.pack()
    
        help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def check_page4_conditions():
    global ipaddr_start_val,ipaddr_start_val2,username_root_val2,password_root_val2,password_secret_root_val2
    global root_config_commands2,selected_checkbox,file2,non_root_device_info, root2_ip_entry
    if (validate_ip_address_root(ipaddr_start_val2) == False or username_root_val2 is None or 
        password_root_val2 is None or ipaddr_start_val2==ipaddr_start_val):
        page4_invalid_values()
        return
    else:
        indicate(page2_btn)
        ipaddr_start_val2=str(ipaddr_start_val2)
        username_root_val2=str(username_root_val2)
        password_root_val2=str(password_root_val2)
        password_secret_root_val2=str(password_secret_root_val2)

        non_root_device_info = {
            'device_type': 'cisco_ios',
            'ip': ipaddr_start_val2,
            'username': username_root_val2,
            'password': password_root_val2,
            'secret': password_secret_root_val2,

        }

        page_2()    
        toggle_visibility_password_wifi() 
        
#?__________________________________________________________________________________________________________________________________
    

def validate_ssid_name_root(new_value):
    global ssid_val
    pattern = re.compile(r'^[a-zA-Z0-9_-]*$')
    
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value=="polish":
                ssid_validate_lbl.configure(text=polish_strings['ssid_null'], text_color="gray")
            else:
                ssid_validate_lbl.configure(text=english_strings['ssid_null'], text_color="gray")
            ssid_val = '' 
        elif len(new_value)>32:
            if language_value=="polish":
                ssid_validate_lbl.configure(text=polish_strings['ssid_too_much_char'], text_color="red")
            else:
                ssid_validate_lbl.configure(text=english_strings['ssid_too_much_char'], text_color="red")
            
            return False
           
        else:
            if language_value=="polish":
                ssid_validate_lbl.configure(text=polish_strings['ssid_good'], text_color="#006633")
            else:
                ssid_validate_lbl.configure(text=english_strings['ssid_good'], text_color="#006633")
            ssid_val = new_value
        return True
    else:
        if language_value=="polish":
            ssid_validate_lbl.configure(text=polish_strings['ssid_incorrect_character'], text_color="red")
        else:
            ssid_validate_lbl.configure(text=english_strings['ssid_incorrect_character'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def validate_password_root(new_value):
    global password_val
    pattern = re.compile(r'^.*$')
    
    if pattern.match(new_value):
        if len(new_value) == 0:
            if language_value == "polish":
                password_validate_lbl.configure(text=polish_strings['password_null'], text_color="gray")
            else:
                password_validate_lbl.configure(text=english_strings['password_null'], text_color="gray")
            password_val = ''
            
        elif len(new_value) < 8:
            if language_value == "polish":
                password_validate_lbl.configure(text=polish_strings['password_characters_min'], text_color="red")
            else:
                password_validate_lbl.configure(text=english_strings['password_characters_min'], text_color="red") 
            password_val = ''
        
        elif not any(char.isdigit() for char in new_value):
            if language_value == "polish":
                password_validate_lbl.configure(text=polish_strings['password_digit'], text_color="red")
            else:
                password_validate_lbl.configure(text=english_strings['password_digit'], text_color="red")
            password_val = ''
            
        elif not any(char.isupper() for char in new_value):
            if language_value == "polish":
                password_validate_lbl.configure(text=polish_strings['password_letter'], text_color="red")
            else:
                password_validate_lbl.configure(text=english_strings['password_letter'], text_color="red")
            password_val = ''
        elif len(new_value)>63:
            if language_value=='polish':
                password_validate_lbl.configure(text=polish_strings['password_characters_max'], text_color="red")
            else:
                password_validate_lbl.configure(text=english_strings['password_characters_max'], text_color="red")
            
            return False
        else:
            if language_value == "polish":
                password_validate_lbl.configure(text=polish_strings['password_good'], text_color="#006633")
            else:
                password_validate_lbl.configure(text=english_strings['password_good'], text_color="#006633")
            password_val = new_value
        return True
    else:
        if language_value == "polish":
            password_validate_lbl.configure(text=polish_strings['password_invalid'], text_color="red")
        else:
            password_validate_lbl.configure(text=english_strings['password_invalid'], text_color="red")
        password_val = ''
        return False

#?__________________________________________________________________________________________________________________________________

def validate_ip_address(ip_str):
    try:
        ipaddress.IPv4Address(ip_str)
        return ip_str
    except ipaddress.AddressValueError:
        return False

#?__________________________________________________________________________________________________________________________________
    
def validate_ipaddr_root(new_value):
    global ipaddr_val
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value):
        
        if len(new_value) == 0:
            if language_value=="polish":
                ipaddr_validate_lbl.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ipaddr_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr_val = None
        elif len(new_value)>15:
            if(language_value=='polish'):
                ipaddr_validate_lbl.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ipaddr_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
        elif new_value.count('.')>3:
            if(language_value=='polish'):
                ipaddr_validate_lbl.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ipaddr_validate_lbl.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ipaddr_validate_lbl.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ipaddr_validate_lbl.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr_val = new_value
        return True
    else:
        if language_value=="polish":
            ipaddr_validate_lbl.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ipaddr_validate_lbl.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def validate_ipaddr2_root(new_value):
    global ipaddr2_val, root2_ip_entry
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value):
        
        if len(new_value) == 0:
            if language_value=="polish":
                ipaddr2_validate_lbl.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ipaddr2_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr2_val = None 
        elif len(new_value)>15:
            if(language_value=='polish'):
                ipaddr2_validate_lbl.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ipaddr2_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
        elif new_value.count('.')>3:
            if(language_value=='polish'):
                ipaddr2_validate_lbl.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ipaddr2_validate_lbl.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ipaddr2_validate_lbl.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ipaddr2_validate_lbl.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr2_val = new_value
        return True
    else:
        if language_value=="polish":
            ipaddr2_validate_lbl.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ipaddr2_validate_lbl.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False


#?__________________________________________________________________________________________________________________________________

ssid_val = None
ipaddr_val = None
ipaddr_val2 = None
password_val = None

def page2_show_help():
    help_window = ctk.CTkToplevel(master=main_frame)
    scroll_frame=ctk.CTkScrollableFrame(master=help_window,width=549,height=299,fg_color="transparent")
    help_window.title("")
    help_window.geometry("550x300+780+500")
    help_window.resizable(False, False)

    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    if language_value=='polish':
        help_lbl = ctk.CTkLabel(master=scroll_frame, text=polish_strings['page2_help_str'],justify="left", wraplength=520)
    elif language_value=='english':
        help_lbl = ctk.CTkLabel(master=scroll_frame, text=english_strings['page2_help_str'],justify="left",wraplength=520)
    close_btn=ctk.CTkButton(master=scroll_frame, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    scroll_frame.pack()
    help_lbl.pack(anchor="w",padx=5)
    close_btn.pack()
    
    help_window.grab_set()
    
#?__________________________________________________________________________________________________________________________________
    
def toggle_visibility_password_wifi():

    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        if language_value=='polish':
            show_hide_button_wifi.configure(text=polish_strings['button_root_hide'])
        else:
            show_hide_button_wifi.configure(text=english_strings['button_root_hide'])
    else:
        password_entry.configure(show="*")
        if language_value=='polish':
            show_hide_button_wifi.configure(text=polish_strings['button_root_show'])
        else:
            show_hide_button_wifi.configure(text=english_strings['button_root_show'])


#?__________________________________________________________________________________________________________________________________
    
def page_2():
    delete_main_frame()
    global file_path1, file_path2, ssid_validate_lbl, password_validate_lbl, ipaddr_validate_lbl,selected_checkbox,root_config_commands
    global ssid_val, password_val, ipaddr_val,ssid_entry,password_entry,root_ip_entry,netmask1_val,show_hide_button_wifi,ipaddr_val2
    global root2_ip_entry, ipaddr2_validate_lbl,netmask2_val
     
    if language_value == 'polish':
        if selected_checkbox=='Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
            page2_next_btn=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page2(),page2_check_values()],
                                    fg_color="#006633",text=polish_strings['next_button'],width=80)
            page2_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_4(),delete_file1() ,indicate(page4_btn),
                                        toggle_visibility_password_secret_start_root2(),toggle_visibility_password_start_root2()],
                                    fg_color="grey",text=polish_strings['back_button'],width=80)
            page2_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page2_show_help()],
                                    fg_color="#606060",text=polish_strings['help_button'],width=80)
            page2_label=ctk.CTkLabel(master=main_frame, text=polish_strings['page2_lbl_str'],justify="center", font=("",25),wraplength=600)
            
            
            ssid_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ssid_lbl_str'],justify="left", font=("",20),wraplength=600)
            ssid_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ssid_name_root), '%P'))
            ssid_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")

            password_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['password_lbl_str'],justify="left", font=("",20),wraplength=600)
            password_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_password_root), '%P'))
            password_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)

            root_ip_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['root_ip_lbl_str'],justify="left", font=("",20),wraplength=600)
            root_ip_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_root), '%P'))
            ipaddr_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)
        
        
        elif selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            page2_next_btn=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page2(),page2_check_values()],
                                    fg_color="#006633",text=polish_strings['next_button'],width=80)
            page2_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_4(),delete_file1() ,indicate(page4_btn),
                                        toggle_visibility_password_secret_start_root2(),toggle_visibility_password_start_root2()],
                                    fg_color="grey",text=polish_strings['back_button'],width=80)
            page2_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page2_show_help()],
                                    fg_color="#606060",text=polish_strings['help_button'],width=80)
            page2_label=ctk.CTkLabel(master=main_frame, text=polish_strings['page2_lbl_str'],justify="center", font=("",25),wraplength=600)
            
            
            ssid_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ssid_lbl_str'],justify="left", font=("",20),wraplength=600)
            ssid_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ssid_name_root), '%P'))
            ssid_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")

            password_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['password_lbl_str'],justify="left", font=("",20),wraplength=600)
            password_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_password_root), '%P'))
            password_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)

            root_ip_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['root_ip_lbl_str'],justify="left", font=("",20),wraplength=600)
            root_ip_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_root), '%P'))
            ipaddr_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)
            
            root2_ip_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['root2_ip_lbl_str'],justify="left", font=("",18),wraplength=600)
            root2_ip_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr2_root), '%P'))
            
            ipaddr2_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)
            root2_ip_lbl.place(relx=0.04,rely=0.79,anchor=tk.W)
            root2_ip_entry.place(relx=0.5,rely=0.86,anchor=tk.CENTER)
            ipaddr2_validate_lbl.place(relx=0.5,rely=93,anchor=tk.CENTER)
        
        show_hide_button_wifi = ctk.CTkButton(master=main_frame, text=polish_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_wifi()],corner_radius=0)

    else:
        
        if selected_checkbox=='Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
            page2_next_btn=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page2(),page2_check_values()],
                                    fg_color="#006633",text=english_strings['next_button'],width=80)
            page2_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_4(),delete_file1() ,indicate(page4_btn),
                                        toggle_visibility_password_secret_start_root2(),toggle_visibility_password_start_root2()],
                                    fg_color="grey",text=english_strings['back_button'],width=80)
            page2_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page2_show_help()],
                                    fg_color="#606060",text=english_strings['help_button'],width=80)
            page2_label=ctk.CTkLabel(master=main_frame, text=english_strings['page2_lbl_str'],justify="center", font=("",25),wraplength=600)
            
            
            ssid_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ssid_lbl_str'],justify="left", font=("",20),wraplength=600)
            ssid_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ssid_name_root), '%P'))
            ssid_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")

            password_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['password_lbl_str'],justify="left", font=("",20),wraplength=600)
            password_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_password_root), '%P'))
            password_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)

            root_ip_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['root_ip_lbl_str'],justify="left", font=("",20),wraplength=600)
            root_ip_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_root), '%P'))
            ipaddr_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)
        
        
        elif selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            page2_next_btn=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page2(),page2_check_values()],
                                    fg_color="#006633",text=english_strings['next_button'],width=80)
            page2_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_4(),delete_file1() ,indicate(page4_btn),
                                        toggle_visibility_password_secret_start_root2(),toggle_visibility_password_start_root2()],
                                    fg_color="grey",text=english_strings['back_button'],width=80)
            page2_help_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page2_show_help()],
                                    fg_color="#606060",text=english_strings['help_button'],width=80)
            page2_label=ctk.CTkLabel(master=main_frame, text=english_strings['page2_lbl_str'],justify="center", font=("",25),wraplength=600)
            
            
            ssid_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ssid_lbl_str'],justify="left", font=("",20),wraplength=600)
            ssid_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ssid_name_root), '%P'))
            ssid_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")

            password_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['password_lbl_str'],justify="left", font=("",20),wraplength=600)
            password_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_password_root), '%P'))
            password_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)

            root_ip_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['root_ip_lbl_str'],justify="left", font=("",20),wraplength=600)
            root_ip_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_root), '%P'))
            ipaddr_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)
            
            root2_ip_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['root2_ip_lbl_str'],justify="left", font=("",18),wraplength=600)
            root2_ip_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr2_root), '%P'))
            
            ipaddr2_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600)
            root2_ip_lbl.place(relx=0.04,rely=0.79,anchor=tk.W)
            root2_ip_entry.place(relx=0.5,rely=0.86,anchor=tk.CENTER)
            ipaddr2_validate_lbl.place(relx=0.5,rely=93,anchor=tk.CENTER)
        
        show_hide_button_wifi = ctk.CTkButton(master=main_frame, text=english_strings['button_root_show'], fg_color="#006633",height=30,width=40,
                                         command=lambda:[toggle_visibility_password_wifi()],corner_radius=0)
        
    netmask1_combobox_defaultvalue=ctk.StringVar(value='255.255.255.0')
    netmask1_combobox_values=['255.255.255.0','255.255.255.128','255.255.255.192','255.255.255.224','255.255.255.240','255.255.255.248','255.255.255.252']
    netmask1_combobox=ctk.CTkComboBox(master=main_frame,values=netmask1_combobox_values,
                                     variable=netmask1_combobox_defaultvalue,corner_radius=0,
                                     border_color="#006633",button_color="#006633",height=30,state="readonly")
    netmask2_combobox_defaultvalue=ctk.StringVar(value='255.255.255.0')
    netmask2_combobox_values=['255.255.255.0','255.255.255.128','255.255.255.192','255.255.255.224','255.255.255.240','255.255.255.248','255.255.255.252']
    netmask2_combobox=ctk.CTkComboBox(master=main_frame,values=netmask2_combobox_values,
                                     variable=netmask2_combobox_defaultvalue,corner_radius=0,
                                     border_color="#006633",button_color="#006633",height=30,state="readonly")
    
    netmask1_val=None
    netmask2_val=None
    ssid_val = None
    ipaddr_val = None
    ipaddr_val2 = None
    password_val = None

#?__________________________________________________________________________________________________________________________________

    def set_netmask_page2():
        global netmask1_val,netmask2_val
        netmask1_val=str(netmask1_combobox.get())
        if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            netmask2_val=str(netmask2_combobox.get())

    ssid_val = str(ssid_entry.get())
    ipaddr_val = str(root_ip_entry.get())
    password_val = str(password_entry.get())
    
    if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
        ipaddr_val2 = str(root2_ip_entry.get())
        netmask2_combobox.place(relx=0.855,rely=0.86,anchor=tk.CENTER)
    
    page2_next_btn.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    page2_back_BTN.place(relx=0.77, rely=0.95, anchor=tk.CENTER)
    page2_help_BTN.place(relx=0.1,rely=0.95, anchor=tk.CENTER)
    page2_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    
    

    ssid_lbl.place(relx=0.04, rely=0.15, anchor=tk.W)
    ssid_entry.place(relx=0.5, rely=0.23, anchor=tk.CENTER)
    ssid_validate_lbl.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

    password_lbl.place(relx=0.04, rely=0.37, anchor=tk.W)
    password_entry.place(relx=0.5, rely=0.44, anchor=tk.CENTER)
    password_validate_lbl.place(relx=0.5, rely=0.51, anchor=tk.CENTER)
    show_hide_button_wifi.place(relx=0.9298,rely=0.44,anchor=tk.CENTER)

    
    netmask1_combobox.place(relx=0.855,rely=0.65,anchor=tk.CENTER)
    root_ip_lbl.place(relx=0.04, rely=0.58, anchor=tk.W)
    root_ip_entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    ipaddr_validate_lbl.place(relx=0.5, rely=0.72, anchor=tk.CENTER)

#?__________________________________________________________________________________________________________________________________

def page2_invalid_values():
    help_window = ctk.CTkToplevel(master=main_frame)
    
    help_window.title("")
    help_window.geometry("550x230+780+500")
    help_window.resizable(False, False)

    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    if language_value=='polish':
        help_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['page2_ivalid_values_str'],justify="left", wraplength=520)
    elif language_value=='english':
        help_lbl = ctk.CTkLabel(master=help_window, text=english_strings['page2_ivalid_values_str'],justify="left",wraplength=520)
    close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    help_lbl.pack(anchor="w",padx=5)
    close_btn.pack()
    
    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def page2_check_values():
    global ssid_val, ipaddr_val, password_val, root_config_commands, file1, netmask1_val,ipaddr2_val
    delete_file1()
    if selected_checkbox=='Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
        if ssid_val == '' or ipaddr_val == '' or password_val == '' or validate_ip_address(ipaddr_val)==False or validate_password_root(password_val)==False or validate_ssid_name_root(ssid_val)==False:
            page2_invalid_values()
            return
        else:
            indicate(page5_btn)
            root_config_commands=None
            if selected_checkbox == 'Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
                root_config_commands = [
                    'configure terminal',
                    'hostname root',
                    'interface dot11Radio 0',
                    'station-role root',
                    'exit',
                    'guest-mode',
                    'authentication open',
                    'authentication key-management wpa version 2',
                    'exit',
                    'interface bvi 1',
                    'no shutdown',
                    'exit',
                    'interface dot11Radio 0',
                    'encryption mode ciphers aes-ccm',
                    'channel least-congested',
                    'no shutdown',
                    'exit'
                    ]
            else:
                root_config_commands= [
                    'configure terminal',
                    'hostname root',
                    'authentication open',
                    'authentication key-management wpa version 2',
                    'exit',
                    'interface dot11Radio 0',
                    'encryption mode ciphers aes-ccm',
                    'station-role root bridge',
                    'exit',
                    'interface bvi 1',
                    'no shutdown',
                    'exit',
                    'interface gigabitEthernet 0',
                    'no shutdown',
                    'exit',
                    'interface dot11Radio 0',
                    'no shutdown',
                    'exit'
                ]    
    elif selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
        if (ssid_val == '' or ipaddr_val == '' or password_val == '' or ipaddr2_val=='' or validate_ip_address(ipaddr_val)==False or 
            validate_ip_address(ipaddr2_val)==False or validate_password_root(password_val)==False or 
            validate_ssid_name_root(ssid_val)==False or ipaddr2_val==ipaddr_val):
            page2_invalid_values()
            return
        else:
            indicate(page5_btn)
            root_config_commands=None
            if selected_checkbox == 'Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
                root_config_commands = [
                    'configure terminal',
                    'hostname root',
                    'interface dot11Radio 0',
                    'station-role root',
                    'exit',
                    'guest-mode',
                    'authentication open',
                    'authentication key-management wpa version 2',
                    'exit',
                    'interface bvi 1',
                    'no shutdown',
                    'exit',
                    'interface dot11Radio 0',
                    'encryption mode ciphers aes-ccm',
                    'channel least-congested',
                    'no shutdown',
                    'exit'
                    ]
            else:
                root_config_commands= [
                    'configure terminal',
                    'hostname root',
                    'authentication open',
                    'authentication key-management wpa version 2',
                    'exit',
                    'interface dot11Radio 0',
                    'encryption mode ciphers aes-ccm',
                    'station-role root bridge',
                    'exit',
                    'interface bvi 1',
                    'no shutdown',
                    'exit',
                    'interface gigabitEthernet 0',
                    'no shutdown',
                    'exit',
                    'interface dot11Radio 0',
                    'no shutdown',
                    'exit'
                ]
    if selected_checkbox == 'Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
        with open(file_path1, 'w') as file1:
            root_config_commands.insert(5,'dot11 ssid ' + ssid_val)
            root_config_commands.insert(9,'wpa-psk ascii ' + password_val)
            root_config_commands.insert(12,'ip address ' + ipaddr_val + ' '+netmask1_val)
            root_config_commands.insert(17,'ssid ' + ssid_val)
            for line in root_config_commands:
                file1.write(str(line) + '\n')
    else:
        with open(file_path1, 'w') as file1:
            root_config_commands.insert(2,'dot11 ssid ' + ssid_val)
            root_config_commands.insert(5,'wpa-psk ascii ' + password_val)
            root_config_commands.insert(10,'ssid ' + ssid_val)
            root_config_commands.insert(13,'ip address ' + ipaddr_val + ' '+netmask1_val)
            root_config_commands.insert(17,'ip address ' + ipaddr2_val + ' '+netmask2_val)
            for line in root_config_commands:
                file1.write(str(line) + '\n')

    page_5()
    file1.close()

#?__________________________________________________________________________________________________________________________________

def validate_ipaddr_nonroot(new_value):
    global ipaddr_nonroot_val
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value):
        
        if len(new_value) == 0:
            if language_value=="polish":
                ipaddr_nonroot_validate_lbl.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ipaddr_nonroot_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr_nonroot_val = None
        elif len(new_value)>15:
            if(language_value=='polish'):
                ipaddr_nonroot_validate_lbl.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ipaddr_nonroot_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
        elif new_value.count('.')>3:
            if(language_value=='polish'):
                ipaddr_nonroot_validate_lbl.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ipaddr_nonroot_validate_lbl.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ipaddr_nonroot_validate_lbl.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ipaddr_nonroot_validate_lbl.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr_nonroot_val = new_value
        return True
    else:
        if language_value=="polish":
            ipaddr_nonroot_validate_lbl.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ipaddr_nonroot_validate_lbl.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False
    

#?__________________________________________________________________________________________________________________________________

def validate_ipaddr2_nonroot(new_value):
    global ipaddr2_nonroot_val
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value):
        
        if len(new_value) == 0:
            if language_value=="polish":
                ipaddr2_nonroot_validate_lbl.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ipaddr2_nonroot_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr2_nonroot_val = None 
        elif len(new_value)>15:
            if(language_value=='polish'):
                ipaddr2_nonroot_validate_lbl.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ipaddr2_nonroot_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
        elif new_value.count('.')>3:
            if(language_value=='polish'):
                ipaddr2_nonroot_validate_lbl.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ipaddr2_nonroot_validate_lbl.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ipaddr2_nonroot_validate_lbl.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ipaddr2_nonroot_validate_lbl.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr2_nonroot_val = new_value
        return True
    else:
        if language_value=="polish":
            ipaddr2_nonroot_validate_lbl.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ipaddr2_nonroot_validate_lbl.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________
 
def validate_ipaddr_dg_nonroot(new_value):
    global ipaddr_dg_nonroot_val
    pattern = re.compile(r'^[0-9.]{0,15}$')
    if pattern.match(new_value):
        
        if len(new_value) == 0:
            if language_value=="polish":
                ipaddr_dg_nonroot_validate_lbl.configure(text=polish_strings['ip_null'], text_color="gray")
            else:
                ipaddr_dg_nonroot_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
            ipaddr_dg_nonroot_val = None  
        elif len(new_value)>15:
            if(language_value=='polish'):
                ipaddr_dg_nonroot_validate_lbl.configure(text=polish_strings['ip_morethan15'], text_color="gray")
            else:
                ipaddr_dg_nonroot_validate_lbl.configure(text=english_strings['ip_null'], text_color="gray")
        elif new_value.count('.')>3:
            if(language_value=='polish'):
                ipaddr_dg_nonroot_validate_lbl.configure(text=polish_strings['ip_moredots'], text_color="red")
            else:
                ipaddr_dg_nonroot_validate_lbl.configure(text=english_strings['ip_moredots'], text_color="red")
            return FALSE
        else:
            if language_value=="polish":
                ipaddr_dg_nonroot_validate_lbl.configure(text=polish_strings['ip_ok'], text_color="#006633")
            else:
                ipaddr_dg_nonroot_validate_lbl.configure(text=english_strings['ip_ok'], text_color="#006633")
            ipaddr_dg_nonroot_val = new_value
        return True
    else:
        if language_value=="polish":
            ipaddr_dg_nonroot_validate_lbl.configure(text=polish_strings['ip_incorrect_character'], text_color="red")
        else:
            ipaddr_dg_nonroot_validate_lbl.configure(text=english_strings['ip_incorrect_character'], text_color="red")
        return False

#?__________________________________________________________________________________________________________________________________

def page_5():
    delete_main_frame()
    global ipaddr_nonroot_val, ipaddr_nonroot_validate_lbl,ipaddr_dg_nonroot_validate_lbl,ipaddr_dg_nonroot_val, netmask_val,password_entry
    global ipaddr_nonroot_entry, ipaddr2_nonroot_val, ipaddr2_nonroot_validate_lbl,netmask3_val,ipaddr2_nonroot_entry

    ipaddr_nonroot_val=None
    ipaddr2_nonroot_val=None
    ipaddr_dg_nonroot_val=None
    netmask_val=None
    netmask3_val=None
    
    if language_value=='polish':
        if selected_checkbox=='Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
            page5_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_2(),delete_file1(),indicate(page2_btn),
                        toggle_visibility_password_wifi()],
                                    fg_color="grey",text=polish_strings['back_button'],width=80)
            
            page5_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page5(),page5_checkvalues()],
                                    fg_color="#006633",text=polish_strings['next_button'],width=80)
            page5_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['page5_default_lbl'],justify="left", font=("",25),wraplength=600)

            ipaddr_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ipaddr_nonroot_lbl'],justify="left", font=("",20),wraplength=600)
            ipaddr_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_nonroot), '%P'))
            ipaddr_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
            ipaddr_dg_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ipaddr_dg_nonroot_lbl'],justify="left", font=("",20),
                                               wraplength=600)

            ipaddr_dg_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_dg_nonroot), '%P'))
            ipaddr_dg_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),
                                                        wraplength=600,fg_color="transparent")
        else:
            page5_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_2(),delete_file1(),indicate(page2_btn),
                        toggle_visibility_password_wifi()],
                                    fg_color="grey",text=polish_strings['back_button'],width=80)
            
            page5_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page5(),page5_checkvalues()],
                                    fg_color="#006633",text=polish_strings['next_button'],width=80)
            page5_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['page5_default_lbl'],justify="left", font=("",25),wraplength=600)

            ipaddr_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ipaddr_nonroot_lbl'],justify="left", font=("",20),wraplength=600)
            ipaddr_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_nonroot), '%P'))
            ipaddr_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
            ipaddr_dg_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['ipaddr_dg_nonroot_lbl'],justify="left", font=("",20),
                                               wraplength=600)

            ipaddr_dg_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_dg_nonroot), '%P'))
            ipaddr_dg_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),
                                                        wraplength=600,fg_color="transparent")
            
            ipaddr2_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['nonroot2_ip_lbl_str'],justify="left", font=("",20),wraplength=600)
            ipaddr2_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr2_nonroot), '%P'))
            ipaddr2_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
            
            ipaddr2_nonroot_lbl.place(relx=0.04,rely=0.65,anchor=tk.W)
            ipaddr2_nonroot_entry.place(relx=0.5,rely=0.75,anchor=tk.CENTER)
            ipaddr2_nonroot_validate_lbl.place(relx=0.5,rely=0.82,anchor=tk.CENTER)
        
    else:
        if selected_checkbox=='Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
            page5_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_2(),delete_file1(),indicate(page2_btn),
                        toggle_visibility_password_wifi()],
                                    fg_color="grey",text=english_strings['back_button'],width=80)
            
            page5_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page5(),page5_checkvalues()],
                                    fg_color="#006633",text=english_strings['next_button'],width=80)
            page5_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['page5_default_lbl'],justify="left", font=("",25),wraplength=600)

            ipaddr_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ipaddr_nonroot_lbl'],justify="left", font=("",20),wraplength=600)
            ipaddr_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_nonroot), '%P'))
            ipaddr_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
            ipaddr_dg_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ipaddr_dg_nonroot_lbl'],justify="left", font=("",20),
                                               wraplength=600)

            ipaddr_dg_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_dg_nonroot), '%P'))
            ipaddr_dg_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),
                                                        wraplength=600,fg_color="transparent")
        else:
            page5_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_2(),delete_file1(),indicate(page2_btn),
                        toggle_visibility_password_wifi()],
                                    fg_color="grey",text=english_strings['back_button'],width=80)
            
            page5_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[set_netmask_page5(),page5_checkvalues()],
                                    fg_color="#006633",text=english_strings['next_button'],width=80)
            page5_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['page5_default_lbl'],justify="left", font=("",25),wraplength=600)

            ipaddr_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ipaddr_nonroot_lbl'],justify="left", font=("",20),wraplength=600)
            ipaddr_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_nonroot), '%P'))
            ipaddr_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
            ipaddr_dg_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['ipaddr_dg_nonroot_lbl'],justify="left", font=("",20),
                                               wraplength=600)

            ipaddr_dg_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr_dg_nonroot), '%P'))
            ipaddr_dg_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),
                                                        wraplength=600,fg_color="transparent")
            
            ipaddr2_nonroot_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['nonroot2_ip_lbl_str'],justify="left", font=("",20),wraplength=600)
            ipaddr2_nonroot_entry=ctk.CTkEntry(master=main_frame,width=600,height=25, corner_radius=0,
                                        border_color="#006633",border_width=1,font=("",24), 
                                        validate="key", validatecommand=(app.register(validate_ipaddr2_nonroot), '%P'))
            ipaddr2_nonroot_validate_lbl=ctk.CTkLabel(master=main_frame, text='',justify="left", font=("",20),wraplength=600,fg_color="transparent")
            
            ipaddr2_nonroot_lbl.place(relx=0.04,rely=0.65,anchor=tk.W)
            ipaddr2_nonroot_entry.place(relx=0.5,rely=0.75,anchor=tk.CENTER)
            ipaddr2_nonroot_validate_lbl.place(relx=0.5,rely=0.82,anchor=tk.CENTER)
        
    
            
    netmask_combobox_defaultvalue=ctk.StringVar(value='255.255.255.0')
    netmask_combobox_values=['255.255.255.0','255.255.255.128','255.255.255.192','255.255.255.224','255.255.255.240','255.255.255.248','255.255.255.252']
    netmask_combobox=ctk.CTkComboBox(master=main_frame,values=netmask_combobox_values,
                                     variable=netmask_combobox_defaultvalue,corner_radius=0,
                                     border_color="#006633",button_color="#006633",height=30,state="readonly")
    
    netmask3_combobox_defaultvalue=ctk.StringVar(value='255.255.255.0')
    netmask3_combobox_values=['255.255.255.0','255.255.255.128','255.255.255.192','255.255.255.224','255.255.255.240','255.255.255.248','255.255.255.252']
    netmask3_combobox=ctk.CTkComboBox(master=main_frame,values=netmask3_combobox_values,
                                     variable=netmask3_combobox_defaultvalue,corner_radius=0,
                                     border_color="#006633",button_color="#006633",height=30,state="readonly")
    
    def set_netmask_page5():
            global netmask_val, netmask3_val
            netmask_val=str(netmask_combobox.get())
            if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox =='Wireless Access Point':
                netmask3_val=str(netmask3_combobox.get())
    
    ipaddr_nonroot_val=str(ipaddr_nonroot_entry.get())
    ipaddr_dg_nonroot_val=str(ipaddr_dg_nonroot_entry.get())
    if selected_checkbox=='Bezprzewodowy punkt dostępowy'or selected_checkbox=='Wireless Access Point':
        ipaddr2_nonroot_val=str(ipaddr2_nonroot_entry.get())
        netmask3_combobox.place(relx=0.855,rely=0.75,anchor=tk.CENTER)

    page5_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
    page5_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
    page5_lbl.place(relx=0.5,rely=0.05,anchor=tk.CENTER)

    netmask_combobox.place(relx=0.855,rely=0.25,anchor=tk.CENTER)
    ipaddr_nonroot_lbl.place(relx=0.04,rely=0.15,anchor=tk.W)
    ipaddr_nonroot_entry.place(relx=0.5,rely=0.25,anchor=tk.CENTER)
    ipaddr_nonroot_validate_lbl.place(relx=0.5,rely=0.33,anchor=tk.CENTER)

    ipaddr_dg_nonroot_lbl.place(relx=0.04,rely=0.40,anchor=tk.W)
    ipaddr_dg_nonroot_entry.place(relx=0.5,rely=0.50,anchor=tk.CENTER)
    ipaddr_dg_nonroot_validate_lbl.place(relx=0.5,rely=0.57,anchor=tk.CENTER)

#?__________________________________________________________________________________________________________________________________

def page5_invalid_values():
    help_window = ctk.CTkToplevel(master=main_frame)
    
    help_window.title("")
    help_window.geometry("550x160+780+500")
    help_window.resizable(False, False)

    help_window.after(300, lambda: help_window.iconbitmap("help.ico"))
    if language_value=='polish':
        help_lbl = ctk.CTkLabel(master=help_window, text=polish_strings['page5_ivalid_values_str'],justify="left", wraplength=520)
    elif language_value=='english':
        help_lbl = ctk.CTkLabel(master=help_window, text=english_strings['page5_ivalid_values_str'],justify="left",wraplength=520)
    close_btn=ctk.CTkButton(master=help_window, command=lambda:[help_window.destroy(),help_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    help_lbl.pack(anchor="w",padx=5)
    close_btn.pack()
    
    help_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def page5_checkvalues():
    global ipaddr_nonroot_val,ipaddr_dg_nonroot_val, non_root_config_commands,file_path2,file2, ssid_val
    global password_val,netmask_val,ipaddr2_nonroot_val, ipaddr_val,ipaddr2_val
    
    delete_file2()
    if selected_checkbox=='Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
        if ipaddr_nonroot_val==ipaddr_val or ipaddr_nonroot_val == '' or ipaddr_dg_nonroot_val == '' or ipaddr_nonroot_val==None or ipaddr_dg_nonroot_val==None or validate_ip_address(ipaddr_dg_nonroot_val)==False or validate_ip_address(ipaddr_nonroot_val)==False :
            page5_invalid_values()
            return
        else:
            indicate(page6_btn)
            non_root_config_commands=None
            if selected_checkbox == 'Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
                non_root_config_commands = [
                'configure terminal',
                'hostname repeater',
                'interface dot11Radio 0',
                'encryption mode ciphers aes-ccm',
                'exit',
                'station-role repeater',
                'exit',
                'guest-mode',
                'infrastructure-ssid',
                'authentication open',
                'authentication key-management wpa version 2',
                'exit',
                'interface bvI 1',
                'no shutdown',
                'exit',
                'interface dot11Radio 0',
                'no shutdown',
                'exit'
                    ]
            else:
                non_root_config_commands= [
                    'configure terminal',
                    'hostname non_root',
                    'infrastructure-ssid',
                    'authentication open',
                    'authentication key-management wpa version 2',
                    'exit',
                    'interface dot11Radio 0',
                    'encryption mode ciphers aes-ccm',
                    'station-role non-root bridge',
                    'exit',
                    'interface gigabitEthernet 0',
                    'exit',
                    'interface bvi 1',
                    'no shutdown',
                    'exit',
                    'interface gigabitEthernet 0',
                    'no shutdown',
                    'exit',
                    'interface dot11Radio 0',
                    'no shutdown',
                    'exit'
                  
                ]
    elif selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
        if (ipaddr_nonroot_val==ipaddr_val or ipaddr_nonroot_val == ''or ipaddr2_nonroot_val=='' or ipaddr_dg_nonroot_val == '' 
            or ipaddr_nonroot_val==None or ipaddr2_nonroot_val==None or ipaddr_dg_nonroot_val==None or 
            validate_ip_address(ipaddr_dg_nonroot_val)==False or validate_ip_address(ipaddr_nonroot_val)==False or 
            validate_ip_address(ipaddr2_nonroot_val)==False or ipaddr2_nonroot_val==ipaddr_nonroot_val or ipaddr2_nonroot_val==ipaddr2_val or
            ipaddr_nonroot_val==ipaddr_val):
            page5_invalid_values()
            return
        else:
            indicate(page6_btn)
            non_root_config_commands=None
            if selected_checkbox == 'Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
                non_root_config_commands = [
                'configure terminal',
                'hostname repeater',
                'interface dot11Radio 0',
                'encryption mode ciphers aes-ccm',
                'exit',
                'station-role repeater',
                'exit',
                'guest-mode',
                'infrastructure-ssid',
                'authentication open',
                'authentication key-management wpa version 2',
                'exit',
                'interface bvI 1',
                'no shutdown',
                'exit',
                'interface dot11Radio 0',
                'no shutdown',
                'exit'
                    ]
            else:
                non_root_config_commands= [
                    'configure terminal',
                    'hostname non_root',
                    'infrastructure-ssid',
                    'authentication open',
                    'authentication key-management wpa version 2',
                    'exit',
                    'interface dot11Radio 0',
                    'encryption mode ciphers aes-ccm',
                    'station-role non-root bridge',
                    'exit',
                    'interface gigabitEthernet 0',
                    'exit',
                    'interface bvi 1',
                    'no shutdown',
                    'exit',
                    'interface gigabitEthernet 0',
                    'no shutdown',
                    'exit',
                    'interface dot11Radio 0',
                    'no shutdown',
                    'exit'
                ]
            
    if selected_checkbox == 'Most Wi-Fi' or selected_checkbox=='Wi-Fi Bridge':
        with open(file_path2, 'w') as file2:
            non_root_config_commands.insert(4,'ssid ' + ssid_val)
            non_root_config_commands.insert(8,'dot11 ssid ' + ssid_val)
            non_root_config_commands.insert(13,'wpa-psk ascii ' + password_val)
            non_root_config_commands.insert(16,'ip address ' + ipaddr_nonroot_val +' ' + netmask_val)
            non_root_config_commands.insert(19,'ip default-gateway ' + ipaddr_dg_nonroot_val)
            for line in non_root_config_commands:
                file2.write(str(line) + '\n')
    else:
        with open(file_path2, 'w') as file2:
            non_root_config_commands.insert(2,'dot11 ssid ' + ssid_val)
            non_root_config_commands.insert(6,'wpa-psk ascii ' + password_val)
            non_root_config_commands.insert(11,'ssid ' + ssid_val)
            non_root_config_commands.insert(14,'ip address ' + ipaddr2_nonroot_val + ' '+netmask3_val)
            non_root_config_commands.insert(17,'ip address  ' + ipaddr_nonroot_val + ' '+netmask_val)
            non_root_config_commands.insert(20,'ip default-gateway ' + ipaddr_dg_nonroot_val)
            for line in non_root_config_commands:
                    file2.write(str(line) + '\n')
        
        
    page_6()
    file2.close()

#?__________________________________________________________________________________________________________________________________

def toggle_visibility_last_page():
    current_text = label_text.get()
    current_text2=label_text2.get()
    current_text3=label_text3.get()
    current_text4=label_text4.get()
    current_text5=label_text5.get()
    
    if current_text == hidden_text and current_text2 == hidden_text2 and current_text3==hidden_text3 and current_text4==hidden_text4 and current_text5==hidden_text5:
        label_text.set(original_text)
        label_text2.set(original_text2)
        label_text3.set(original_text3)
        label_text4.set(original_text4)
        label_text5.set(original_text5)
        if language_value=='polish':
            show_hide_last_page.configure(text=polish_strings['last_page_passwords_hide'])
        else:
            show_hide_last_page.configure(text=english_strings['last_page_passwords_hide'])
    else:
        label_text.set(hidden_text)
        label_text2.set(hidden_text2)
        label_text3.set(hidden_text3)
        label_text4.set(hidden_text4)
        label_text5.set(hidden_text5)
        if language_value=='polish': 
            show_hide_last_page.configure(text=polish_strings['last_page_passwords_show'])
        else:
            show_hide_last_page.configure(text=english_strings['last_page_passwords_show'])

#?__________________________________________________________________________________________________________________________________

def page_6():
    delete_main_frame()
    global root_device_info,non_root_device_info,root_config_commands,non_root_config_commands
    global ipaddr_start_val, username_root_val,password_root_val,password_secret_root_val, ipaddr_nonroot_val, username_root_val2
    global root_device_info_lbl3,root_device_info_lbl4,root_device_config_lbl3,show_hide_last_page,original_text,hidden_text,label_text
    global original_text2, hidden_text2,label_text2, original_text3, hidden_text3, label_text3
    global password_val, ssid_val, ipaddr_val, original_text4, hidden_text4, label_text4, original_text5, hidden_text5 
    global label_text5,send_to_non_root_btn,ipaddr2_val,ipaddr2_nonroot_val
    if language_value=='polish':
        page6_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_5(),delete_file2(),indicate(page5_btn),
                                                    ],
                                 fg_color="grey",text=polish_strings['back_button'],width=80)
        
        page6_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_7(),indicate(page7_btn)],
                                 fg_color="#006633",text=polish_strings['next_button'],width=80)

        final_step_lbl=ctk.CTkLabel(master=main_frame, text=polish_strings['final_step_lbl_str'],justify="left", wraplength=649,font=('',16))

        send_to_root_btn=ctk.CTkButton(master=main_frame,fg_color="#006633",text=polish_strings['send_to_root_button_text'],font=('',14),
                                       command=lambda:[send_config_to_root()])
        send_to_non_root_btn=ctk.CTkButton(master=main_frame,fg_color="#006633",text=polish_strings['send_to_non_root_button_text'],font=('',14),
                                       command=lambda:[send_config_to_nonroot()])
        
        root_device_info_lbl1=ctk.CTkLabel(master=main_frame,text=polish_strings['ip_last_page']+': '+ ipaddr_start_val,font=('',14))
        root_device_info_lbl2=ctk.CTkLabel(master=main_frame,text=polish_strings['username_last_page']+': '+ username_root_val,font=('',14))
        
        original_text = password_root_val
        hidden_text = "*" * len(original_text)
        label_text = tk.StringVar()
        label_text.set(hidden_text)
        root_device_info_lbl3=ctk.CTkLabel(master=main_frame,text=polish_strings['password_last_page']+': ',font=('',14))
        root_device_info_lbl3_1=ctk.CTkLabel(master=main_frame,textvariable=label_text,font=('',14))
        
        original_text2 = password_secret_root_val
        hidden_text2 = "*" * len(original_text2)
        label_text2 = tk.StringVar()
        label_text2.set(hidden_text2)
        root_device_info_lbl4=ctk.CTkLabel(master=main_frame,text=polish_strings['password_en_last_page']+': ',font=('',14))
        root_device_info_lbl4_1=ctk.CTkLabel(master=main_frame,textvariable=label_text2,font=('',14))
        
        
        root_device_config_lbl1=ctk.CTkLabel(master=main_frame,text=polish_strings['ip2_last_page']+': '+ ipaddr_val,font=('',14))
        root_device_config_lbl2=ctk.CTkLabel(master=main_frame,text=polish_strings['ssid_last_page']+': '+ ssid_val,font=('',14))
        
        if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            root_device_config_lbl1_2=ctk.CTkLabel(master=main_frame,text=polish_strings['ip3_last_page']+': '+ ipaddr2_val,font=('',14))
            root_device_config_lbl1_2.place(relx=0.95,rely=0.47,anchor=tk.E)
        
        original_text3 = password_val
        hidden_text3 = "*" * len(original_text3)
        label_text3 = tk.StringVar()
        label_text3.set(hidden_text3)
        root_device_config_lbl3=ctk.CTkLabel(master=main_frame,text=polish_strings['password2_last_page']+': ' ,font=('',14))
        root_device_config_lbl3_1=ctk.CTkLabel(master=main_frame,textvariable=label_text3,font=('',14),wraplength=260)
        
        non_root_values_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['values_non_root_last_page'],font=('',16))
        
        non_root_device_info_lbl1=ctk.CTkLabel(master=main_frame,text=polish_strings['ip_last_page']+': '+ ipaddr_start_val2,font=('',14))
        non_root_device_info_lbl2=ctk.CTkLabel(master=main_frame,text=polish_strings['username_last_page']+': '+ username_root_val2,font=('',14))
        
        
        original_text4 = password_root_val2
        hidden_text4 = "*" * len(original_text4)
        label_text4 = tk.StringVar()
        label_text4.set(hidden_text4)
        
        non_root_device_info_lbl3=ctk.CTkLabel(master=main_frame,text=polish_strings['password_last_page']+': ',font=('',14))
        non_root_device_info_lbl3_1=ctk.CTkLabel(master=main_frame,textvariable=label_text4,font=('',14))
        
        
        
        original_text5 = password_secret_root_val2
        hidden_text5 = "*" * len(original_text5)
        label_text5 = tk.StringVar()
        label_text5.set(hidden_text5)
 
        non_root_device_info_lbl4=ctk.CTkLabel(master=main_frame,text=polish_strings['password_en_last_page']+': ' ,font=('',14))
        non_root_device_info_lbl4_1=ctk.CTkLabel(master=main_frame,textvariable=label_text5,font=('',14))
        
        non_root_device_config_lbl1=ctk.CTkLabel(master=main_frame,text=polish_strings['ip2_last_page']+': '+ ipaddr_nonroot_val,font=('',14))
        non_root_device_config_lbl2=ctk.CTkLabel(master=main_frame,text=polish_strings['ip_dg_last_page']+': '+ ipaddr_dg_nonroot_val,font=('',14))
        if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            non_root_device_config_lbl1_2=ctk.CTkLabel(master=main_frame,text=polish_strings['ip3_last_page']+': '+ ipaddr2_nonroot_val,font=('',14))
            non_root_device_config_lbl1_2.place(relx=0.95,rely=0.72,anchor=tk.E)
        
        
        show_hide_last_page=ctk.CTkButton(master=main_frame, text=polish_strings['last_page_passwords_show'], fg_color="#006633",height=20,width=40,
                                         command=lambda:[toggle_visibility_last_page()],corner_radius=0)
    else:
        page6_back_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_5(),delete_file2(),indicate(page5_btn),
                                                    ],
                                 fg_color="grey",text=english_strings['back_button'],width=80)
        
        page6_next_BTN=ctk.CTkButton(master=main_frame,command=lambda:[page_7(),indicate(page7_btn)],
                                 fg_color="#006633",text=english_strings['next_button'],width=80)

        final_step_lbl=ctk.CTkLabel(master=main_frame, text=english_strings['final_step_lbl_str'],justify="left", wraplength=649,font=('',16))

        send_to_root_btn=ctk.CTkButton(master=main_frame,fg_color="#006633",text=english_strings['send_to_root_button_text'],font=('',14),
                                       command=lambda:[send_config_to_root()])
        send_to_non_root_btn=ctk.CTkButton(master=main_frame,fg_color="#006633",text=english_strings['send_to_non_root_button_text'],font=('',14),
                                       command=lambda:[send_config_to_nonroot()])
        
        root_device_info_lbl1=ctk.CTkLabel(master=main_frame,text=english_strings['ip_last_page']+': '+ ipaddr_start_val,font=('',14))
        root_device_info_lbl2=ctk.CTkLabel(master=main_frame,text=english_strings['username_last_page']+': '+ username_root_val,font=('',14))
        
        original_text = password_root_val
        hidden_text = "*" * len(original_text)
        label_text = tk.StringVar()
        label_text.set(hidden_text)
        root_device_info_lbl3=ctk.CTkLabel(master=main_frame,text=english_strings['password_last_page']+': ',font=('',14))
        root_device_info_lbl3_1=ctk.CTkLabel(master=main_frame,textvariable=label_text,font=('',14))
        
        original_text2 = password_secret_root_val
        hidden_text2 = "*" * len(original_text2)
        label_text2 = tk.StringVar()
        label_text2.set(hidden_text2)
        root_device_info_lbl4=ctk.CTkLabel(master=main_frame,text=english_strings['password_en_last_page']+': ',font=('',14))
        root_device_info_lbl4_1=ctk.CTkLabel(master=main_frame,textvariable=label_text2,font=('',14))
        
        
        root_device_config_lbl1=ctk.CTkLabel(master=main_frame,text=english_strings['ip2_last_page']+': '+ ipaddr_val,font=('',14))
        root_device_config_lbl2=ctk.CTkLabel(master=main_frame,text=english_strings['ssid_last_page']+': '+ ssid_val,font=('',14))
        
        if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            root_device_config_lbl1_2=ctk.CTkLabel(master=main_frame,text=english_strings['ip3_last_page']+': '+ ipaddr2_val,font=('',14))
            root_device_config_lbl1_2.place(relx=0.95,rely=0.52,anchor=tk.E)
        
        original_text3 = password_val
        hidden_text3 = "*" * len(original_text3)
        label_text3 = tk.StringVar()
        label_text3.set(hidden_text3)
        root_device_config_lbl3=ctk.CTkLabel(master=main_frame,text=english_strings['password2_last_page']+': ' ,font=('',14))
        root_device_config_lbl3_1=ctk.CTkLabel(master=main_frame,textvariable=label_text3,font=('',14),wraplength=260)
        
        non_root_values_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['values_non_root_last_page'],font=('',16))
        
        non_root_device_info_lbl1=ctk.CTkLabel(master=main_frame,text=english_strings['ip_last_page']+': '+ ipaddr_start_val2,font=('',14))
        non_root_device_info_lbl2=ctk.CTkLabel(master=main_frame,text=english_strings['username_last_page']+': '+ username_root_val2,font=('',14))
        
        
        original_text4 = password_root_val2
        hidden_text4 = "*" * len(original_text4)
        label_text4 = tk.StringVar()
        label_text4.set(hidden_text4)
        
        non_root_device_info_lbl3=ctk.CTkLabel(master=main_frame,text=english_strings['password_last_page']+': ',font=('',14))
        non_root_device_info_lbl3_1=ctk.CTkLabel(master=main_frame,textvariable=label_text4,font=('',14))
        
        
        
        original_text5 = password_secret_root_val2
        hidden_text5 = "*" * len(original_text5)
        label_text5 = tk.StringVar()
        label_text5.set(hidden_text5)
 
        non_root_device_info_lbl4=ctk.CTkLabel(master=main_frame,text=english_strings['password_en_last_page']+': ' ,font=('',14))
        non_root_device_info_lbl4_1=ctk.CTkLabel(master=main_frame,textvariable=label_text5,font=('',14))
        
        non_root_device_config_lbl1=ctk.CTkLabel(master=main_frame,text=english_strings['ip2_last_page']+': '+ ipaddr_nonroot_val,font=('',14))
        non_root_device_config_lbl2=ctk.CTkLabel(master=main_frame,text=english_strings['ip_dg_last_page']+': '+ ipaddr_dg_nonroot_val,font=('',14))
        
        if selected_checkbox=='Bezprzewodowy punkt dostępowy' or selected_checkbox=='Wireless Access Point':
            non_root_device_config_lbl1_2=ctk.CTkLabel(master=main_frame,text=english_strings['ip3_last_page']+': '+ ipaddr2_nonroot_val,font=('',14))
            non_root_device_config_lbl1_2.place(relx=0.95,rely=0.72,anchor=tk.E)
        
        show_hide_last_page=ctk.CTkButton(master=main_frame, text=english_strings['last_page_passwords_show'], fg_color="#006633",height=20,width=40,
                                         command=lambda:[toggle_visibility_last_page()],corner_radius=0)
    
    if language_value=='polish':
        show_hide_last_page.place(relx=0.95,rely=0.32,anchor=tk.E)
        root_device_info_lbl1.place(relx=0.05,rely=0.37,anchor=tk.W)   
        root_device_info_lbl2.place(relx=0.05,rely=0.42,anchor=tk.W)
        root_device_info_lbl3.place(relx=0.05,rely=0.47,anchor=tk.W)
        root_device_info_lbl3_1.place(relx=0.12,rely=0.47,anchor=tk.W)
        root_device_info_lbl4.place(relx=0.05,rely=0.52,anchor=tk.W)
        root_device_info_lbl4_1.place(relx=0.2,rely=0.52,anchor=tk.W)
        
        root_device_config_lbl1.place(relx=0.95,rely=0.37,anchor=tk.E)
        root_device_config_lbl2.place(relx=0.95,rely=0.42,anchor=tk.E)
        root_device_config_lbl3.place(relx=0.7,rely=0.52,anchor=tk.E)
        root_device_config_lbl3_1.place(relx=0.95,rely=0.52,anchor=tk.E)
        
        non_root_values_lbl.place(relx=0.013,rely=0.57,anchor=tk.W)
        
        non_root_device_info_lbl1.place(relx=0.05,rely=0.62,anchor=tk.W)
        non_root_device_info_lbl2.place(relx=0.05,rely=0.67,anchor=tk.W)
        non_root_device_info_lbl3.place(relx=0.05,rely=0.72,anchor=tk.W)
        non_root_device_info_lbl3_1.place(relx=0.12,rely=0.72,anchor=tk.W)
        non_root_device_info_lbl4.place(relx=0.05,rely=0.77,anchor=tk.W)
        non_root_device_info_lbl4_1.place(relx=0.2,rely=0.77,anchor=tk.W)
        
        non_root_device_config_lbl1.place(relx=0.95,rely=0.62,anchor=tk.E)
        non_root_device_config_lbl2.place(relx=0.95,rely=0.67,anchor=tk.E)
        
        
        
        page6_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
        page6_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
        
        final_step_lbl.place(relx=0.5,rely=0.17,anchor=tk.CENTER)

        send_to_root_btn.place(relx=0.25,rely=0.85,anchor=tk.CENTER)
        
    else:
        show_hide_last_page.place(relx=0.95,rely=0.32,anchor=tk.E)
        root_device_info_lbl1.place(relx=0.05,rely=0.37,anchor=tk.W)   
        root_device_info_lbl2.place(relx=0.05,rely=0.42,anchor=tk.W)
        root_device_info_lbl3.place(relx=0.05,rely=0.47,anchor=tk.W)
        root_device_info_lbl3_1.place(relx=0.15,rely=0.47,anchor=tk.W)
        root_device_info_lbl4.place(relx=0.05,rely=0.52,anchor=tk.W)
        root_device_info_lbl4_1.place(relx=0.23,rely=0.52,anchor=tk.W)
        
        root_device_config_lbl1.place(relx=0.95,rely=0.37,anchor=tk.E)
        root_device_config_lbl2.place(relx=0.95,rely=0.42,anchor=tk.E)
        root_device_config_lbl3.place(relx=0.80,rely=0.47,anchor=tk.E)
        root_device_config_lbl3_1.place(relx=0.95,rely=0.47,anchor=tk.E)
        
        non_root_values_lbl.place(relx=0.013,rely=0.57,anchor=tk.W)
        
        non_root_device_info_lbl1.place(relx=0.05,rely=0.62,anchor=tk.W)
        non_root_device_info_lbl2.place(relx=0.05,rely=0.67,anchor=tk.W)
        non_root_device_info_lbl3.place(relx=0.05,rely=0.72,anchor=tk.W)
        non_root_device_info_lbl3_1.place(relx=0.15,rely=0.72,anchor=tk.W)
        non_root_device_info_lbl4.place(relx=0.05,rely=0.77,anchor=tk.W)
        non_root_device_info_lbl4_1.place(relx=0.23,rely=0.77,anchor=tk.W)
        
        non_root_device_config_lbl1.place(relx=0.95,rely=0.62,anchor=tk.E)
        non_root_device_config_lbl2.place(relx=0.95,rely=0.67,anchor=tk.E)
        
        
        
        page6_next_BTN.place(relx=0.90,rely=0.95,anchor=tk.CENTER)
        page6_back_BTN.place(relx=0.77,rely=0.95, anchor=tk.CENTER)
        
        final_step_lbl.place(relx=0.5,rely=0.18,anchor=tk.CENTER)

        send_to_root_btn.place(relx=0.25,rely=0.85,anchor=tk.CENTER)
        
#?__________________________________________________________________________________________________________________________________

def send_config_to_root():
    global root_device_info,root_config_commands,send_to_non_root_btn
    if language_value=="polish":
        send_to_non_root_btn.place(relx=0.75,rely=0.85,anchor=tk.CENTER)
    else:
        send_to_non_root_btn.place(relx=0.75,rely=0.85,anchor=tk.CENTER)
    send_window = ctk.CTkToplevel(master=main_frame)
    send_window.title("")
    send_window.geometry("500x100+780+500")
    send_window.resizable(False, False)
    send_window.after(300, lambda: send_window.iconbitmap("help.ico"))

    device=root_device_info
    config_commands=root_config_commands

    try:
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_config_set(config_commands)
        connection.disconnect()
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_lbl_str'],justify="center",wraplength=499,font=('',18))
    except netmiko.exceptions.NetmikoTimeoutException:
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_error_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_error_lbl_str'],justify="center",wraplength=499,font=('',18))
    except netmiko.exceptions.NetMikoAuthenticationException:
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_error_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_error_lbl_str'],justify="center",wraplength=499,font=('',18))
    except netmiko.exceptions:
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_error_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_error_lbl_str'],justify="center",wraplength=499,font=('',18))

    

    close_btn=ctk.CTkButton(master=send_window, command=lambda:[send_window.destroy(),send_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    help_lbl.pack(anchor="w",padx=5,pady=10)
    close_btn.pack()
    
    send_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def send_config_to_nonroot():
    global non_root_device_info,non_root_config_commands
    send_window = ctk.CTkToplevel(master=main_frame)
    send_window.title("")
    send_window.geometry("500x100+780+500")
    send_window.resizable(False, False)
    send_window.after(300, lambda: send_window.iconbitmap("help.ico"))

    device=non_root_device_info
    config_commands=non_root_config_commands

    try:
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_config_set(config_commands)
        connection.disconnect()
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send2_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send2_lbl_str'],justify="center",wraplength=499,font=('',18))
    except netmiko.exceptions.NetmikoTimeoutException:
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_error_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_error_lbl_str'],justify="center",wraplength=499,font=('',18))
    except netmiko.exceptions.NetMikoAuthenticationException:
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_error_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_error_lbl_str'],justify="center",wraplength=499,font=('',18))
    except netmiko.exceptions:
        if language_value=='polish':
            help_lbl = ctk.CTkLabel(master=send_window, text=polish_strings['send1_error_lbl_str'],justify="center", wraplength=499,font=('',18))
        elif language_value=='english':
            help_lbl = ctk.CTkLabel(master=send_window, text=english_strings['send1_error_lbl_str'],justify="center",wraplength=499,font=('',18))

    

    close_btn=ctk.CTkButton(master=send_window, command=lambda:[send_window.destroy(),send_window.update()],
                            text='OK', fg_color="#006633",width=40,height=20)
    
    help_lbl.pack(anchor="w",padx=5,pady=10)
    close_btn.pack()
    
    send_window.grab_set()

#?__________________________________________________________________________________________________________________________________

def page_7():
    delete_main_frame()
    if language_value=='polish':
        end_lbl=ctk.CTkLabel(master=main_frame,text=polish_strings['end_lbl'],justify="left", wraplength=649,font=('',24))
        close_btn=ctk.CTkButton(master=main_frame, command=lambda:[app.destroy()],
                            text=polish_strings['end'], fg_color="#006633",font=('',22))
    else:
        end_lbl=ctk.CTkLabel(master=main_frame,text=english_strings['end_lbl'],justify="left", wraplength=649,font=('',23))
        close_btn=ctk.CTkButton(master=main_frame, command=lambda:[app.destroy()],
                            text=english_strings['end'], fg_color="#006633",font=('',22))
    
    end_lbl.place(relx=0.01,rely=0.4,anchor=tk.W)
    
    close_btn.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
#?__________________________________________________________________________________________________________________________________    

select_language()



app.mainloop()

