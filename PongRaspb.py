# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:28:14 2021

@author: Lenovo
"""

#Initialisation de la biliotheque tkinter + random
import tkinter as tk
#import random as rdm


#Initialisation des variables 
    #fenetre
haut_fenetre=500;
larg_fenetre=500;
    #position initiale de la balle
PosXball=haut_fenetre/2
PosYball=larg_fenetre/2
    #position raquette 1 et 2
PosXj1=10
PosYj1=haut_fenetre/2
PosXj2= larg_fenetre-20
PosYj2= haut_fenetre/2
    #vitesse de la balle
dx=5
dy=7
    #init des scores
scorej1=0
scorej2=0

#init de la fennetre de jeux.
Pong = tk.Tk()
Pong.tittle=("Jeu de Pong")

#Création du canvas + ajout a la fen
canvas = tk.Canvas(Pong,width = 500, height = 500 , bd=0, bg="black")
canvas.pack(padx=10,pady=10)


#création des elements du jeux
balle = canvas.create_oval(PosXball,PosYball,PosXball+20,PosYball+20,fill='white') #balle de rayon 20
raquetteJ1 = canvas.create_rectangle(PosXj1,PosYj1,PosXj1+10,PosYj1+100,fill='blue')
raquetteJ2 = canvas.create_rectangle(PosXj2,PosYj2,PosXj2+10,PosYj2+100,fill='red')
score=canvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text=str(scorej1)+" - "+str(scorej2))




 
#mapping clavier pour le mouvement des raquettes
def mouvement(event):
    global PosYj1,PosYj2
    Key = event.keysym
 
    if Key == 'z':
        if canvas.coords(raquetteJ1)[1]>=10:
            canvas.move(raquetteJ1,0,-20)
            #print(canvas.coords(raquetteJ1))
    if Key == 's':
        if canvas.coords(raquetteJ1)[1]+100<=haut_fenetre:
            canvas.move(raquetteJ1,0,20)
            #print(canvas.coords(raquetteJ1))
    if Key == 'p':
        if canvas.coords(raquetteJ2)[1]>=10:
            canvas.move(raquetteJ2,0,-20)
            #print(canvas.coords(raquetteJ2))
    if Key == 'm':
        if canvas.coords(raquetteJ2)[1]+100<=haut_fenetre:
            canvas.move(raquetteJ2,0,20)
            #print(canvas.coords(raquetteJ2))
        


def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
    global PosXball, PosYball, dx ,dy,scorej1,scorej2
 
    PosXball = PosXball + dx
 
    PosYball = PosYball + dy
    
    #print("balle:")
    #print(canvas.coords(balle))
 
    canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
 
    if PosYball < 0 or PosYball > 465:
        dy=-dy
        
    if canvas.coords(balle)[0] == 480 and canvas.coords(raquetteJ2)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ2)[3]:#ici la balle ne rebondit pas sur la raquette
        dx = -dx
    if canvas.coords(balle)[0] == 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
        dx = -dx
        
    if PosXball<0 :
        #reset position
        PosXball=haut_fenetre/2
        PosYball=larg_fenetre/2
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
        
        #MAJ du score
        scorej2+=1
        canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
        
    if PosXball > larg_fenetre:
        #reset position
        PosXball=haut_fenetre/2
        PosYball=larg_fenetre/2
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
        
        #MAJ du score
        scorej1+=1
        canvas.itemconfig(score,text= str(scorej1)+" - "+str(scorej2))
        
        
    
    if scorej1>=5 or scorej2>=5:
        gameOverScreen()
        
            
        

    canvas.after(50,mouvball)

    
def gameOverScreen():
    #efface les objets
    canvas.delete(balle)
    canvas.delete(raquetteJ1)
    canvas.delete(raquetteJ2)
    canvas.delete(score)
    #ecran de game over
    if scorej1>=5:
        canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="blue",font="Times 40 bold",text="Victoire J1 : "+ str(scorej1)+" - "+str(scorej2))
    if scorej2>=5:
        canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="red",font="Times 40 bold",text="Victoire J2 : "+ str(scorej2)+" - "+str(scorej1))    



canvas.focus_set()#on met le focus sur le canvas
Pong.focus_force()
#on dit au canvas de prendre en compte les actions de mouvement(event)
#on ne doit pas laisser les touches enfonce
canvas.bind('<Key>',mouvement) 

mouvball()
Pong.mainloop()