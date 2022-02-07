from tkinter import *
from tkinter.messagebox import *
import time
import os
def failist_sõnastikusse():
	tund_kirjeldus={}
	file=open("Tund.txt","r")
	for line in file:
		tund,kirjeldus=line.strip().split(":")
		tund_kirjeldus[tund.strip()]=kirjeldus.strip()
	file.close()
	return tund_kirjeldus

tund_kirjeldus=failist_sõnastikusse()
def kirjeldus_aknasse(t:str):
	if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
		alam_aken=Toplevel()
		lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
		alam_aken.geometry("400x400")
		c=Canvas(alam_aken,height=500,width=500)
		file=PhotoImage(file=t)
		c.create_image(10,10,image=file,anchor=NW)
		c.pack()
		alam_aken.mainloop()
	else:
		showinfo("Vastus","Kui ei taha,siis ei taha!")

j=0
tunniplaan=Tk()
tunniplaan.geometry("1000x600")
tunniplaan.title("Tunniplan")
tunniplaan.configure(bg="white")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(1,10,2):
     Ep=Label(tunniplaan,text=p[j],heigh=4,width=10,font="Arial 15",fg="black",bg="white",relief="ridge").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
     j+=1
kell=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
for i in range(11):
     tn=Label(tunniplaan,text=str(i)+"\n"+kell[i],heigh=4,width=10,font="Arial 8",fg="black",bg="white",relief="ridge").grid(row=0,column=i+1,sticky=N+S+W+E)


#Esmaspäev
t1=Button(tunniplaan, text ="Multimeedia",bg="#adc1ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("mult.png")).grid(row=1,column=2, columnspan=2, sticky=N+S+W+E)
t2=Button(tunniplaan, text ="Programmeerimise alused",bg="#ade1ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("code.png")).grid(row=2,column=2, columnspan=3, sticky=N+S+W+E)
t3=Button(tunniplaan, text ="Multimeedia",bg="#adc1ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("mult.png")).grid(row=2,column=5, columnspan=2, sticky=N+S+W+E)
t4=Button(tunniplaan, text ="Programmeerimise alused",bg="#ade1ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("code.png")).grid(row=1,column=5, columnspan=3, sticky=N+S+W+E)
t5=Button(tunniplaan, text ="Rühmaju \n hataja \n tund",bg="#ade1ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("class.png")).grid(row=1,column=8, rowspan=2, sticky=N+S+W+E)
#Teisipäev
t6=Button(tunniplaan, text = "Inglise keel", bg = "#fffff0", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("Eng.png")).grid(row = 3, column = 2, columnspan = 2, sticky = N+S+W+E)
t7=Button(tunniplaan, text = "Inglise keel", bg = "#e1adff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("eng2.png")).grid(row = 4, column = 2, columnspan = 2, sticky = N+S+W+E)
t8=Button(tunniplaan, text = "Operatsiooni \n süsteemide \n alused", bg = "#e181ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("OS.png")).grid(row = 3, column = 4, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
t9=Button(tunniplaan, text = "Kehaline kasvatus", bg = "#e181c1", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("fit.png")).grid(row = 3, column = 7, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
t10=Button(tunniplaan, text = "Eesti keel", bg = "#cdb5ff", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("Est.png")).grid(row = 3, column = 9, sticky = N+S+W+E)
t11=Button(tunniplaan, text = "Eesti keel", bg = "#cbb6c8",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("est2.png")).grid(row = 4, column = 9, sticky = N+S+W+E)
t12=Button(tunniplaan, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "#ffe7b4", font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("geo.png")).grid(row = 3, column = 10, rowspan = 2, sticky = N+S+W+E)
#Kolmapäev
t13=Button(tunniplaan, text = "Programmeerimise alused", bg = "#ade1ff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("code.png")).grid(row = 5, column = 2, columnspan = 3, sticky = N+S+W+E)
t14=Button(tunniplaan, text = "Multimeedia", bg = "#adc1ff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("mult.png")).grid(row = 6, column = 2, columnspan = 3, sticky = N+S+W+E)
t15=Button(tunniplaan, text = "Multimeedia", bg = "#adc1ff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("mult.png")).grid(row = 5, column = 6, columnspan = 3, sticky = N+S+W+E)
t16=Button(tunniplaan, text = "Programmeerimise alused", bg = "#ade1ff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("code.png")).grid(row = 6, column = 6, columnspan = 3, sticky = N+S+W+E)
t17=Button(tunniplaan, text = "Kunstiained", bg = "#e181cf",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("art.png")).grid(row = 5, column = 9, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
#Neljapäev
t18=Button(tunniplaan, text = "Andmebaasisüstee \n mide alused (eesti \n keeles)", bg = "#ff81a2",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("data.png")).grid(row = 7, column = 2, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
t19=Button(tunniplaan, text = "Andmebaasisüsteemide alused \n (eesti keeles)", bg = "#ff81a2",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("data.png")).grid(row = 7, column = 4, columnspan = 3, rowspan = 2, sticky = N+S+W+E)
t20=Button(tunniplaan, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "#ffe7b4",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("geo.png")).grid(row = 7, column = 7, rowspan = 2, sticky = N+S+W+E)
t21=Button(tunniplaan, text = "Eesti keel", bg = "#cdb5ff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("Est.png")).grid(row = 7, column = 8, sticky = N+S+W+E)
t22=Button(tunniplaan, text = "Eesti keel", bg = "#cbb6c8",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("est2.png")).grid(row = 8, column = 8, sticky = N+S+W+E)
#Reede
t23=Button(tunniplaan, text = "Keel ja kirjandus", bg = "#e1ff81",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("rus.png")).grid(row = 9, column = 3, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
t24=Button(tunniplaan, text = "Matemaatika", bg = "#fcbad2",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("math.png")).grid(row = 9, column = 6, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
t25=Button(tunniplaan, text = "Suhtlemine ja \n klienditeenindus", bg = "#c1adff",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("cust.png")).grid(row = 9, column = 8, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
t26=Button(tunniplaan, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "#ffe7b4",font="Arial 12",height=2,width=12,relief="ridge", command=lambda:kirjeldus_aknasse("geo.png")).grid(row = 9, column = 10, rowspan = 2, sticky = N+S+W+E)
#Blank panel 
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=1,column=1, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=3,column=1, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=5,column=1, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=7,column=1, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=9,column=1, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=1,column=9, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=1,column=10, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=1,column=11, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=3,column=11, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=5,column=11, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=7,column=11, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=9,column=11, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=7,column=9, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=7,column=10, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=9,column=1, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=9,column=2, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=9,column=5, rowspan=2, sticky=N+S+W+E)
Label(tunniplaan,text =" ",font="Arial 22",height=3,width=6, relief="ridge").grid(row=0,column=0, sticky=N+S+W+E)



tunniplaan.mainloop()