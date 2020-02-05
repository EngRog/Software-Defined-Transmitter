#!/usr/bin/python

import Tkinter
import tkFont
import string
import sys

from Tkinter import *


meter_kwh=99999.99
required_number=0



#wfont = nametofont("TkDefaultFont")
#wfont = tkFont.nametofont
#
#font.config(weight='bold')


root = Tkinter.Tk()

#default_font = Tkinter.font.nametofont("TkDefaultFont")
#default_font = Tkinter.font
#default_font.configure(size=14)

root.title=("Load Pull Test")
root.geometry('400x400+200+200')


app=Tkinter.Frame(root)
app.grid()


text = Tkinter.Label(app, text= "Data Rate   ")
text.grid(row=1,column=1)
text = Tkinter.Label(app, text= "KHz   ")
text.grid(row=1,column=3)

text = Tkinter.Label(app, text= "Modulation  ")
text.grid(row=2,column=1)
text = Tkinter.Label(app, text= "Data Source  ")
text.grid(row=3,column=1)
text = Tkinter.Label(app, text= "Amplitude   ")
text.grid(row=4,column=1)
text = Tkinter.Label(app, text= "Phase   ")
text.grid(row=5,column=1)


data_rate = StringVar(app)
modulation_type = StringVar(app)
data_source = StringVar(app)
amplitude = StringVar(app)
phase = StringVar(app)

data_rate.set('16')
data_rate_txt = Tkinter.OptionMenu(app,data_rate,'1','2','4','8','16','32','64','128','256','512','1024','2048',
                                          '4096','8192','16384','32768','65536','131072','262144')
data_rate_txt.grid(row=1,column=2)

modulation_type.set('AM')
modulation_type_txt = Tkinter.OptionMenu(app,modulation_type,'AM','FM','PM','ASK','FSK','PSK','BPSK','QAM16','QAM64','QAM256')
modulation_type_txt.grid(row=2,column=2)

data_source.set('PseudoRandom')
data_source_txt = Tkinter.OptionMenu(app,data_source,'PseudoRandom','External','File')
data_source_txt.grid(row=3,column=2)

amplitude.set('0.5')
amplitude_txt = Tkinter.OptionMenu(app,amplitude,'0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0')
amplitude_txt.grid(row=4,column=2)

phase.set('0.0')
phase_txt = Tkinter.OptionMenu(app,phase,'0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9')
phase_txt.grid(row=5,column=2)

def start_tx():
    print("start")

def stop_tx():
    print("stop")

def pause_tx():
    print("pause")


start_but=Button(app,text="Start Tx",command=start_tx)
start_but.grid(row=6,column=1)
stop_but=Button(app,text="Stop Tx",command=stop_tx)
stop_but.grid(row=6,column=2)
pause_but=Button(app,text="Pause Tx",command=pause_tx)
pause_but.grid(row=6,column=3)

Label(app,text="SPI   ",font=('Comic Sans',12)).grid(row=7,column=1)

Label(app,text="Add",font=('Comic Sans',12)).grid(row=7,column=2)
address_box= Entry(app,width=10,textvariable=required_number,font=('Comic Sans',12))
address_box.grid(row=7,column=3)

Label(app,text="Data",font=('Comic Sans',12)).grid(row=8,column=2)
data_box= Entry(app,width=10,textvariable=meter_kwh,font=('Comic Sans',12))
data_box.grid(row=8,column=3)

start_but=Button(app,text="read SPI",command=start_tx)
start_but.grid(row=9,column=1)
stop_but=Button(app,text="Write SPI",command=stop_tx)
stop_but.grid(row=9,column=2)


root.mainloop()

