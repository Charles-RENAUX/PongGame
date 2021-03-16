# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:53:39 2021

@author: Lenovo
"""

import tkinter as tk
import random as rdm
 
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
     #position initiale de la balle
PosXballmenu=haut_fenetre/4
PosYballmenu=larg_fenetre/2
    #init des scores
scorej1=0
scorej2=0
# ---------------------------------------------------------------------------------------------------------
def game_2players():
    
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
   
    menu.destroy()#Detruire le menu pour utiliser le score
    Pong = tk.Tk()
    Pong.title("[New Game]")
 
    canvas = tk.Canvas(Pong,width = 500, height = 500 , bd=0, bg="black")
    canvas.pack(padx=10,pady=10)

    canvas.focus_set()
   
    Pong.mainloop()
   
  
# -------------------------------------------------------------------------------------------------------------

    
def game_vsWall():
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
            
    
    
    def mouvball():#fonction qui fait bouger la balle et qui gere les colision avec les bordures
        global PosXball, PosYball, dx ,dy,scorej1,scorej2
     
        PosXball = PosXball + dx
     
        PosYball = PosYball + dy
        
        #print("balle:")
        #print(canvas.coords(balle))
     
        canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
     
        if PosYball < 0 or PosYball > 465:
            dy=-dy
            if rdm.randint(1, 10) >7:
                dy+=rdm.randint(0, 3)
        if PosXball> larg_fenetre:
            dx = -dx
            if rdm.randint(1, 10) >8:
                dy+=rdm.randint(0, 2)
            
        if canvas.coords(balle)[0] == 20 and canvas.coords(raquetteJ1)[1] <= canvas.coords(balle)[1] <= canvas.coords(raquetteJ1)[3]:#ici la balle ne rebondit pas sur la raquette
            dx = -dx
            #MAJ du score
            scorej1+=1
            if scorej1%2==0:
                dx+=3
                dy+=2
            canvas.itemconfig(score,text= str(scorej1))
            
        if PosXball<0 :
            #reset position
            PosXball=haut_fenetre/2
            PosYball=larg_fenetre/2
            canvas.coords(balle,PosXball,PosYball,PosXball+10,PosYball+10)
            gameOverScreen()

        canvas.after(50,mouvball)
    
        
    def gameOverScreen():
        global scorej1,dx,dy
        #efface les objets
        canvas.delete(balle)
        canvas.delete(raquetteJ1)
        canvas.delete(score)
        #ecran de game over
        canvas.create_text(larg_fenetre/2,haut_fenetre/2,fill="green",font="Times 40 bold",text="Score : "+ str(scorej1))
        scorej1=0
        dx=5
        dy=7
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
    
    
    #init de la fennetre du menu.
    menu = tk.Tk()
    menu.title("[Pong]")
    menu.geometry("500x500")
    
    #Création du canvas + ajout a la fen
    MenuCanvas = tk.Canvas(menu,width = 500, height = 500 , bd=0, bg="black")
    MenuCanvas.pack(padx=10,pady=10)
    
    #création des elements du jeux
    balleMenu= MenuCanvas.create_oval(PosXballmenu,PosYballmenu,PosXballmenu+20,PosYballmenu+20,fill='white') #balle de rayon 20
    MenuCanvas.create_text(larg_fenetre/2,50,fill="white",font="Times 40 bold",text="PONG")
    raquetteMenu=MenuCanvas.create_rectangle(10,haut_fenetre/4,20,haut_fenetre/4+250,fill='white')
    
    entre1=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4,larg_fenetre/2+210,haut_fenetre/4+50,outline='white')
    entre2=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+70,larg_fenetre/2+210,haut_fenetre/4+120,outline='white')
    entre3=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+140,larg_fenetre/2+210,haut_fenetre/4+190,outline='white')
    entre4=MenuCanvas.create_rectangle(larg_fenetre/2+10,haut_fenetre/4+210,larg_fenetre/2+210,haut_fenetre/4+260,outline='white')
    
    entre1Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+25,fill="white",font="Times 20 bold",text="2 joueurs")
    entre2Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+95,fill="white",font="Times 20 bold",text="vs IA")
    entre3Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+165,fill="white",font="Times 20 bold",text="vs Wall")
    entre4Titre=MenuCanvas.create_text(larg_fenetre/2+105,haut_fenetre/4+235,fill="white",font="Times 20 bold",text="Exit")
    
    def animation():
        global PosXballmenu, PosYballmenu, dx ,dy,haut_fenetre,larg_fenetre
        PosXballmenu = PosXballmenu + dx
        PosYballmenu = PosYballmenu + dy
        MenuCanvas.coords(balleMenu,PosXballmenu,PosYballmenu,PosXballmenu+10,PosYballmenu+10)
        
       
        if PosYballmenu < haut_fenetre/4+25 or PosYballmenu > haut_fenetre/4+250:
            dy=-dy
        if PosXballmenu < 20 or PosXballmenu > larg_fenetre/2:
            dx=-dx
        MenuCanvas.after(50,animation)
        
    def onCanvasClick1(event):
        global scorej1,scorej2
        scorej1,scorej2 = 0, 0
        menu.after(100,game_2players)
        menu.after(110, menu.destroy)
    
    def onCanvasClick2(event):
         menu.after(100,game_vsIA)
         menu.after(110, menu.destroy)
         
    def onCanvasClick3(event):
        global scorej1
        scorej1= 0
        menu.after(100,game_vsWall)
        menu.after(110, menu.destroy)
         
    def onCanvasClick4(event):
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
    
    menu.focus_force()
    animation()
    menu.mainloop()


creatMenu()