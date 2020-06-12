t=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

l1=[t[1],'|',t[2],'|',t[3]]
l2=['-','+','-','+','-','-']
l3=[t[4],'|',t[5],'|',t[6]]
l4=['-','+','-','+','-','-']
l5=[t[7],'|',t[8],'|',t[9]]

def print_tic():
    
    print(l1[0],l1[1],l1[2],l1[3],l1[4])
    print(l2[0],l2[1],l2[2],l2[3],l2[4])
    print(l3[0],l3[1],l3[2],l3[3],l3[4])
    print(l4[0],l4[1],l4[2],l4[3],l4[4])
    print(l5[0],l5[1],l5[2],l5[3],l5[4])

def play_again(choise):
    global winn
    if (choise =='1') : 
        reset()
        winn = False
    else :
         print('End Game')
    
def reset():
    for i in range(1,9):
        t[i]=' '

click=True
## function X_o
winn=False
def Winner(numb):
    global winn
    if numb=='1':print('>>>>>>>player X you won the game<<<<<<<')  ; winn= True
    elif numb=='2':print('>>>>>>>player O you won the game<<<<<<<'); winn= True
    elif numb=='0':print('no one win') ; winn= True
    else :print('=======')
        



def X_o(pos):
    global click
    
  
    if click == True : 
        t[pos]='X'
        click=False
        
        
    else : 
        t[pos]='O'
        click=True
        


    if   (t[1]==t[2]==t[3]=='X'):t[1]=t[2]=t[3]='-' ; Winner('1') 
    elif (t[4]==t[5]==t[6]=='X'):t[4]=t[5]=t[6]='-' ; Winner('1') 
    elif (t[7]==t[8]==t[9]=='X'):t[7]=t[8]=t[9]='-' ; Winner('1')
    elif (t[1]==t[4]==t[7]=='X'):t[1]=t[4]=t[7]='|' ; Winner('1')
    elif (t[2]==t[5]==t[8]=='X'):t[2]=t[5]=t[8]='|' ; Winner('1')
    elif (t[3]==t[6]==t[9]=='X'):t[3]=t[6]=t[9]='|' ; Winner('1')
    elif (t[7]==t[8]==t[9]=='X'):t[7]=t[8]=t[9]='-' ; Winner('1')
    elif (t[1]==t[5]==t[9]=='X'):t[1]=t[5]=t[9]='\\'; Winner('1')
    elif (t[3]==t[5]==t[8]=='X'):t[3]=t[5]=t[8]='/' ; Winner('1')
    
    
    if   (t[1]==t[2]==t[3]=='O'):t[1]=t[2]=t[3]='-' ; Winner('2')
    elif (t[4]==t[5]==t[6]=='O'):t[4]=t[5]=t[6]='-' ; Winner('2')
    elif (t[7]==t[8]==t[9]=='O'):t[7]=t[8]=t[9]='-' ; Winner('2')
    elif (t[1]==t[4]==t[7]=='O'):t[1]=t[4]=t[7]='|' ; Winner('2')
    elif (t[2]==t[5]==t[8]=='O'):t[2]=t[5]=t[8]='|' ; Winner('2')
    elif (t[3]==t[6]==t[9]=='O'):t[3]=t[6]=t[9]='|' ; Winner('2')
    elif (t[7]==t[8]==t[9]=='O'):t[7]=t[8]=t[9]='-' ; Winner('2')
    elif (t[1]==t[5]==t[9]=='O'):t[1]=t[5]=t[9]='\\'; Winner('2')
    elif (t[3]==t[5]==t[8]=='O'):t[3]=t[5]=t[8]='/' ; Winner('2')
    
    if (t[1]==t[2]==t[3]==t[4]==t[5]==t[6]==t[7]==t[8]==t[9]!=' ') : Winner('0')
    


# main program
    
if (winn==False ):
    print_tic()

    
    while winn==False  :
        choise=input('select empty spalce for put X.')
        
        
        statement=False
        while (statement== False):
            if   ( choise.isalpha() == True ) :
                choise=input('\nthe place is not alphabetiq \n select empty spalce for put X.') 
            elif (int(choise) not in range(1,10)) : choise=input('\nbetween 1 and 9 \nselect empty spalce for put X.') 
            else : statement=True
        c=int(choise)
        if (t[c]==' '):
                
                
            X_o(c)
                
            l1=[t[1],'|',t[2],'|',t[3]]
            l2=['-','+','-','+','-','-']
            l3=[t[4],'|',t[5],'|',t[6]]
            l4=['-','+','-','+','-','-']
            l5=[t[7],'|',t[8],'|',t[9]]     
    
            
            print_tic()     
    
    
    
    
if (winn==True) :
    
    
    choise=input('press any number pour quitter \npress 1 for play another part ' )
    play_again(choise)
    
    
    
else : print('+++++')




            


   
    
            




    
    

