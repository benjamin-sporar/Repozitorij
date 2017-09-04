from tkinter import *
import math

#okno = Tk()
#gumb = Button(okno,text='Shrani')
#gumb.grid()
#platno = tk.Canvas(okno,height=550,width=550,bg="white")
#platno.grid()
#platno.create_oval(30,30,470,470)
#platno.create_line(250,10,240,20)
#platno.create_line(250,10,260,20)
#platno.create_line(490,250,480,240)
#platno.create_line(490,250,480,260)
#platno.create_line(250,10,250,490)
#platno.create_line(10,250,490,250)


class Okno(Frame):
    def __init__(self, okno = None, height=400, width=600):
        Frame.__init__(self, okno)
        self.okno = okno
        
        
        self.platno = Canvas(self.okno,height=height,width=width,bg="white")
        self.platno.pack(fill = BOTH, expand = YES)
        self.narisi_bg()
        self.platno.bind('<Button-1>', self.narisi_poltrak)
        self.odpri_okno()
        self.narisi_osi()

    def odpri_okno(self):
        self.okno.title("Grafični vmesnik")
        self.pack(fill=BOTH, expand=YES)

        
        menu = Menu(self.okno)
        self.okno.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Shrani",command=self.shrani)
        file.add_command(label="Nadaljuj",command=self.nadaljuj)
        file.add_command(label="Izhod",command=self.izhod)
        menu.add_cascade(label="Datoteka",menu=file)
        
        
    def izhod(self):
        exit()

    def shrani(self):
        return

    def nadaljuj(self):
        return

    def narisi_bg(self):
        canvas = self.platno
        height = canvas["height"]
        width = canvas["width"]

        center = (int(width)/2, int(height)/2)
        canvas.create_oval(center[0]-100,center[1]-100,center[0]+100,center[1]+100)

        self.poltrak = canvas.create_line(0,0,0,0)
        self.trikotnik1 = canvas.create_line(0,0,0,0)
        self.trikotnik2 = canvas.create_line(0,0,0,0)

    def narisi_osi(self):
        canvas = self.platno
        height = canvas["height"]
        width = canvas["width"]
        center = (int(width)/2, int(height)/2)
        x1 = (center[0] - 1000,center[1])
        x2 = (center[0] + 1000,center[1])
        y1 = (center[0],center[1]- 1000)
        y2 = (center[0],center[1]+ 1000)
        self.osi1 = canvas.create_line(x1,x2)
        self.osi2 = canvas.create_line(y1,y2)


    def narisi_poltrak(self, event):
        x = event.x
        y = event.y

        
        canvas = self.platno
        height = canvas["height"]
        width = canvas["width"]

        center = (int(width)/2, int(height)/2)
        fromCenter = (x-center[0], y-center[1])

        

        dolzina = math.sqrt(fromCenter[0]**2 + fromCenter[1]**2)
        if(dolzina < 1e-8):
            return
        faktor = 1000/dolzina
        faktor1 = 100/dolzina
        canvas.delete(self.poltrak)
        canvas.delete(self.trikotnik1)
        canvas.delete(self.trikotnik2)
        
        self.poltrak = canvas.create_line(center,
                                          center[0]+fromCenter[0]*faktor,
                                          center[1]+fromCenter[1]*faktor)
        
        self.trikotnik1 = canvas.create_line(center[0]+fromCenter[0]*faktor1,
                                            center[1]+fromCenter[1]*faktor1,
                                            center[0]+fromCenter[0]*faktor1,
                                            center[1], fill = "green")
        self.trikotnik2 = canvas.create_line(center,
                                             center[0]+fromCenter[0]*faktor1,
                                             center[1],
                                             fill = "red")

        sinus_kota = math.sqrt((fromCenter[1]*faktor1)**2)/100
        kosinus_kota = math.sqrt((fromCenter[0]*faktor1)**2)/100

        if (kosinus_kota < 1e-8)and y<center[1]:
            print("Sinus kota = {0}".format(format(sinus_kota,'.4f')))
            print("Kosinus kota = {0}".format("0"))
            print("Tangens kota = {0}".format("neskončno"))
        elif (kosinus_kota < 1e-8)and y>center[1]:
            print("Sinus kota = {0}".format(format(sinus_kota,'.4f')))
            print("Kosinus kota = {0}".format("0"))
            print("Tangens kota = {0}".format('-neskončno'))
        else:
            print("Sinus kota = {0}".format(format(sinus_kota,'.4f')))
            print("Kosinus kota = {0}".format(format(kosinus_kota,'.4f')))
            print("Tangens kota = {0}".format(format(sinus_kota/kosinus_kota,'.4f')))


        if x == center[0] and y > center[1]:
            x1 = (3*(math.pi)/2)
            x1a = (3*(math.pi)/2*180/math.pi)
            print("Kot v radianih = {0}".format(format(x1, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x1a, '.2f')))
        elif (kosinus_kota < 1e-8)and y<center[1]:
            x2 = ((math.pi)/2)
            x2a = ((math.pi)/2*180/math.pi)
            print("Kot v radianih = {0}".format(format(x2, '.4')))
            print("Kot v stopinjah = {0}".format(format(x2a, '.2f')))
        elif x > center[0] and y < center[1]:
            x3 = (math.atan(sinus_kota/kosinus_kota))
            x3a = (math.atan(sinus_kota/kosinus_kota)*180/math.pi)
            print("Kot v radianih = {0}".format(format(x3, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x3a, '.2f')))
        elif x < center[0] and y < center[1]:
            x4 = ((math.atan(kosinus_kota/sinus_kota) + (math.pi)/2))
            x4a = ((math.atan(kosinus_kota/sinus_kota) + (math.pi)/2)*180/math.pi)
            print("Kot v radianih = {0}".format(format(x4, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x4a, '.2f')))
        elif x > center[0] and y > center[1]:
            x5 = ((math.atan(kosinus_kota/sinus_kota) + 3*(math.pi)/2))
            x5a = ((math.atan(kosinus_kota/sinus_kota) + 3*(math.pi)/2)*180/math.pi)
            print("Kot v radianih = {0}".format(format(x5, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x5a, '.2f')))
        elif x >= center[0] and y == center[1]:
            x6 = (0)
            x6a = (0)
            print("Kot v radianih = {0}".format(format(x6, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x6a, '.2f')))
        elif x < center[0] and y == center[1]:
            x7 = (math.pi)
            x7a = (180)
            print("Kot v radianih = {0}".format(format(x7, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x7a, '.2f')))
        else:
            x8 = ((math.atan(sinus_kota/kosinus_kota)+math.pi))
            x8a = ((math.atan(sinus_kota/kosinus_kota)+math.pi)*180/math.pi)
            print("Kot v radianih = {0}".format(format(x8, '.4f')))
            print("Kot v stopinjah = {0}".format(format(x8a, '.2f')))




paleta = Tk()
paleta.geometry("640x480")


pogon=Okno(paleta)
paleta.mainloop()
