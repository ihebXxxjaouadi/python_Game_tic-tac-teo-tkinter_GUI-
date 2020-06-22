global t
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

reset = False
## function X_o
def play_again(YESno):
    global reset
    global winn
    if (YESno in ('Yes','y')) : 
        winn = False
        reset = True
        if_play()        
    else :
         print('End Game')
    
def reset_tic():
    for i in range(1,9):
        t[i]=' '
        
    l1=[t[1],'|',t[2],'|',t[3]]
    l2=['-','+','-','+','-','-']
    l3=[t[4],'|',t[5],'|',t[6]]
    l4=['-','+','-','+','-','-']
    l5=[t[7],'|',t[8],'|',t[9]]
    
    print(l1[0],l1[1],l1[2],l1[3],l1[4])
    print(l2[0],l2[1],l2[2],l2[3],l2[4])
    print(l3[0],l3[1],l3[2],l3[3],l3[4])
    print(l4[0],l4[1],l4[2],l4[3],l4[4])
    print(l5[0],l5[1],l5[2],l5[3],l5[4])



winn=False
def Winner(numb):
    global winn
    if numb=='1':print('\n \n \n-_-_-_-_-_-_-_-_-_-_-');print('>>>>>>>player X you won the game<<<<<<<')  ;print('-_-_-_-_-_-_-_-_-_-_-'); winn= True
    elif numb=='2':print('\n \n \n-_-_-_-_-_-_-_-_-_-_-');print('>>>>>>>player O you won the game<<<<<<<');print('-_-_-_-_-_-_-_-_-_-_-'); winn= True
    elif numb=='0':print('\n \n \n-_-_-_-_-_-_-_-_-_-_-');print('no one win') ; print('-_-_-_-_-_-_-_-_-_-_-');winn= True
    else :print('=======')
        


click=True


def X_o(pos):
    global click
    
    
    
    if click == True : 
        t[pos]='X'
        click=False
        
        
        
    else : 
        t[pos]='O'
        click=True
        

        


    if   (t[1]==t[2]==t[3]=='X'):t[1]=t[2]=t[3]='-' ; Winner('1') ; score(1,0)
    elif (t[4]==t[5]==t[6]=='X'):t[4]=t[5]=t[6]='-' ; Winner('1') ; score(1,0)
    elif (t[7]==t[8]==t[9]=='X'):t[7]=t[8]=t[9]='-' ; Winner('1') ; score(1,0)
    elif (t[1]==t[4]==t[7]=='X'):t[1]=t[4]=t[7]='-' ; Winner('1') ; score(1,0)
    elif (t[2]==t[5]==t[8]=='X'):t[2]=t[5]=t[8]='-' ; Winner('1') ; score(1,0)
    elif (t[3]==t[6]==t[9]=='X'):t[3]=t[6]=t[9]='-' ; Winner('1') ; score(1,0)
    elif (t[7]==t[8]==t[9]=='X'):t[7]=t[8]=t[9]='-' ; Winner('1') ; score(1,0)
    elif (t[1]==t[5]==t[9]=='X'):t[1]=t[5]=t[9]='\\'; Winner('1') ; score(1,0)
    elif (t[3]==t[5]==t[8]=='X'):t[3]=t[5]=t[7]='/' ; Winner('1') ; score(1,0)
    
    
    if   (t[1]==t[2]==t[3]=='O'):t[1]=t[2]=t[3]='-' ; Winner('2') ; score(0,1)
    elif (t[4]==t[5]==t[6]=='O'):t[4]=t[5]=t[6]='-' ; Winner('2') ; score(0,1)
    elif (t[7]==t[8]==t[9]=='O'):t[7]=t[8]=t[9]='-' ; Winner('2') ; score(0,1)
    elif (t[1]==t[4]==t[7]=='O'):t[1]=t[4]=t[7]='-' ; Winner('2') ; score(0,1)
    elif (t[2]==t[5]==t[8]=='O'):t[2]=t[5]=t[8]='-' ; Winner('2') ; score(0,1)
    elif (t[3]==t[6]==t[9]=='O'):t[3]=t[6]=t[9]='-' ; Winner('2') ; score(0,1)
    elif (t[7]==t[8]==t[9]=='O'):t[7]=t[8]=t[9]='-' ; Winner('2') ; score(0,1)
    elif (t[1]==t[5]==t[9]=='O'):t[1]=t[5]=t[9]='\\'; Winner('2') ; score(0,1)
    elif (t[3]==t[5]==t[8]=='O'):t[3]=t[5]=t[7]='/' ; Winner('2') ; score(0,1)
    
    if (t[1]==t[2]==t[3]==t[4]==t[5]==t[6]==t[7]==t[8]==t[9]!=' ') : Winner('0')
  
  
call=True    
def X_player():
    global call
    global choise
    if (call==True):choise=input('select empty place >>>'+str(player1)+'<<< \n-->' );call=False
    else : choise=input('select empty place >>>'+str(player2)+'<<< \n-->' );call=True
    

# main program
    
    
    
    

def play():

    global l1,l2,l3,l4,l5
    global choise
    
    while winn==False  :
        
        
        X_player()
        
        
        
        statement=False
        while (statement== False):
            if   ( choise.isnumeric() == False ):choise=input('\nthe place is not alphabetiq \n select empty place. \n-->') 
            elif (int(choise) not in range(1,10)) : choise=input('\nbetween 1 and 9 \nselect empty place. \n-->') 
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
    
    
def if_play():
    global YESno    
      
    if (winn==False ) and (reset==False):
        print_tic()
        play()
    if (winn==False ) and (reset==True):
        reset_tic()
    
        
        
        play()   
    else : print('_-_-_-_')
        
        
    if (winn==True) :
        YESno=input('\n \n \npress  "No/n"pour quitter \npress "Yes/y" for play another part. \n--> ' )
        statement=False
        while (statement==False):
            if YESno.isalpha()==False  : YESno=input('\npress  "No/n"for cut the game\npress "Yes/y" for play another part. \n--')
            elif (YESno not in ('No','n','Yes','y')) : YESno=input('press  "No/n"pour quitter \npress "Yes/y" for play another part. \n-- ')
            else : statement=True
        play_again(YESno)
            
            
            
    else : print('+++++')
    
    
    
    
def enter_players():
    
    global player1,player2  
    
    player1=input('enter your name player1 >>>X<<< . \n-->')
    statement = False
    while statement == False :
        if player1=='' and player1.strip()=='' :player1=input('is empty \nenter your name . \n-->')
        else : statement = True
    
    
    player2=input('enter your name player  >>>O<<< . \n-->')
       
    statement = False
    while statement == False :
        if player2=='' and player2.strip()=='' :player2=input('is empty \nenter your name . \n-->')
        else : statement = True    
s1=0
s2=0               
def score (x,y):
    global s1,s2

    s1+=x
    s2+=y
    print('\n '+player1+'    '+player2)
    print('========= =========')
    print('    '+str(s1)+'    |    '+str(s2)+'    ')    
    print('========= =========\n')
    print('_-_-_-_-_-_-_-_-___-_-__-_-_-_')
    
enter_players()
if_play()    
  
            


   
    
            




    
    

