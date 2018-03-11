size(400,400);
Ncols = width;
Nrows = height;
background(80)
myArray = [[0]*Ncols]*Nrows;

#set up a dot grid background
for i  in range(0,Ncols,20):
    for j in range(0,Nrows,20):
        myArray[i][j] = int(random(255));
        stroke(200);
        point(i,j)
    

#first square at the origin
stroke(100), fill(100); rect(0,0,40,40);

#second square in darker colour rotated 45. Rotation command changes the way the coordinates are understood for all subsequent commands.
stroke(20); fill(20); rotate(radians(45)); rect(0,0,40,40);

#to show this - third square is also rotated relative to the window 
stroke(150); fill(150); rect(0,0,20,20); 

#fourth quare is translated, but also on the rotated grid. 
stroke(0); translate(100,-100); rect(0,0,40,40)

#put the rotation back to normal! - why is translate not going back to 0,0?
rotate(radians(-45)); translate(-100,100);rect(250,50,40,40)

#for loops still seem more fun & efficient than translate:
for i in range(0,Ncols,10):
    print(i)
    stroke(255); fill(255);
    ellipse(i,0,15,15)
    ellipse(0,i,15,15)
    
rotate(radians(45));
        
for i in range(0,2*Ncols,15):
    print(i)
    stroke(255); fill(255);
    ellipse(i,0,15,15)
    ellipse(0,i,15,15)  

translate(-40,-100);
  
for i in range(0,2*Ncols,15):
    stroke(255); fill(255);
    ellipse(i,0,15,15)
    ellipse(0,i,15,15)    
    
for i in range(0,600,5):
    stroke(i);
    line(i,10,i,40)
