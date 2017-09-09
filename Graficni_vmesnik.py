from tkinter import *
import math

class Okno(Frame):
    def __init__(self, okno = None, height=580, width=800):
        Frame.__init__(self, okno)
        self.okno = okno
        self.platno = Canvas(self.okno, height = height,
                             width = width, bg = "white")
        self.platno.pack(fill = BOTH, expand = YES)
        self.narisi_bg()
        self.platno.bind('<Button-1>', self.klik_miske) #vsakič ko kliknemo levo tipko miške kličemo metodo klik miške
        self.odpri_okno()
        self.narisi_osi()
    #ustvarimo okvir kjer se vse dogaja
        
    def odpri_okno(self):
        self.okno.title("Trigonometrični pripomoček")
        self.pack(fill = BOTH, expand = YES)
        menu = Menu(self.okno)
        self.okno.config(menu = menu)
        file = Menu(menu)
        file.add_command(label = "Shrani", command = self.shrani)
        file.add_command(label = "Nadaljuj", command = self.nadaljuj)
        file.add_command(label = "Izhod", command = self.izhod)
        menu.add_cascade(label = "Datoteka", menu = file)
    #ustvarimo osnovni meni, ki ima možnosti shrani, nadaljuj in izhod
    def shrani(self):
        try:
            with open("shrani.txt", "w") as shrani:
                shrani.write("{0} {1}".format(self.x, self.y))  
        except (FileNotFoundError, AttributeError, ValueError):
            return
    #da lahko shranimo kar je trenutno na zaslonu, try in except dodana, če na začetku ni datoteke        

    def nadaljuj(self):
        try:
            with open("shrani.txt") as shrani:
                vsebina = shrani.read().split(" ")
                x = float(vsebina[0])
                y = float(vsebina[1])
                self.narisi_poltrak(x, y)
        except (FileNotFoundError, AttributeError, ValueError):
            return
    #da lahko pokličemo tisto kar smo nazadnje shranili, try in except dodana, če na začetku ni datoteke          

    def izhod(self):
        exit()
    #da lahko zapremo aplikacijo
        
    def narisi_bg(self):
        canvas = self.platno
        height = canvas["height"]
        width = canvas["width"]
        center = (int(width)/2, int(height)/2)
        canvas.create_oval(center[0]-100, center[1]-100,
                           center[0]+100, center[1]+100)
        self.poltrak = canvas.create_line(0,0,0,0)
        self.trikotnik1 = canvas.create_line(0,0,0,0)
        self.trikotnik2 = canvas.create_line(0,0,0,0)
    #metoda nariše ozadje, ter enotski krog

    def narisi_osi(self):
        canvas = self.platno
        height = canvas["height"]
        width = canvas["width"]
        center = (int(width)/2, int(height)/2)
        x1 = (center[0] - 1000,center[1])
        x2 = (center[0] + 1000,center[1])
        y1 = (center[0],center[1]- 1000)
        y2 = (center[0],center[1]+ 1000)
        self.osi1 = canvas.create_line(x1, x2)
        self.osi2 = canvas.create_line(y1, y2)
        self.okvir = canvas.create_rectangle(30,550,790,580,fill = "white")
        
        self.izpis_kota_v_rad = canvas.create_text(int(width)-680,int(height)-15,
                text = "Kot v radianih = ______ Rad")
        self.izpis_kota_v_deg = canvas.create_text(int(width)-520,int(height)-15,
                text = "Kot v stopinjah = ______\u00b0")
        self.izpis_sinusa = canvas.create_text(int(width)-380,int(height)-15,
                text = "Sinus kota = ____")
        self.izpis_kosinusa = canvas.create_text(int(width)-250,int(height)-15,
                text = "Kosinus kota = ____")
        self.izpis_tangensa = canvas.create_text(int(width)-100,int(height)-15,
                text = "Tangens kota = _____")
    #metoda ob zagonu programa nariše koordinatne osi, s centrom v sredini okvirja(ne okna!)

    def klik_miske(self, event):
        self.narisi_poltrak(event.x, event.y)
    #zaradi lažje oblike shranjevanja
        
    def narisi_poltrak(self, x, y):
        self.x = x
        self.y = y
        canvas = self.platno
        height = canvas["height"]
        width = canvas["width"]
        center = (int(width)/2, int(height)/2)
        fromCenter = (x-center[0], y-center[1]) #koordinate glede na središče okvirja
        dolzina = math.sqrt(fromCenter[0]**2 + fromCenter[1]**2) #razdalja od središča do mesta kjer kliknemo
        
        if dolzina < 1e-8:
            canvas.delete(self.poltrak, self.trikotnik1,self.trikotnik2,
                self.izpis_kota_v_rad, self.izpis_kota_v_deg, self.izpis_sinusa,
                self.izpis_kosinusa, self.izpis_tangensa)
            self.izpis_kota_v_rad = canvas.create_text(int(width)-680,int(height)-15,
                    text = "Kot v radianih = ______ Rad")
            self.izpis_kota_v_deg = canvas.create_text(int(width)-520,int(height)-15,
                    text = "Kot v stopinjah = ______\u00b0")
            self.izpis_sinusa = canvas.create_text(int(width)-380,int(height)-15,
                    text = "Sinus kota = ____")
            self.izpis_kosinusa = canvas.create_text(int(width)-250,int(height)-15,
                    text = "Kosinus kota = ____")
            self.izpis_tangensa = canvas.create_text(int(width)-100,int(height)-15,
                    text = "Tangens kota = _____")
            return
            #izjema, če kliknemo v center nam vrne stanje ob zagonu
        
        faktor = 1000/dolzina #da se poltrak ne dotika kroga, temveč sega čez(za lažjo nastavitev želenega kota)
        canvas.delete(self.poltrak, self.trikotnik1, self.trikotnik2, self.okvir,
                self.izpis_kota_v_rad, self.izpis_kota_v_deg, self.izpis_sinusa,
                self.izpis_kosinusa, self.izpis_tangensa)
        #pobrišemo vse podatke izpisane ob prejšnjem kliku, skupaj z izrisanim poltrakom in pravoktnim trikotnikom
        
        self.poltrak = canvas.create_line(center,
            center[0] + fromCenter[0]*faktor, center[1] + fromCenter[1]*faktor)
        self.trikotnik1 = canvas.create_line(center[0] + fromCenter[0]*faktor/10,
            center[1] + fromCenter[1]*faktor/10,center[0] + fromCenter[0]*faktor/10,
            center[1], fill = "red")
        self.trikotnik2 = canvas.create_line(center,
            center[0] + fromCenter[0]*faktor/10, center[1], fill = "green")
        #na novo narišemo poltrak in pravokotni trikotnik
        sinus_kota = math.sqrt((fromCenter[1]*faktor/10)**2)/100
        kosinus_kota = math.sqrt((fromCenter[0]*faktor/10)**2)/100 
            
        if x > center[0] and y <= center[1]:
            if y==center[1]:
                k1 = "0"
                k2 = "0"
                k3 = "0"
                k4 = "1"
                k5 = "0"
            else:
                x1 = math.asin(sinus_kota)
                k1 = format(x1, '.4f')
                k2 = format(math.degrees(x1), '.2f')
                k3 = format(sinus_kota, '.3f')
                k4 = format(kosinus_kota, '.3f')
                k5 = format(sinus_kota/kosinus_kota, '.3f')
                
        elif kosinus_kota < 1e-8 and y<center[1]:
            x2 = math.pi/2
            k1 = format(x2, '.4f')
            k2 = format(math.degrees(x2), '.2f')
            k3 = "1"
            k4 = "0"
            k5 = "'neskončno'"
               
        elif x < center[0] and y < center[1]:
            x3 = math.pi - math.acos(kosinus_kota) 
            k1 = format(x3, '.4f')
            k2 = format(math.degrees(x3), '.2f')
            k3 = format(sinus_kota, '.3f')
            k4 = format(- kosinus_kota, '.3f')
            k5 = format(- sinus_kota/kosinus_kota, '.3f')
           
        elif x < center[0] and y >= center[1]:
            x4 = math.asin(sinus_kota) + math.pi
            if y==center[1]:
                k1 = format(math.pi, '.4f')
                k2 = "180"
                k3 = "0"
                k4 = "- 1"
                k5 = "0"
            else:
                k1 = format(x4, '.4f')
                k2 = format(math.degrees(x4), '.2f')
                k3 = float("-" + (format(sinus_kota, '.3f')))
                k4 = format(- kosinus_kota, '.3f')
                k5 = format(sinus_kota/kosinus_kota, '.3f')
                  
        elif kosinus_kota < 1e-8 and y > center[1]:
            x5 = 3*(math.pi)/2
            k1 = format(x5, '.4f')
            k2 = format(math.degrees(x5), '.2f')
            k3 = "- 1"
            k4 = "0"
            k5 = "'- neskončno'"
            
        elif x > center[0] and y > center[1]:
            x6 = 2*math.pi - math.acos(kosinus_kota)
            k1 = format(x6, '.4f')
            k2 = format(math.degrees(x6), '.2f')
            k3 = format(- sinus_kota,'.3f')
            k4 = format(kosinus_kota,'.3f')
            k5 = format(- sinus_kota/kosinus_kota,'.3f')
        #definiramo katere vrednosti trigonometričnih funkcij nam izpisuje glede na to v katerem kvadrantu smo
    
        self.okvir = canvas.create_rectangle(30,550,790,580,fill = "white")
        self.izpis_kota_v_rad = canvas.create_text(int(width)-680,int(height)-15,
                                    text = "Kot v radianih = {} Rad".format(k1))
        self.izpis_kota_v_deg = canvas.create_text(int(width)-520,int(height)-15,
                                    text = "Kot v stopinjah = {} \u00b0".format(k2))
        self.izpis_sinusa = canvas.create_text(int(width)-380,int(height)-15,
                                    text = "Sinus kota = {}".format(k3),fill = "red")
        self.izpis_kosinusa = canvas.create_text(int(width)-250,int(height)-15,
                                    text = "Kosinus kota = {}".format(k4),fill = "green")
        self.izpis_tangensa = canvas.create_text(int(width)-100,int(height)-15,
                                    text = "Tangens kota = {}".format(k5))
        #kaj točno se izpisuje v pravokotnik ob vsakem kliku

paleta = Tk()
napis = Label(paleta, text = "Pritisni na zaslon!")
napis.pack()
paleta.geometry("840x640")

pogon=Okno(paleta)
paleta.mainloop()
