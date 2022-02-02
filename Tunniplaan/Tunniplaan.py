from tkinter import*

tunniplaan=Tk()
tunniplaan.title("Akna nimetus")
tunniplaan.geometry("1080x1024")
Ep=Label(tunniplaan,text ="Esmaspäev",font="Arial 22",height=4,width=10, relief="ridge").grid(row=1,column=0, rowspan=2, sticky=N+S+W+E)
Tp=Label(tunniplaan,text ="Teisepäev",font="Arial 22",height=4,width=10, relief="ridge").grid(row=3,column=0, rowspan=2, sticky=N+S+W+E)
Kp=Label(tunniplaan,text ="Kolmapäev",font="Arial 22",height=4,width=10, relief="ridge").grid(row=5,column=0, rowspan=2, sticky=N+S+W+E)
Np=Label(tunniplaan,text ="Neljapäev",font="Arial 22",height=4,width=10, relief="ridge").grid(row=7,column=0, rowspan=2, sticky=N+S+W+E)
Rp=Label(tunniplaan,text ="Reede",font="Arial 22",height=4,width=10, relief="ridge").grid(row=9,column=0, rowspan=2, sticky=N+S+W+E)

t0=Label(tunniplaan,text ="0",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=1, sticky=N+S+W+E)
t1=Label(tunniplaan,text ="1",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=2, sticky=N+S+W+E)
t2=Label(tunniplaan,text ="2",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=3, sticky=N+S+W+E)
t3=Label(tunniplaan,text ="3",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=4, sticky=N+S+W+E)
t4=Label(tunniplaan,text ="4",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=5, sticky=N+S+W+E)
t5=Label(tunniplaan,text ="5",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=6, sticky=N+S+W+E)
t6=Label(tunniplaan,text ="6",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=7, sticky=N+S+W+E)
t7=Label(tunniplaan,text ="7",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=8, sticky=N+S+W+E)
t9=Label(tunniplaan,text ="8",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=9, sticky=N+S+W+E)
t10=Label(tunniplaan,text ="9",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=10, sticky=N+S+W+E)
t11=Label(tunniplaan,text ="10",font="Arial 18",height=3,width=6, relief="ridge").grid(row=0,column=11, sticky=N+S+W+E)

#Esmaspäev
Button(tunniplaan, text ="Multimeedia",bg="blue", font="Arial 12",height=2,width=12,relief="ridge").grid(row=1,column=2, columnspan=2, sticky=N+S+W+E)
Button(tunniplaan, text ="Programmeerimise alused",bg="lightblue", font="Arial 12",height=2,width=12,relief="ridge").grid(row=2,column=2, columnspan=3, sticky=N+S+W+E)
Button(tunniplaan, text ="Multimeedia",bg="blue", font="Arial 12",height=2,width=12,relief="ridge").grid(row=2,column=5, columnspan=2, sticky=N+S+W+E)
Button(tunniplaan, text ="Programmeerimise alused",bg="lightblue", font="Arial 12",height=2,width=12,relief="ridge").grid(row=1,column=5, columnspan=3, sticky=N+S+W+E)
Button(tunniplaan, text ="Rühmaju \n hataja \n tund",bg="lightblue", font="Arial 12",height=2,width=12,relief="ridge").grid(row=1,column=8, rowspan=2, sticky=N+S+W+E)

tunniplaan.mainloop()