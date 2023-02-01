import tkinter as tk
from tkinter import *
from subprocess import Popen
import cv2
from tkinter import messagebox
from subprocess import Popen, PIPE
import time
from tkVideoPlayer import TkinterVideo
import asyncio
import threading
# from Face_Detect2 import *
# # from threading import Thread
# import concurrent.futures
# from concurrent.futures import ProcessPoolExecutor

# import amınaKODUM as amk / enner valencia

import pandas as pd
import asynctkinter as at
# import tracemalloc
# tracemalloc.start()



Filepath="C:/Users/pc/vs_code/Z16_Face_Detect_2/Face_Detect2.py"
StartButtonPath="C:/Users/pc/vs_code/Z16_Face_Detect_2/start5.png"
StopButtonPath="C:/Users/pc/vs_code/Z16_Face_Detect_2/stop_5.png"
ErrorCode_1="Proje Başlatma Öncelik Hatası"

PastelMavi="#82AAE3"
KoyuMavi="#144272"
TozPembe="#947EC3"
KahveRengi="#AA8B56"
KapaliMavi="#5F7161"  # /#3C6255 /22A39F/439A97/5F8D4E/5F7161




process=False

root = tk.Tk()
root.title("YoloV5 Kullanım Arayüzü")
root.geometry("900x800")
root.config(bg=KapaliMavi)

output_widget = tk.Text(root)
output_widget.config(width=78,height=11,bg=KoyuMavi,fg="white",font="Calibri 13")
output_widget.place(x=25,y=450)


# async def run_script():
#     process = await asyncio.create_subprocess_exec(
#         "python", Filepath, stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)

#     stdout, stderr = await process.communicate()
#     output_widget.config(state='normal')
#     output_widget.insert('end', stdout.decode('utf-8'))
#     output_widget.config(state='disabled')
    


# def baslat():
#     asyncio.run(run_script())




def run_script():

        global process
        process=True
        process = Popen(["python", Filepath], stdout=PIPE, stderr=PIPE)

        output, errors =   process.communicate()
        output_widget.config(state='normal')
        output_widget.insert('end', output.decode('latin-1').encode('utf-16').decode('utf-16'))
        output_widget.config(state='disabled')
        HizAyari = output.decode().split("\n")
        
        for line in HizAyari:
            print(line)
            time.sleep(0.005)   #time.sleep(0.0001)

# videoplayer=TkinterVideo(master=root,scaled=True)
# videoplayer.load(process)
# videoplayer.pack(expand=True)
# videoplayer.play()












start_btn=PhotoImage(file=StartButtonPath)
img_label=Label(image=start_btn)

start = tk.Button(  root,
                    image=start_btn,
                    text="Face Detect  AÇ",
                    activebackground="red",
                    activeforeground="black",
                    command=run_script,
                    borderwidth=0
                    )
start.place(x=25,y=200)





def stop_script():
    if not process:
                    message_box=messagebox.showinfo(ErrorCode_1,"Stop fonksiyonu, start fonksiyonu başlamadan çağrılamaz")
                    print(message_box)
    else:
                    process.kill()


stop_btn=PhotoImage(file=StopButtonPath)
img_label2=Label(image=stop_btn)





stop = tk.Button( 
                  root,
                  text="Face Detect  KAPA ",
                  activebackground="red",
                  image=stop_btn,
                  activeforeground="black",
                  command=stop_script,
                  borderwidth=0
                )
stop.place(x=25,y=300)



IkonPhoto=PhotoImage(file="C:/Users/pc/vs_code/Z16_Face_Detect_2/resim3.png")
root.iconphoto(False,IkonPhoto)



BilgilendirmeLabel=tk.Label(
                    root,
                    text="Yolo ile geliştirdiğimiz Uygulamaların butonla çağrılıp başlatılma örneği 1",
                    font="Calibri 16",
                    fg="black",
                    bg=KahveRengi,
                    wraplength=475
                    )
BilgilendirmeLabel.place(x=25,y=100)


LogoLabelFoto=PhotoImage(file="C:/Users/pc/vs_code/Z16_Face_Detect_2/resim4.png")
LogoLabel=tk.Label(
                    root,
                    image=LogoLabelFoto,
                    wraplength=200,
                    bg="#FFFFFF",
                    borderwidth=0
                ) 
LogoLabel.place(x=300,y=200)
            



ConsoleOutput="key point coordinate information"
ConsoleLabel=tk.Label(
                    root,
                    text=ConsoleOutput,
                    font="Calibri 16",
                    fg="white",
                    bg=KahveRengi,
                    width=64,
                    wraplength=350
                    )
ConsoleLabel.place(x=25,y=418)


#videolabel



root.mainloop()

