import tkinter 
from tkinter import *
from tkinter import messagebox




form=Tk()

def reset():
     button1['text'] = button2['text'] = button3['text'] = button4['text'] = button5['text'] = button6['text'] = ' '
     button7['text'] = button8['text'] = button9['text'] = ' '
     
     
click=True

def put(buttons):
    global click
    
    
    '''
    123
    456
    789
    '''
    form.update()



    if buttons['text']==' ' and click==True:
         buttons['text']='X'
         buttons['foreground']='blue'
         #buttons['background']=''
         click=False

    elif  buttons['text']==' ' and click==False:
          buttons['text']='O'
          buttons['foreground']='red'
          click=True
          
    elif buttons['text']!=' ' :
        
        messagebox.showerror('','is not empty')
     

    else: messagebox.showinfo('',' no one won')

    if   (button1['text'] == button2['text'] == button3['text'] == 'O') : button1['text'] = button2['text'] = button3['text'] = '-' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset() 
    elif (button4['text'] == button5['text'] == button6['text'] == 'O') : button4['text'] = button5['text'] = button6['text'] = '-' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset()
    elif (button7['text'] == button8['text'] == button9['text'] == 'O') : button7['text'] = button8['text'] = button9['text'] = '-' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset()
    elif (button1['text'] == button4['text'] == button7['text'] == 'O') : button1['text'] = button4['text'] = button7['text'] = '|' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset()
    elif (button2['text'] == button5['text'] == button8['text'] == 'O') : button2['text'] = button5['text'] = button8['text'] = '|' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset()
    elif (button3['text'] == button6['text'] == button9['text'] == 'O') : button3['text'] = button6['text'] = button9['text'] = '|' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset()
    elif (button1['text'] == button5['text'] == button9['text'] == 'O') : button1['text'] = button5['text'] = button9['text'] = '\\';messagebox.showinfo('player O',' you won the GAME !!!') ; reset()
    elif (button3['text'] == button5['text'] == button7['text'] == 'O') : button3['text'] = button5['text'] = button7['text'] = '/' ;messagebox.showinfo('player O',' you won the GAME !!!') ; reset()

        #messagebox.showinfo('',' player O you won')

    
    if   (button1['text'] == button2['text'] == button3['text'] == 'X') : button1['text'] = button2['text'] = button3['text'] = '-' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button4['text'] == button5['text'] == button6['text'] == 'X') : button4['text'] = button5['text'] = button6['text'] = '-' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button7['text'] == button8['text'] == button9['text'] == 'X') : button7['text'] = button8['text'] = button9['text'] = '-' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button1['text'] == button4['text'] == button7['text'] == 'X') : button1['text'] = button4['text'] = button7['text'] = '|' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button2['text'] == button5['text'] == button8['text'] == 'X') : button2['text'] = button5['text'] = button8['text'] = '|' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button3['text'] == button6['text'] == button9['text'] == 'X') : button3['text'] = button6['text'] = button9['text'] = '|' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button1['text'] == button5['text'] == button9['text'] == 'X') : button1['text'] = button5['text'] = button9['text'] = '\\';messagebox.showinfo('player X',' you won the GAME !!!') ; reset()
    elif (button3['text'] == button5['text'] == button7['text'] == 'X') : button3['text'] = button5['text'] = button7['text'] = '/' ;messagebox.showinfo('player X',' you won the GAME !!!') ; reset()



buttons=StringVar()

button1=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button1))
button1.grid(row=0,column=0,sticky=N+W+E+S)

button2=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button2))
button2.grid(row=0,column=1,sticky=N+W+E+S)

button3=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button3))
button3.grid(row=0,column=2,sticky=N+W+E+S)

button4=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button4))
button4.grid(row=1,column=0,sticky=N+W+E+S)

button5=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button5))
button5.grid(row=1,column=1,sticky=N+W+E+S)

button6=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button6))
button6.grid(row=1,column=2,sticky=N+W+E+S)

button7=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button7))
button7.grid(row=2,column=0,sticky=N+W+E+S)

button8=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button8))
button8.grid(row=2,column=1,sticky=N+W+E+S)

button9=Button(form,text=' ',font='consolas 10 bold',height=4,width=8,command=lambda:put(button9))
button9.grid(row=2,column=2,sticky=N+W+E+S)




form.mainloop()

