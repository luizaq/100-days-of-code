def direita():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_on_right():
        direita()
    if front_is_clear():
        move()
    if not front_is_clear() and wall_on_right():
        turn_left()
   
    #if not front_is_clear():
        #direita()
        #move()
           
  
     
