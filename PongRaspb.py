# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:40:15 2021

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
soundRebondRaquette=py.mixer.Sound('SoundPackage/Sound/reboundJoueur2.wav')
soundRebondWallH=py.mixer.Sound('SoundPackage/Sound/reboundWallH.wav') 
soundRebondRaquetteIA=py.mixer.Sound('SoundPackage/Sound/reboundIA.wav')
soundRebondVsWall=py.mixer.Sound('SoundPackage/Sound/reboundVsWall.wav')
gameOverSound=py.mixer.Sound('SoundPackage/Sound/losing.wav')
winSound=py.mixer.Sound('SoundPackage/Sound/win.mp3')
winSoundAlternate=py.mixer.Sound('SoundPackage/Sound/winA.mp3')
plusOne=py.mixer.Sound('SoundPackage/Sound/plusOne.wav')
minusOne=py.mixer.Sound('SoundPackage/Sound/minusOne.wav')
soundAttack=py.mixer.Sound('SoundPackage/Sound/nani.mp3')
soundAttack2=py.mixer.Sound('SoundPackage/Sound/bug.mp3')
soundSpeed=py.mixer.Sound('SoundPackage/Sound/speed.wav')
soundFall=py.mixer.Sound('SoundPackage/Sound/fall.wav')



Startingsound=py.mixer.Sound('SoundPackage/Music/generique.wav')
MusicMenu=py.mixer.Sound('SoundPackage/Music/Menu.mp3')
MusicIA=py.mixer.Sound('SoundPackage/Music/VsIA.mp3')
Music2J=py.mixer.Sound('SoundPackage/Music/2joueurs.mp3')
MusicPODER=py.mixer.Sound('SoundPackage/Music/PODER.mp3')
Music4J=py.mixer.Sound('SoundPackage/Music/4joueurs.mp3')
MusicWall=py.mixer.Sound('SoundPackage/Music/VsWall.mp3')


    #fenetre
haut_fenetre=480;
larg_fenetre=800;

#ZoneDetection et  parametres IA
ZoneDetection = 0.9
mu = 0.4
sigma = 0.1
epsilon = 0.15
cap = 0.95

    #position initiale de la balle
PosXball=haut_fenetre/2
PosYball=larg_fenetre/2
    #position raquette 1,2,3 et 4
PosXj1=10
PosYj1=haut_fenetre/2
PosXj2= larg_fenetre-20
PosYj2= haut_fenetre/2
PosXj3=larg_fenetre/2
PosYj3=10
PosXj4= larg_fenetre/2
PosYj4= haut_fenetre-20


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
scorej3=0
scorej4=0
    #esp mode
espJ1=0
espJ2=0
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
    Pong.title("Pong by Prheidator [Mode 2 joueurs]")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = larg_fenetre, height = haut_fenetre , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    raquetteJ2 = canvas.create_rectangle(PosXj2,PosYj2,PosXj2+10,PosYj2+100,fill='red')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1)+" - "+str(scorej2))
    
    Music2J.play()
    
    def resetAnimation():
        canvas.configure(bg='black')
        canvas.itemconfig(raquetteJ1,fill="blue")
        canvas.itemconfig(raquetteJ2,fill="red")
        canvas.itemconfig(balle,fill="white")
        
    def animPointMarqueJ1():
        canvas.configure(bg='blue')
        canvas.itemconfig(raquetteJ2,fill="red4")
        canvas.itemconfig(raquetteJ1,fill="blue4")
        canvas.after(250,resetAnimation)
        
    def animPointMarqueJ2():
        canvas.configure(bg='red')
        canvas.itemconfig(raquetteJ2,fill="red4")
        canvas.itemconfig(raquetteJ1,fill="blue4")
        canvas.after(250,resetAnimation)
        
    def animSpeedUp():
        soundSpeed.play()
        canvas.configure(bg='white')
        canvas.itemconfig(balle,fill="black")
        canvas.after(250,resetAnimation)
        
    def animDefaiteJ1():
        soundFall.play()
        canvas.coords(balle,500,250,530,280)
        canvas.itemconfig(balle,fill=tabColor[rd.randint(0, 7)])
        canvas.itemconfig(raquetteJ1,fill=tabColor[rd.randint(0, 7)])
        if canvas.coords(raquetteJ1)[1]<=haut_fenetre:
            canvas.move(raquetteJ1,5,15)
            canvas.after(100,resetAnimation)
        else:
            gameOverScreen()
    
    def animDefaiteJ2():
        soundFall.play()
        canvas.coords(balle,300,250,330,280)
        canvas.itemconfig(balle,fill=tabColor[rd.randint(0, 7)])
        canvas.itemconfig(raquetteJ2,fill=tabColor[rd.randint(0, 7)])
        if canvas.coords(raquetteJ2)[1]<=haut_fenetre:
            canvas.move(raquetteJ2,-5,15)
            canvas.after(100,resetAnimation)
        else:
            gameOverScreen()
        
    
    def anglej1():
       global PosXball, PosYball, dx ,dy, PosYj1
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[3]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[3] < canvas.coords(raquetteJ1)[1]+35 :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy-6
           animSpeedUp()
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+35 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+65 :
           #modif vitesse
           #print("3")
           soundRebondRaquette.play()
           if dx>=10:
               dx=dx-3
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+65 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy+6
           animSpeedUp()
           #print("5")
        
    def anglej2():
       global PosXball, PosYball, dx ,dy, PosYj2
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[3]>=canvas.coords(raquetteJ2)[1] and canvas.coords(balle)[3] < canvas.coords(raquetteJ2)[1]+35 :
           #modif angle
           if dx>-25:
               dx=dx-5
           dy=dy-6
           animSpeedUp()
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+35 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+65 :
           #modif vitesse
           soundRebondRaquette.play()
           #print("3")
           if dx<=-10:
               dx=dx+3
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+65 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[3] :
           #modif angle
           if dx>-25:
               dx=dx-5
           dy=dy+6
           animSpeedUp()
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
             if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre-10:
                 canvas.move(raquetteJ1,0,20)
                 #print(canvas.coords(raquetteJ1))
        def hautj2():
             if canvas.coords(raquetteJ2)[1]>=10:
                canvas.move(raquetteJ2,0,-20)
                #print(canvas.coords(raquetteJ2))
        def basj2():
             if canvas.coords(raquetteJ2)[1]+100<=haut_fenetre-10:
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
     
        if PosYball < 0 or PosYball > haut_fenetre-20:
            dy=-dy
            soundRebondWallH.play()
            
        if canvas.coords(balle)[0] >= larg_fenetre-25 and canvas.coords(raquetteJ2)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ2)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            anglej2()
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            anglej1()
            
        if PosXball<0 :
            if scorej2<5:
                #reset position
                PosXball=haut_fenetre/2 + 150
                PosYball=larg_fenetre/2-150
                dx=-8
                dy=10
                canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
                
                #MAJ du score
                minusOne.play()
                scorej2+=1
                canvas.after(10,animPointMarqueJ2)
                canvas.after(300,animPointMarqueJ2)
                
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
        if PosXball > larg_fenetre:
            
            if scorej1<5:
                #reset position
                minusOne.play()
                PosXball=haut_fenetre/2
                PosYball=larg_fenetre/2
                dx=8
                dy=10
                canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
                
                #MAJ du score
                scorej1+=1
                canvas.after(10,animPointMarqueJ1)
                canvas.after(300,animPointMarqueJ1)
                
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
            
        
        if scorej1>=5 :
           dx=0
           dy=0
           animDefaiteJ2()
            
        if scorej2>=5:
            dx=0
            dy=0
            animDefaiteJ1()
            
            
            
                
        if not py.mixer.get_busy():
            Music2J.play()
    
        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        global scorej1,scorej2,dx,dy
        dx=8
        dy=10
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

# ---------------------------------------------------------------------------------------------------------
def game_2playersPODER():
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
    Pong.title("Pong by Prheidator [Mode 2 joueurs version PODER]")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = larg_fenetre, height = haut_fenetre , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    raquetteJ2 = canvas.create_rectangle(PosXj2,PosYj2,PosXj2+10,PosYj2+100,fill='red')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1)+" - "+str(scorej2))
    barreEspJ1=canvas.create_rectangle(larg_fenetre/2-62,80,larg_fenetre/2-8,100,outline='white')
    barreEspJ1Int=canvas.create_rectangle(larg_fenetre/2-60,82,larg_fenetre/2-60,98,fill='blue')
    barreEspJ2=canvas.create_rectangle(larg_fenetre/2+8,80,larg_fenetre/2+62,100,outline='white')
    barreEspJ2Int=canvas.create_rectangle(larg_fenetre/2+10,82,larg_fenetre/2+10,98,fill='red')
    
    MusicPODER.play()
    
    def resetAnimation():
        canvas.configure(bg='black')
        canvas.itemconfig(raquetteJ1,fill="blue")
        canvas.itemconfig(raquetteJ2,fill="red")
        canvas.itemconfig(balle,fill="white")
        
    def animPointMarqueJ1():
        canvas.configure(bg='blue')
        canvas.itemconfig(raquetteJ2,fill="red4")
        canvas.itemconfig(raquetteJ1,fill="blue4")
        canvas.after(250,resetAnimation)
        
    def animPointMarqueJ2():
        canvas.configure(bg='red')
        canvas.itemconfig(raquetteJ2,fill="red4")
        canvas.itemconfig(raquetteJ1,fill="blue4")
        canvas.after(250,resetAnimation)
        
    def animSpeedUp():
        soundSpeed.play()
        canvas.configure(bg='white')
        canvas.itemconfig(balle,fill="black")
        canvas.after(250,resetAnimation)
        
    def animDefaiteJ1():
        soundFall.play()
        canvas.coords(balle,500,250,530,280)
        canvas.itemconfig(balle,fill=tabColor[rd.randint(0, 7)])
        canvas.itemconfig(raquetteJ1,fill=tabColor[rd.randint(0, 7)])
        if canvas.coords(raquetteJ1)[1]<=haut_fenetre:
            canvas.move(raquetteJ1,5,15)
            canvas.after(100,resetAnimation)
        else:
            gameOverScreen()
    
    def animDefaiteJ2():
        soundFall.play()
        canvas.coords(balle,300,250,330,280)
        canvas.itemconfig(balle,fill=tabColor[rd.randint(0, 7)])
        canvas.itemconfig(raquetteJ2,fill=tabColor[rd.randint(0, 7)])
        if canvas.coords(raquetteJ2)[1]<=haut_fenetre:
            canvas.move(raquetteJ2,-5,15)
            canvas.after(100,resetAnimation)
        else:
            gameOverScreen()
    
    def anglej1():
       global PosXball, PosYball, dx ,dy, PosYj1
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[3]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[3] < canvas.coords(raquetteJ1)[1]+35 :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy-6
           animSpeedUp()
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+35 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+65 :
           #modif vitesse
           #print("3")
           soundRebondRaquette.play()
           if dx>=10:
               dx=dx-3
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+65 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy+6
           animSpeedUp()
           #print("5")
        
    def anglej2():
       global PosXball, PosYball, dx ,dy, PosYj2
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[3]>=canvas.coords(raquetteJ2)[1] and canvas.coords(balle)[3] < canvas.coords(raquetteJ2)[1]+35 :
           #modif angle
           if dx>-25:
               dx=dx-5
           dy=dy-6
           animSpeedUp()
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+35 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+65 :
           #modif vitesse
           soundRebondRaquette.play()
           #print("3")
           if dx<=-10:
               dx=dx+3
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+65 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[3] :
           #modif angle
           if dx>-25:
               dx=dx-5
           dy=dy+6
           animSpeedUp()
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
             if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre-10:
                 canvas.move(raquetteJ1,0,20)
                 #print(canvas.coords(raquetteJ1))
        def hautj2():
             if canvas.coords(raquetteJ2)[1]>=10:
                canvas.move(raquetteJ2,0,-20)
                #print(canvas.coords(raquetteJ2))
        def basj2():
             if canvas.coords(raquetteJ2)[1]+100<=haut_fenetre-10:
                canvas.move(raquetteJ2,0,20)
                #print(canvas.coords(raquetteJ2))
        
        def  attaquej1():
            global dy,dx,espJ1
            if  canvas.coords(balle)[0] <= 90 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:
                if espJ1==2:
                    Music2J.set_volume(0.2)
                    soundAttack.play()
                    soundAttack.set_volume(1.0)
                    dy=0
                    dx=50
                    espJ1=0
                    x0,y0,x1,y1 = canvas.coords(barreEspJ1Int)
                    x1=larg_fenetre/2-60+(25*espJ1)
                    canvas.coords(barreEspJ1Int,x0,y0,x1,y1)
                    canvas.after(3000,Music2J.set_volume(1.0))
                    
                     
        def  attaquej2():
            global dy,dx,espJ2
            if canvas.coords(balle)[0] >= larg_fenetre-100 and canvas.coords(raquetteJ2)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ2)[3]:
                if espJ2==2:
                    Music2J.set_volume(0.2)
                    soundAttack2.play()
                    soundAttack2.set_volume(1.0)
                    dy=0
                    dx=-50
                    espJ2=0
                    x0,y0,x1,y1 = canvas.coords(barreEspJ2Int)
                    x1=larg_fenetre/2+10+(25*espJ2)
                    canvas.coords(barreEspJ2Int,x0,y0,x1,y1)
                    canvas.after(3000,Music2J.set_volume(1.0))
        
        if Key == 'z':
             hautj1()
        if Key == 's':
             basj1()
        if Key == 'p':
            hautj2()
        if Key == 'm':
            basj2()
        if Key == 'a':
            attaquej1()
        if Key == 'l':
            attaquej2()
    
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2,espJ1,espJ2
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if PosYball < 0 or PosYball > haut_fenetre-20:
            dy=-dy
            soundRebondWallH.play()
            
        if canvas.coords(balle)[0] >= larg_fenetre-25 and canvas.coords(raquetteJ2)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ2)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            if espJ2<2:
               espJ2+=1
               x0,y0,x1,y1 = canvas.coords(barreEspJ2Int)
               x1=larg_fenetre/2+10+(25*espJ2)
               canvas.coords(barreEspJ2Int,x0,y0,x1,y1)
            anglej2()
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            if espJ1<2:
               espJ1+=1
               x0,y0,x1,y1 = canvas.coords(barreEspJ1Int)
               x1=larg_fenetre/2-60+(25*espJ1)
               canvas.coords(barreEspJ1Int,x0,y0,x1,y1)
            anglej1()
            
        if PosXball<0 :
            if scorej2<5:
                #reset position
                PosXball=haut_fenetre/2 + 150
                PosYball=larg_fenetre/2-150
                dx=-8
                dy=10
                canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
                
                #MAJ du score
                minusOne.play()
                scorej2+=1
                
                espJ1=0
                x0,y0,x1,y1 = canvas.coords(barreEspJ1Int)
                x1=larg_fenetre/2-60+(10*espJ1)
                canvas.coords(barreEspJ1Int,x0,y0,x1,y1)
                
                
                canvas.after(10,animPointMarqueJ2)
                canvas.after(300,animPointMarqueJ2)
                
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
            
            
        if PosXball > larg_fenetre:
            if scorej1<5:
                #reset position
                PosXball=haut_fenetre/2
                PosYball=larg_fenetre/2
                dx=8
                dy=10
                canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
                
                #MAJ du score
                minusOne.play()
                scorej1+=1
                
                espJ2=0
                x0,y0,x1,y1 = canvas.coords(barreEspJ2Int)
                x1=larg_fenetre/2+10+(10*espJ2)
                canvas.coords(barreEspJ2Int,x0,y0,x1,y1)
            
                canvas.after(10,animPointMarqueJ1)
                canvas.after(300,animPointMarqueJ1)
                
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
            
        
        if scorej1>=5 :
           dx=0
           dy=0
           animDefaiteJ2()
            
        if scorej2>=5:
            dx=0
            dy=0
            animDefaiteJ1()
            
                
        if not py.mixer.get_busy():
            Music2J.play()
    
        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        global scorej1,scorej2,dx,dy
        dx=8
        dy=10
        #efface les objets
        canvas.delete(balle)
        canvas.delete(raquetteJ1)
        canvas.delete(raquetteJ2)
        canvas.delete(score)
        canvas.delete(barreEspJ1)
        canvas.delete(barreEspJ1Int)
        canvas.delete(barreEspJ2)
        canvas.delete(barreEspJ2Int)
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
    Pong.title("Pong by Prheidator [Mode 1 joueur VS IA]")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = larg_fenetre, height = haut_fenetre , bd=0, bg="black")
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
                if canvas.coords(raquetteIA)[1]+100<=haut_fenetre-10:
                    canvas.move(raquetteIA,0,20)
                    
        
       
        #print(zoneBall)
     
    
    def resetAnimation():
        canvas.configure(bg='black')
        canvas.itemconfig(raquetteJ1,fill="blue")
        canvas.itemconfig(raquetteIA,fill="red")
        canvas.itemconfig(balle,fill="white")
        
    def animPointMarqueJ1():
        canvas.configure(bg='blue')
        canvas.itemconfig(raquetteIA,fill="red4")
        canvas.itemconfig(raquetteJ1,fill="blue4")
        canvas.after(250,resetAnimation)
        
    def animPointMarqueJ2():
        canvas.configure(bg='red')
        canvas.itemconfig(raquetteIA,fill="red4")
        canvas.itemconfig(raquetteJ1,fill="blue4")
        canvas.after(250,resetAnimation)
        
    def animSpeedUp():
        soundSpeed.play()
        canvas.configure(bg='white')
        canvas.itemconfig(balle,fill="black")
        canvas.after(250,resetAnimation)
    
    def animDefaiteJ1():
        soundFall.play()
        canvas.coords(balle,500,250,530,280)
        canvas.itemconfig(balle,fill=tabColor[rd.randint(0, 7)])
        canvas.itemconfig(raquetteJ1,fill=tabColor[rd.randint(0, 7)])
        if canvas.coords(raquetteJ1)[1]<=haut_fenetre:
            canvas.move(raquetteJ1,5,15)
            canvas.after(100,resetAnimation)
        else:
            gameOverScreen()
    
    def animDefaiteJ2():
        soundFall.play()
        canvas.coords(balle,300,250,330,280)
        canvas.itemconfig(balle,fill=tabColor[rd.randint(0, 7)])
        canvas.itemconfig(raquetteIA,fill=tabColor[rd.randint(0, 7)])
        if canvas.coords(raquetteIA)[1]<=haut_fenetre:
            canvas.move(raquetteIA,-5,15)
            canvas.after(100,resetAnimation)
        else:
            gameOverScreen()
    
    def angle():
       global PosXball, PosYball, dx ,dy, PosYj1
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[3]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[3] < canvas.coords(raquetteJ1)[1]+35 :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy-6
           animSpeedUp()
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+35 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+65 :
           #modif vitesse
           #print("3")
           soundRebondRaquette.play()
           if dx>=10:
               dx=dx-3
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+65 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy+6
           animSpeedUp()
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
            if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre-10:
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
     
        if PosYball < 0 or PosYball > haut_fenetre-20:
            dy=-dy
            soundRebondWallH.play()
            
        if canvas.coords(balle)[0] >= larg_fenetre-25 and canvas.coords(raquetteIA)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteIA)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            #update de la zone de detection
            ZoneDetection = ZoneDetectionUpdate()
            soundRebondRaquetteIA.play()
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            angle()
            
        if PosXball<0 :
            if scorej2<5:
                #reset position
                PosXball=haut_fenetre/2 + 150
                PosYball=larg_fenetre/2-150
                dx=-8
                dy=10
                canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
                
                #MAJ du score
                minusOne.play()
                scorej2+=1
                canvas.after(10,animPointMarqueJ2)
                canvas.after(300,animPointMarqueJ2)
                
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
        if PosXball > larg_fenetre:
            
            if scorej1<5:
                #reset position
                plusOne.play()
                PosXball=haut_fenetre/2
                PosYball=larg_fenetre/2
                dx=8
                dy=10
                canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
                
                #MAJ du score
                scorej1+=1
                canvas.after(10,animPointMarqueJ1)
                canvas.after(300,animPointMarqueJ1)
                
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
            
        
        if scorej1>=5 :
           dx=0
           dy=0
           animDefaiteJ2()
            
        if scorej2>=5:
            dx=0
            dy=0
            animDefaiteJ1()
            
        if not py.mixer.get_busy():
           MusicIA.play()    
            
        canvas.after(20,IA)
        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        global dx,dy
        dx=8
        dy=10
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
   
 
# ---------------------------------------------------------------------------------------------------------
def game_4players():
    global larg_fenetre,haut_fenetre,scorej1, scorej2, scorej3,scorej4
    MusicMenu.stop()
   
       
    #init des scores
    scorej1=5
    scorej2=5
    scorej3=5
    scorej4=5
    #init de la fennetre de jeux.
    Pong = tk.Tk()
    Pong.title("Pong by Prheidator [Mode 4 joueurs]")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = larg_fenetre, height = haut_fenetre , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    mur1=canvas.create_rectangle(0,0,150,10,fill='white')
    mur2=canvas.create_rectangle(larg_fenetre-150,0,larg_fenetre,10,fill='white')
    mur3=canvas.create_rectangle(0,haut_fenetre,150,haut_fenetre-10,fill='white')
    mur4=canvas.create_rectangle(larg_fenetre-150,haut_fenetre,larg_fenetre,haut_fenetre-10,fill='white')
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    raquetteJ2 = canvas.create_rectangle(PosXj2,PosYj2,PosXj2+10,PosYj2+100,fill='red')
    raquetteJ3 = canvas.create_rectangle(PosXj3,PosYj3,PosXj3+100,PosYj3+10,fill='green')
    raquetteJ4 = canvas.create_rectangle(PosXj4,PosYj4,PosXj4+100,PosYj4+10,fill='yellow')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1)+" - "+str(scorej2))
    
    Music4J.play()
    
    def anglej1():
       global dx ,dy
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+20 :
           #modif angle
           dy=dy-6
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+20 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+40 :
           #modif angle
           dy=dy-4
           #print("2")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+40 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+60 :
           #vitesse de la balle
            dx=8
            dy=10
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+60 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+80 :
           #modif angle
           dy=dy+4
           #print("4")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+80 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           dy=dy+6
           #print("5")
        
    def anglej2():
       global dx ,dy
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1] and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+20 :
           #modif angle
           dy=dy-6
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+20 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+40 :
           #modif angle
           dy=dy-4
           #print("2")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+40 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+60 :
           #vitesse de la balle
            dx=8
            dy=10
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+60 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[1]+80 :
           #modif angle
           dy=dy+4
           #print("4")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ2)[1]+80 and canvas.coords(balle)[1] < canvas.coords(raquetteJ2)[3] :
           dy=dy+6
           #print("5")
           
           
    def anglej3():
       global dx ,dy
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[0]>=canvas.coords(raquetteJ3)[0] and canvas.coords(balle)[0] < canvas.coords(raquetteJ3)[0]+20 :
           #modif angle
           dx=dx-6
           #print("1")
       if canvas.coords(balle)[0]>=canvas.coords(raquetteJ3)[0]+20 and canvas.coords(balle)[0] < canvas.coords(raquetteJ3)[0]+40 :
           #modif angle
           dx=dx-4
           #print("2")
       if canvas.coords(balle)[0]>=canvas.coords(raquetteJ3)[0]+40 and canvas.coords(balle)[0] < canvas.coords(raquetteJ3)[0]+60 :
           #vitesse de la balle
            dx=8
            dy=10
       if canvas.coords(balle)[0]>=canvas.coords(raquetteJ3)[0]+60 and canvas.coords(balle)[0] < canvas.coords(raquetteJ3)[0]+80 :
           #modif angle
           dx=dx+4
           #print("4")
       if canvas.coords(balle)[0]>=canvas.coords(raquetteJ3)[0]+80 and canvas.coords(balle)[0] < canvas.coords(raquetteJ2)[3] :
           dx=dx+6
           #print("5")
           
    def anglej4():
        global  dx ,dy
        #detection frappe de la balle entre 5zones de la raquette
        if canvas.coords(balle)[0]>=canvas.coords(raquetteJ4)[0] and canvas.coords(balle)[0] < canvas.coords(raquetteJ4)[0]+20 :
            #modif angle
            dx=dx-6
            #print("1")
        if canvas.coords(balle)[0]>=canvas.coords(raquetteJ4)[0]+20 and canvas.coords(balle)[0] < canvas.coords(raquetteJ4)[0]+40 :
            #modif angle
            dx=dx-4
            #print("2")
        if canvas.coords(balle)[0]>=canvas.coords(raquetteJ4)[0]+40 and canvas.coords(balle)[0] < canvas.coords(raquetteJ4)[0]+60 :
            #vitesse de la balle
             dx=8
             dy=10
        if canvas.coords(balle)[0]>=canvas.coords(raquetteJ4)[0]+60 and canvas.coords(balle)[0] < canvas.coords(raquetteJ4)[0]+80 :
            #modif angle
            dx=dx+4
            #print("4")
        if canvas.coords(balle)[0]>=canvas.coords(raquetteJ4)[0]+80 and canvas.coords(balle)[0] < canvas.coords(raquetteJ2)[3] :
            dx=dx+6
            #print("5")
           
           
    #mapping clavier pour le mouvement des raquettes
    def mouvement(event):
        global PosYj1,PosYj2,PosXj3,PosXj4
        Key = event.keysym
     
        def hautj1():
             if canvas.coords(raquetteJ1)[1]>=10:
                 canvas.move(raquetteJ1,0,-20)
                 #print(canvas.coords(raquetteJ1))
        def basj1():
             if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre-10:
                 canvas.move(raquetteJ1,0,20)
                 #print(canvas.coords(raquetteJ1))
        def hautj2():
             if canvas.coords(raquetteJ4)[0]>=10:
                canvas.move(raquetteJ2,0,-20)
                #print(canvas.coords(raquetteJ2))
        def basj2():
             if canvas.coords(raquetteJ2)[1]+100<=haut_fenetre-10:
                canvas.move(raquetteJ2,0,20)
                #print(canvas.coords(raquetteJ2))
                
        def gauchej3():
            if canvas.coords(raquetteJ3)[0]>=160:
                canvas.move(raquetteJ3,-20,0)
        def droitej3(): 
            if canvas.coords(raquetteJ3)[2]<=larg_fenetre-160:
                canvas.move(raquetteJ3,+20,0)
                
        def gauchej4():
            if canvas.coords(raquetteJ4)[0]>=160:
                canvas.move(raquetteJ4,-20,0)
        def droitej4(): 
            if canvas.coords(raquetteJ4)[2]<=larg_fenetre-160:
                canvas.move(raquetteJ4,+20,0)
               
        
        if Key == 'z':
             hautj1()
        if Key == 's':
             basj1()
        if Key == 'p':
            hautj2()
        if Key == 'm':
            basj2()
        if Key == 't':
             gauchej3()
        if Key == 'y':
             droitej3()
        if Key == 'c':
             gauchej4()
        if Key == 'v':
             droitej4()
    
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2,scorej3,scorej4
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if (PosYball < 20 and PosXball <= 150) or (PosYball > haut_fenetre-30 and PosXball>= larg_fenetre-150) or (PosYball < 20 and PosXball>= larg_fenetre-150) or (PosYball > haut_fenetre-30 and PosXball <= 150):
            dy=-dy
            soundRebondWallH.play()
            
        if canvas.coords(balle)[0] >= larg_fenetre-25 and canvas.coords(raquetteJ2)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ2)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            anglej2()
           
        if canvas.coords(balle)[0] <= 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            soundRebondRaquette.play()
            anglej1()
            
        if canvas.coords(balle)[1] <= 20 and canvas.coords(raquetteJ3)[0] <= canvas.coords(balle)[0] <= canvas.coords(raquetteJ3)[2]:#ici la balle ne rebondit pas sur la raquette
            dy = -dy
            soundRebondRaquette.play()
            anglej3()
            
        if canvas.coords(balle)[3] >= haut_fenetre-25 and canvas.coords(raquetteJ4)[0] <= canvas.coords(balle)[2] <= canvas.coords(raquetteJ4)[2]:#ici la balle ne rebondit pas sur la raquette
            dy = -dy
            soundRebondRaquette.play()
            anglej4()
            
        if PosXball<0 :
            minusOne.play()
            #reset position
            PosXball=350
            PosYball=250
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            
            #MAJ du score
            scorej2-=1
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
        if PosXball > larg_fenetre:
            minusOne.play()
            #reset position
            PosXball=350
            PosYball=250
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            #MAJ du score
            scorej1-=1
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
            
        if PosYball < 0:
            minusOne.play()
            #reset position
            PosXball=350
            PosYball=250
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            #MAJ du score
            scorej3-=1
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
         
        if PosYball > haut_fenetre:
            minusOne.play()
            #reset position
            PosXball=350
            PosYball=250
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            #MAJ du score
            scorej4 -=1
            canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))   
    
        if scorej1<=0 and scorej2<=0 and scorej3 <=0:
            gameOverScreen()
        if scorej4<=0 and scorej2<=0 and scorej3 <=0:
            gameOverScreen()
        if scorej1<=0 and scorej4<=0 and scorej3 <=0:
            gameOverScreen()
        if scorej1<=0 and scorej2<=0 and scorej4 <=0:
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
        canvas.delete(raquetteJ3)
        canvas.delete(raquetteJ4)
        canvas.delete(score)
        canvas.delete(mur1)
        canvas.delete(mur2)
        canvas.delete(mur3)
        canvas.delete(mur4)
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
    Pong.title("Pong by Prheidator [Mode 1 joueur VS the f**g Wall]")
    
    #Création du canvas + ajout a la fen
    canvas = tk.Canvas(Pong,width = larg_fenetre, height = haut_fenetre , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)
    
    
    #création des elements du jeux
    balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
    raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
    score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1))
    
    MusicWall.play()
    
    def resetAnimation():
        canvas.configure(bg='black')
        canvas.itemconfig(balle,fill="white")
    
    def animSpeedUp():
        soundSpeed.play()
        canvas.configure(bg='white')
        canvas.itemconfig(balle,fill="black")
        canvas.after(250,resetAnimation)
     
    #mapping clavier pour le mouvement des raquettes
    def mouvement(event):
        global PosYj1
        Key = event.keysym
        def hautj1():
            if canvas.coords(raquetteJ1)[1]>=10:
                canvas.move(raquetteJ1,0,-20)
                #print(canvas.coords(raquetteJ1))
        def basj1():
            if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre-10:
                canvas.move(raquetteJ1,0,20)
                #print(canvas.coords(raquetteJ1))
        if Key == 'z':
            hautj1()
        if Key == 's':
            basj1()
            
    
    def angle():
       global PosXball, PosYball, dx ,dy, PosYj1
       #detection frappe de la balle entre 5zones de la raquette
       if canvas.coords(balle)[3]>=canvas.coords(raquetteJ1)[1] and canvas.coords(balle)[3] < canvas.coords(raquetteJ1)[1]+35 :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy-6
           animSpeedUp()
           #print("1")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+35 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[1]+65 :
           #modif vitesse
           #print("3")
           soundRebondRaquette.play()
           if dx>=10:
               dx=dx-3
               #print("-actif")
       if canvas.coords(balle)[1]>=canvas.coords(raquetteJ1)[1]+65 and canvas.coords(balle)[1] < canvas.coords(raquetteJ1)[3] :
           #modif angle
           if dx<25:
               dx=dx+5
           dy=dy+6
           animSpeedUp()
           #print("5")
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2,soundRebondRaquette
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if PosYball < 0 or PosYball > haut_fenetre-20:
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
    menu.title("Pong by Prheidator")
    
    
    #Création du canvas + ajout a la fen
    MenuCanvas = tk.Canvas(menu,width = larg_fenetre, height = haut_fenetre , bd=0, bg="black")
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
        MenuCanvas.create_image(40,200, anchor = tk.NW, image=photo)
        balleMenu= MenuCanvas.create_oval(PosXballmenu,PosYballmenu,PosXballmenu+20,PosYballmenu+20,fill='white') #balle de rayon 20
        MenuCanvas.create_text(larg_fenetre/4,250,fill="white",font="Times 40 bold",text="PONG")
        MenuCanvas.create_text(larg_fenetre/4+50,275,fill="white",font="Times 8 bold",text="by Prheidator")
        raquetteMenu=MenuCanvas.create_rectangle(10,haut_fenetre/4,20,haut_fenetre/4+250,fill='white')
        
        
        entre1=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4,larg_fenetre/2+310,haut_fenetre/4+50,outline='white')
        entre2=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+70,larg_fenetre/2+310,haut_fenetre/4+120,outline='white')
        entre3=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+140,larg_fenetre/2+310,haut_fenetre/4+190,outline='white')
        entre4=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+280,larg_fenetre/2+310,haut_fenetre/4+330,outline='white')
        entre5=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+210,larg_fenetre/2+310,haut_fenetre/4+260,outline='white')
        entre6=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4-70,larg_fenetre/2+310,haut_fenetre/4-20,outline='white')
        
        entre1Titre=MenuCanvas.create_text(larg_fenetre/2+160,haut_fenetre/4+25,fill="white",font="Times 20 bold",text="2 joueurs")
        entre2Titre=MenuCanvas.create_text(larg_fenetre/2+160,haut_fenetre/4+95,fill="white",font="Times 20 bold",text="vs IA")
        entre3Titre=MenuCanvas.create_text(larg_fenetre/2+160,haut_fenetre/4+165,fill="white",font="Times 20 bold",text="vs Wall")
        entre4Titre=MenuCanvas.create_text(larg_fenetre/2+160,haut_fenetre/4+305,fill="white",font="Times 20 bold",text="Exit")
        entre5Titre=MenuCanvas.create_text(larg_fenetre/2+160,haut_fenetre/4+235,fill="white",font="Times 20 bold",text="4 joueurs")
        entre6Titre=MenuCanvas.create_text(larg_fenetre/2+160,haut_fenetre/4-45,fill="white",font="Times 20 bold",text="2J - PODER")
        
        MenuCanvas.create_text(larg_fenetre-50,haut_fenetre-50,fill="white",font="Times 8 bold",text="Beta 1.8.5")
        
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
        
        def onCanvasClick5(event):
            global scorej1,scorej2,scorej3, scorej4
            scorej1,scorej2,scorej3, scorej4 = 0, 0, 0, 0
            MusicMenu.stop()
            menu.after(100,game_4players)
            menu.after(110, menu.destroy)
            
        def onCanvasClick6(event):
            global scorej1,scorej2,espJ1, espJ2
            scorej1,scorej2 = 0, 0
            espJ1, espJ2 = 0,0
            MusicMenu.stop()
            menu.after(100,game_2playersPODER)
            menu.after(110, menu.destroy)
            
            
        #clique definition
        MenuCanvas.tag_bind(entre1, '<Button-1>', onCanvasClick1) 
        MenuCanvas.tag_bind(entre1Titre, '<Button-1>', onCanvasClick1)  
        
        MenuCanvas.tag_bind(entre2, '<Button-1>', onCanvasClick2) 
        MenuCanvas.tag_bind(entre2Titre, '<Button-1>', onCanvasClick2)
        
        MenuCanvas.tag_bind(entre3, '<Button-1>', onCanvasClick3) 
        MenuCanvas.tag_bind(entre3Titre, '<Button-1>', onCanvasClick3)
        
        MenuCanvas.tag_bind(entre4, '<Button-1>', onCanvasClick4) 
        MenuCanvas.tag_bind(entre4Titre, '<Button-1>', onCanvasClick4)
        
        #clique definition
        MenuCanvas.tag_bind(entre5, '<Button-1>', onCanvasClick5) 
        MenuCanvas.tag_bind(entre5Titre, '<Button-1>', onCanvasClick5) 
        
        #clique definition
        MenuCanvas.tag_bind(entre6, '<Button-1>', onCanvasClick6) 
        MenuCanvas.tag_bind(entre6Titre, '<Button-1>', onCanvasClick6) 
        animation()
        
    menu.focus_force()
    animIntro()
    menu.mainloop()

    
creatMenu()