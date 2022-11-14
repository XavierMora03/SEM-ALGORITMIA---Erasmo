# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import * 
import re 
import random
class aplicacion(): 
  def __init__ (self): 
    self.raiz =Tk() 
    self.raiz.geometry('600x400') 
    self.raiz.resizable(width=False,height=False) 
    self.raiz.title('Expresiones regulares') 
    label = Label(self.raiz,text="Validacion de expresiones regulares,\nCaracteres especiales y\nGenerador de contraseñas")  
    label.pack(side=TOP)


    self.textos=Frame(self.raiz)
    self.textos.pack(side=TOP)
    self.frameDeAbajo=Frame(self.raiz)
    self.frameDeAbajo.pack(side=BOTTOM)
    self.t1=Entry(self.textos,width=40)
    self.t1.grid(row=0, column=0)
    self.t2=Entry(self.textos,width=40)
    self.t2.grid(row=1,column=0)
    self.t3=Entry(self.textos,width=40)
    self.t3.grid(row=2,column=0, pady=80)
    

    self.b1=Button(self.textos,text='validar',command=lambda:self.validar(1))
    self.b1.grid(row=0, column=1)
    self.b2=Button(self.textos,text='validar',command=lambda:self.validar(2) )
    self.b2.grid(row=1, column=1)
    self.b3=Button(self.textos, text='Generar\nContraseña',command=lambda:self.validar(3)) 
    self.b3.grid(row=2, column=1, pady=80)
    
    self.l1=Label(self.textos,text='...')
    self.l1.grid(row=0,column=2)
    self.l2=Label(self.textos,text='...')
    self.l2.grid(row=1,column=2)
    self.l3=Label(self.textos,text='...')
    self .l3.grid(row=2,column=2, pady=80)
    
    
    self.bsalir=Button(self.frameDeAbajo, text="Salir",command=self.raiz.destroy)
    self.bsalir.pack(side=LEFT)

    self.blimpiar=Button(self.frameDeAbajo, text="Limpiar", command=self.limpiar)
    self.blimpiar.pack(side=LEFT)

    self.raiz.mainloop()
  def limpiar(self):
      self.t1.delete(first=0,last='end')
      self.l1.config(fg='black',text='...')
      self.t2.delete(first=0,last='end')
      self.l2.config(fg='black',text='...')
      self.t3.delete(first=0,last='end')
      self.l3.config(fg='black',text='...')
      
  def validar(self,numero):
      if(numero == 1):
          
          txtAvalidar = self.t1.get()
          x=re.search('^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$', txtAvalidar)
          print(x)
          if x:
              self.l1.config(fg='green',text='IPv4 valida')
          else:
              self.l1.config(fg='red',text='IPv4 invalida')
             
      if(numero == 2):
        txtAvalidar = self.t2.get()
        x=re.search('^[a-zA-Z0-9 ]*$', txtAvalidar)
        print(x)
        if x:
            self.l2.config(fg='green',text='Sin caracteres\nespeciales')
        else:
            self.l2.config(fg='red',text='Con caracteres\nespeciales')
            
      if(numero == 3):
          randomWord = ''
          
          for x in range(random.randint(21, 31)):
              randomWord += chr(random.randint(32, 126))
          self.t3.delete(0,'end')
          self.t3.insert(0,randomWord)
          self.l3.config(fg='green',text='Contraseña\nsegura\ngenerada')
          
        
app=aplicacion() 

