import random

objects = ['rock','paper','scissor']
win = [('rock','scissor'),('paper','rock'),('scissor','paper')]

while True:
    player = input("rock[1], paper[2], scissor[3] Quit[0] ?")
    if player == "0":
        break
    player = objects[int(player)-1]
    cpu = objects[random.randint(0,2)]
    print (player, cpu)
    if ((player,cpu) in win):
        print ("Player wins")
    else:
        if ((cpu, player) in win):
         print ("CPU wins")
        else:
         print ("Tie")
         
       
    
        
            
    
        

            
                
                    

                    
          

                
    

            
                



                
            
            
    
    
        
    
  
  
  
      
          
      
      

  
  
  
      
  