size(200,200);
Ncols = width;
Nrows = height;
background(80)

# Set up 2D array
myArray = [[0]*Ncols]*Nrows;

for i  in range(0,Ncols,20):
    for j in range(0,Nrows,20):
        myArray[i][j] = int(random(255));
        stroke(200);
        rect(i,j,20,20)

stroke(20);  
beginShape(TRIANGLE_STRIP);
vertex(10, 75);
vertex(40, 20);
vertex(50, 75);
vertex(60, 20);
vertex(70, 75);
vertex(130, 20);
vertex(90, 75);
endShape();

beginShape();
vertex(130, 120);
vertex(150, 120);
vertex(150, 140);
vertex(170, 140);
vertex(170, 160);
vertex(130, 160);
endShape(CLOSE);

beginShape(TRIANGLE_FAN);
vertex(57.5, 150);
vertex(57.5, 115); 
vertex(92, 150); 
vertex(57.5, 185); 
vertex(22, 150); 
vertex(57.5, 115); 
endShape();

