# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:58:02 2021

@author: Lenovo
"""


import tkinter as tk
from PIL import ImageTk,Image
import pygame as py 
import random as rd
import numpy as np
from math import pi,sqrt,exp

#Initialisation des variables
     #initialisation des sons
py.mixer.init()
soundRebondRaquette=py.mixer.Sound('SoundPackage/Sound/reboundJoueur.wav')
soundRebondWallH=py.mixer.Sound('SoundPackage/Sound/reboundWallH.wav') 
soundRebondRaquetteIA=py.mixer.Sound('SoundPackage/Sound/reboundIA.wav')
soundRebondVsWall=py.mixer.Sound('SoundPackage/Sound/reboundVsWall.wav')
gameOverSound=py.mixer.Sound('SoundPackage/Sound/losing.wav')
winSound=py.mixer.Sound('SoundPackage/Sound/win.mp3')
winSoundAlternate=py.mixer.Sound('SoundPackage/Sound/winA.mp3')
plusOne=py.mixer.Sound('SoundPackage/Sound/plusOne.wav')
minusOne=py.mixer.Sound('SoundPackage/Sound/minusOne.wav')

Startingsound=py.mixer.Sound('SoundPackage/Music/generique.wav')
MusicMenu=py.mixer.Sound('SoundPackage/Music/Menu.mp3')
MusicIA=py.mixer.Sound('SoundPackage/Music/VsIA.mp3')
Music2J=py.mixer.Sound('SoundPackage/Music/2joueurs.mp3')
MusicWall=py.mixer.Sound('SoundPackage/Music/VsWall.mp3')

    #fenetre
haut_fenetre=500;
larg_fenetre=500;

#ZoneDetection et  parametres IA
ZoneDetection = 0.9
mu = 0.4
sigma = 0.1
epsilon = 0.15
cap = 0.95

    #position initiale de la balle
PosXball=haut_fenetre/2
PosYball=larg_fenetre/2
    #position raquette 1 et 2
PosXj1=10
PosYj1=haut_fenetre/2
PosXj2= larg_fenetre-20
PosYj2= haut_fenetre/2
    #vitesse de la balle
dx=8
dy=10

dxMenu= 10
dyMenu= 14
     #position initiale de la balle
PosXballmenu=haut_fenetre/4
PosYballmenu=larg_fenetre/2
    #init des scores
scorej1=0
scorej2=0
    #init de la liste de couleurs
tabColor=np.array(['blue','red','green','yellow','pink','purple','orange','grey'])
    #var introduction
introduction=True
apparition=True
vR,vG,vB = 0,0,0


# ---------------------------------------------------------------------------------------------------------
def game_2players():
    MusicMenu.stop()
   #reinitialisation des variables
    PosXball=haut_fenetre/2
    PosYball=larg_fenetre/2
        #position raquette 1 et 2
    PosXj1=10
    PosYj1=haut_fenetre/2
    PosXj2= larg_fenetre-20
    PosYj2= haut_fenetre/2
    #vitesse de la balle
    #init de la fennetre de jeux.
    Pong = tk.Tk()
    Pong.tittle=("Jeu de Pong 2 joueurs")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = 500, height = 500 , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    raquetteJ2 = canvas.create_rectangle(PosXj2,PosYj2,PosXj2+10,PosYj2+100,fill='red')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1)+" - "+str(scorej2))
    
    Music2J.play()
    
    def anglej1():
       global PosXball, PosYball, dx ,dy, PosYj1
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+20 :
           #modif angle
           dx=dx+5
           dy=dy-6
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+20 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+40 :
           #modif angle
           dy=dy-4
           #print("2")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+40 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+60 :
           #modif vitesse
           #print("3")
           if dx>=10:
               dx=dx-5
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+60 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+80 :
           #modif angle
           dy=dy+4
           #print("4")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+80 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           #modif angle
           dx=dx+5
           dy=dy+6
           #print("5")
        
    def anglej2():
       global PosXball, PosYball, dx ,dy, PosYj2
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1] and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+20 :
           #modif angle
           dx=dx-5
           dy=dy-6
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+20 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+40 :
           #modif angle
           dy=dy-4
           #print("2")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+40 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+60 :
           #modif vitesse
           #print("3")
           if dx>=-10:
               dx=dx+5
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+60 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+80 :
           #modif angle
           dy=dy+4
           #print("4")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+80 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[3] :
           #modif angle
           dx=dx-5
           dy=dy+6
           #print("5")
     
    #mapping clavier pour le mouvement des raquettes
    def mouvement(event):
        global PosYj1,PosYj2
        Key = event.keysym
     
        def hautj1():
             if canvas.coords(raquetteJ1)[1]>=10:
                 canvas.move(raquetteJ1,0,-20)
                 #print(canvas.coords(raquetteJ1))
        def basj1():
             if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre:
                 canvas.move(raquetteJ1,0,20)
                 #print(canvas.coords(raquetteJ1))
        def hautj2():
             if canvas.coords(raquetteJ2)[1]>=10:
                canvas.move(raquetteJ2,0,-20)
                #print(canvas.coords(raquetteJ2))
        def basj2():
             if canvas.coords(raquetteJ2)[1]+100<=haut_fenetre:
                canvas.move(raquetteJ2,0,20)
                #print(canvas.coords(raquetteJ2))
                
        if Key == 'z':
             hautj1()
        if Key == 's':
             basj1()
        if Key == 'p':
            hautj2()
        if Key == 'm':
            basj2()
            
    
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if PosYball < 0 or PosYball > 465:
            dy=-dy
            soundRebondWallH.play()
            
        if canvas.coords(balle)[0] >= 480 and canvas.coords(raquetteJ2)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ2)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            anglej2()
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            anglej1()
            
        if PosXball<0 :
            minusOne.play()
            #reset position
            PosXball=haut_fenetre/2
            PosYball=larg_fenetre/2
            dx=-8
            dy=10
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            
            #MAJ du score
            scorej2+=1
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
        if PosXball > larg_fenetre:
            #reset position
            minusOne.play()
            PosXball=haut_fenetre/2
            PosYball=larg_fenetre/2
            dx=8
            dy=10
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            
            #MAJ du score
            scorej1+=1
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
            
        
        if scorej1>=5 or scorej2>=5:
            gameOverScreen()
            
                
        if not py.mixer.get_busy():
            Music2J.play()
    
        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        global scorej1,scorej2
        #efface les objets
        canvas.delete(balle)
        canvas.delete(raquetteJ1)
        canvas.delete(raquetteJ2)
        canvas.delete(score)
        Music2J.stop()
        if abs(scorej1-scorej2) < 5:
            winSound.play()
        if abs(scorej1-scorej2) >= 5:
            winSoundAlternate.play()
        #ecran de game over
        if scorej1>=5:
            canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="blue",font="Times 40 bold",text="Victoire J1 : "+ str(scorej1)+" - "+str(scorej2))
            canvas.after(3000,Pong.destroy)
            canvas.after(2999,creatMenu)
        if scorej2>=5:
            canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="red",font="Times 40 bold",text="Victoire J2 : "+ str(scorej2)+" - "+str(scorej1))    
            canvas.after(3000,Pong.destroy)
            canvas.after(2999,creatMenu)
    
    
    canvas.focus_set()#on met le focus sur le canvas
    Pong.focus_force()
    #on dit au canvas de prendre en compte les actions de mouvement(event)
    #on ne doit pas laisser les touches enfonce
    canvas.bind('<Key>',mouvement) 
    
    mouvball()
    Pong.mainloop()


# -------------------------------------------------------------------------------------------------------------
def game_vsIA():
    global menu

    MusicMenu.stop()
    #init de la fennetre de jeux.
    Pong = tk.Tk()
    Pong.tittle=("Jeu de Pong Vs IA")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = 500, height = 500 , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    raquetteIA = canvas.create_rectangle(PosXj2,PosYj2,PosXj2+10,PosYj2+100,fill='red')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1)+" - "+str(scorej2))
    
    MusicIA.play()
    
    def IA():       
    
        #deplacement dans la zone
       
        global larg_fenetre
        if canvas.coords(balle)[2] > larg_fenetre*ZoneDetection:
            if canvas.coords(balle)[3]-10 < canvas.coords(raquetteIA)[1]+50:
                if canvas.coords(raquetteIA)[1]>=10:
                    canvas.move(raquetteIA,0,-20)
                       
            if canvas.coords(balle)[3]-10 > canvas.coords(raquetteIA)[1]+50:
                if canvas.coords(raquetteIA)[1]+100<=haut_fenetre:
                    canvas.move(raquetteIA,0,20)
                    
        
       
        #print(zoneBall)
     
        
    def angle():
       global PosXball, PosYball, dx ,dy, PosYj1
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+20 :
           #modif angle
           dx=dx+5
           dy=dy-6
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+20 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+40 :
           #modif angle
           dy=dy-4
           #print("2")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+40 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+60 :
           #modif vitesse
           #print("3")
           if dx>=10:
               dx=dx-5
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+60 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+80 :
           #modif angle
           dy=dy+4
           #print("4")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+80 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           #modif angle
           dx=dx+5
           dy=dy+6
           #print("5")
        
     
    #mapping clavier pour le mouvement des raquettes
    def mouvement(event):
        global PosYj1
        Key = event.keysym
     
        def hautj1():
            if canvas.coords(raquetteJ1)[1]>=10:
                canvas.move(raquetteJ1,0,-20)
                #print(canvas.coords(raquetteJ1))
        def basj1():
            if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre:
                canvas.move(raquetteJ1,0,20)
                #print(canvas.coords(raquetteJ1))
        if Key == 'z':
            hautj1()
        if Key == 's':
            basj1()
                #print(canvas.coords(raquetteJ1))
       
            
    def loi_normale_x_spot(x,mu,sigma):
        return round((1/(sigma*sqrt(2*pi))) * exp(((-1)/2)*((x-mu)/sigma)*((x-mu)/sigma)),5)
    
    def valeur_normale(mu,sigma,epsilon,cap):
        #valeur finale
        x, y = rd.random(), rd.random()# variables random
        var = abs(x-y)
        print("var="+str(var))
        
        n = 2000
        x1, dx = 0, var/n # current position and increment
        integral = 0
    
        for i in range(n):
            integral += (loi_normale_x_spot(x1,mu,sigma) + loi_normale_x_spot(x1+dx,mu,sigma))*0.5*dx # integration par la methode des trapezes
            # maj des variables
            x1 += dx
        
        res = min(round(integral,2)+epsilon,cap)
        return res

    def ZoneDetectionUpdate():
            return valeur_normale(sigma,mu,epsilon,cap)
        
        
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2,ZoneDetection
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if PosYball < 0 or PosYball > 465:
            dy=-dy
            soundRebondWallH.play()
            
        if canvas.coords(balle)[0] >= 480 and canvas.coords(raquetteIA)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteIA)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            #update de la zone de detection
            ZoneDetection = ZoneDetectionUpdate()
            soundRebondRaquetteIA.play()
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            angle()
            
        if PosXball<0 :
            minusOne.play()
            #reset position
            PosXball=haut_fenetre/2
            PosYball=larg_fenetre/2
            dx=8
            dy=10
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            
            
            #MAJ du score
            scorej2+=1
            soundRebondRaquette.play()
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
        if PosXball > larg_fenetre:
            plusOne.play()
            #reset position
            PosXball=haut_fenetre/2
            PosYball=larg_fenetre/2
            dx=-8
            dy=10
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            
            #MAJ du score
            scorej1+=1
            soundRebondRaquette.play()
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
            
        
        if scorej1>=5 or scorej2>=5:
            gameOverScreen()
         
            
        if not py.mixer.get_busy():
           MusicIA.play()    
            
        canvas.after(20,IA)
        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        #efface les objets
        canvas.delete(balle)
        canvas.delete(raquetteJ1)
        canvas.delete(raquetteIA)
        canvas.delete(score)
        MusicIA.stop()
        
        
        #ecran de game over
        if scorej1>=5:
            winSound.play()
            canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="blue",font="Times 40 bold",text="Victoire J1 : "+ str(scorej1)+" - "+str(scorej2))
            canvas.after(3000,Pong.destroy)
            canvas.after(2999,creatMenu)
        if scorej2>=5:
            gameOverSound.play()
            canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="red",font="Times 40 bold",text="Victoire IA : "+ str(scorej2)+" - "+str(scorej1))    
            canvas.after(3000,Pong.destroy)
            canvas.after(2999,creatMenu)
    
    
    canvas.focus_set()#on met le focus sur le canvas
    Pong.focus_force()
    #on dit au canvas de prendre en compte les actions de mouvement(event)
    #on ne doit pas laisser les touches enfonce
    canvas.bind('<Key>',mouvement) 
    
    mouvball()
    Pong.mainloop()
   
  
# -------------------------------------------------------------------------------------------------------------

    
def game_vsWall():
    MusicMenu.stop()
        #position balle
    PosXball=haut_fenetre/2
    PosYball=larg_fenetre/2
        #position raquette 1 et 2
    PosXj1=10
    PosYj1=haut_fenetre/2

    
       #init de la fennetre de jeux.
    Pong = tk.Tk()
    Pong.tittle=("Jeu de Pong")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = 500, height = 500 , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1))
    
    MusicWall.play()
     
    #mapping clavier pour le mouvement des raquettes
    def mouvement(event):
        global PosYj1
        Key = event.keysym
        def hautj1():
            if canvas.coords(raquetteJ1)[1]>=10:
                canvas.move(raquetteJ1,0,-20)
                #print(canvas.coords(raquetteJ1))
        def basj1():
            if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre:
                canvas.move(raquetteJ1,0,20)
                #print(canvas.coords(raquetteJ1))
        if Key == 'z':
            hautj1()
        if Key == 's':
            basj1()
            
    
    def angle():
        global PosXball, PosYball, dx ,dy, PosYj1
        #detection frappe de la balle entre 5zones de la raquette
        if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+20 :
            #modif angle
            dx=dx+5
            dy=dy-6
            #print("1")
        if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+20 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+40 :
            #modif angle
            dy=dy-4
            #print("2")
        if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+40 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+60 :
            #modif vitesse
            #print("3")
            if dx>=10:
                dx=dx-5
                #print("-actif")
        if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+60 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+80 :
            #modif angle
            dy=dy+4
            #print("4")
        if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+80 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
            #modif angle
            dx=dx+5
            dy=dy+6
            #print("5")
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2,soundRebondRaquette
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if PosYball < 0 or PosYball > 465:
            dy=-dy
            soundRebondWallH.play()
            
        if PosXball> larg_fenetre:
            dx = -dx
            soundRebondVsWall.play()
            
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            angle()
            #MAJ du score
            scorej1+=1
            canvas.itemconfig(score,text= str(scorej1))
            
            
        if PosXball<0 :
            minusOne.play()
            #reset position
            PosXball=haut_fenetre/2
            PosYball=larg_fenetre/2
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            gameOverScreen()
       
        if not py.mixer.get_busy():
            MusicWall.play()
        
        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        global scorej1,dx,dy,gameOverSound
        #efface les objets
        canvas.delete(balle)
        canvas.delete(raquetteJ1)
        canvas.delete(score)
        MusicWall.stop()
      
        gameOverSound.play()
       
            
        
        #ecran de game over
        canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="green",font="Times 40 bold",text="Score : "+ str(scorej1))
        scorej1=0
        dx=8
        dy=10
        canvas.after(3000,Pong.destroy)
        canvas.after(2999,creatMenu)
    
        
        
        
        
        
    canvas.focus_set()#on met le focus sur le canvas
    Pong.focus_force()
    #on dit au canvas de prendre en compte les actions de mouvement(event)
    #on ne doit pas laisser les touches enfonce
    canvas.bind('<Key>',mouvement) 
    
    mouvball()
    Pong.mainloop()

# -------------------------------------------------------------------------------------------------------------

def creatMenu():
    
    global Startingsound
    
    
    #init de la fennetre du menu.
    menu = tk.Tk()
    menu.title("[Pong]")
    menu.geometry("500x500")
    
    #Création du canvas + ajout a la fen
    MenuCanvas = tk.Canvas(menu,width = 500, height = 500 , bd=0, bg="black")
    MenuCanvas.pack(padx=10,pady=10)
    
   
    
    image = Image.open("Images/images.png")
    image = image.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    
    def animIntro():
       global introduction,apparition,vR,vG,vB
       
       
       
       def destroyIntro():
           MenuCanvas.delete(title)
           #MenuCanvas.delete(logo)
          
           
       def apparitionTxt():
            global vR,vB,vG
            vR=vR+17
            vG=vG+17
            vB=vB+17
            mycolor = '#%02x%02x%02x' % (vR,vG,vB)
            MenuCanvas.itemconfig(title,fill=mycolor)
            if vR<255:
                MenuCanvas.after(200,apparitionTxt)
           
       if introduction:
           Startingsound.play()
           title=MenuCanvas.create_text(larg_fenetre/2,haut_fenetre/2-20,fill="black",font="Times 25 bold",text="Prheidator studio")
           apparitionTxt()
           introduction=False
           MenuCanvas.after(3000,destroyIntro)
           MenuCanvas.after(3500,creatMenuPrincipal)
       else:
           MenuCanvas.after(100,creatMenuPrincipal)
           
        
        
    def creatMenuPrincipal():
        global PosXball,PosYball,balleMenu,raquetteMenu
        #création des elements du jeux
        MenuCanvas.create_image(larg_fenetre*3/4,0, anchor = tk.NW, image=photo)
        balleMenu= MenuCanvas.create_oval(PosXballmenu,PosYballmenu,PosXballmenu+20,PosYballmenu+20,fill='white') #balle de rayon 20
        MenuCanvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text="PONG")
        MenuCanvas.create_text(larg_fenetre/2+50,75,fill="white",font="Times 8 bold",text="by Prheidator")
        raquetteMenu=MenuCanvas.create_rectangle(10,haut_fenetre/4,20,haut_fenetre/4+250,fill='white')
        
        
        entre1=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4,larg_fenetre/2+210,haut_fenetre/4+50,outline='white')
        entre2=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+70,larg_fenetre/2+210,haut_fenetre/4+120,outline='white')
        entre3=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+140,larg_fenetre/2+210,haut_fenetre/4+190,outline='white')
        entre4=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+210,larg_fenetre/2+210,haut_fenetre/4+260,outline='white')
        
        entre1Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+25,fill="white",font="Times 20 bold",text="2 joueurs")
        entre2Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+95,fill="white",font="Times 20 bold",text="vs IA")
        entre3Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+165,fill="white",font="Times 20 bold",text="vs Wall")
        entre4Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+235,fill="white",font="Times 20 bold",text="Exit")
        
        MenuCanvas.create_text(larg_fenetre-50,haut_fenetre-50,fill="white",font="Times 8 bold",text="Beta 1.4")
        
        MusicMenu.play()
        
        
        def animation():
            global PosXballmenu, PosYballmenu,haut_fenetre,larg_fenetre,soundRebondRaquette,dxMenu,dyMenu,tabC
            
            #calcul mouvement balle
            PosXballmenu = PosXballmenu + dxMenu
            PosYballmenu = PosYballmenu + dyMenu
            MenuCanvas.coords(balleMenu,PosXballmenu,PosYballmenu,PosXballmenu+10,PosYballmenu+10)
            
           
            if PosYballmenu <= 0 or PosYballmenu >= haut_fenetre-40:
                dyMenu=-dyMenu
                soundRebondWallH.play()
                MenuCanvas.itemconfig(balleMenu,fill=tabColor[rd.randint(0, 7)])
            if PosXballmenu >= larg_fenetre-30:
                dxMenu=-dxMenu
                soundRebondWallH.play()
                MenuCanvas.itemconfig(balleMenu,fill=tabColor[rd.randint(0, 7)])
                
            if MenuCanvas.coords(balleMenu)[0] <= 20 and MenuCanvas.coords(raquetteMenu)[1] <= MenuCanvas.coords(balleMenu)[1] <= MenuCanvas.coords(raquetteMenu)[3]:#ici la balle ne rebondit pas sur la raquette
                dxMenu = -dxMenu
                soundRebondRaquette.play()
                MenuCanvas.itemconfig(balleMenu,fill='white')
            if PosXballmenu<0 :
                dxMenu=-dxMenu
                MenuCanvas.itemconfig(balleMenu,fill=tabColor[rd.randint(0, 7)])
            
                
            if not py.mixer.get_busy():
                MusicMenu.play()
            
            MenuCanvas.after(50,animation)
            
        def onCanvasClick1(event):
            global scorej1,scorej2
            scorej1,scorej2 = 0, 0
            MusicMenu.stop()
            menu.after(100,game_2players)
            menu.after(110, menu.destroy)
        
        def onCanvasClick2(event):
            global scorej1,scorej2
            scorej1,scorej2 = 0, 0
            MusicMenu.stop()
            menu.after(100,game_vsIA)
            menu.after(110, menu.destroy)
             
        def onCanvasClick3(event):
            global scorej1
            scorej1= 0
            MusicMenu.stop()
            menu.after(100,game_vsWall)
            menu.after(110, menu.destroy)
             
        def onCanvasClick4(event):
            MusicMenu.stop()
            menu.destroy()
        
        #clique definition
        MenuCanvas.tag_bind(entre1, '<Button-1>', onCanvasClick1) 
        MenuCanvas.tag_bind(entre1Titre, '<Button-1>', onCanvasClick1)  
        
        MenuCanvas.tag_bind(entre2, '<Button-1>', onCanvasClick2) 
        MenuCanvas.tag_bind(entre2Titre, '<Button-1>', onCanvasClick2)
        
        MenuCanvas.tag_bind(entre3, '<Button-1>', onCanvasClick3) 
        MenuCanvas.tag_bind(entre3Titre, '<Button-1>', onCanvasClick3)
        
        MenuCanvas.tag_bind(entre4, '<Button-1>', onCanvasClick4) 
        MenuCanvas.tag_bind(entre4Titre, '<Button-1>', onCanvasClick4)
        
        animation()
        
    menu.focus_force()
    animIntro()
    menu.mainloop()

    
creatMenu()