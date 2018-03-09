size(400,400);
background(50);
Ncols = width;
Nrows = height;

# Set up 2D array
myArray = [[0]*Ncols]*Nrows;

for i  in range(0,Ncols,20):
    for j in range(0,Nrows,20):
        myArray[i][j] = int(random(255));
        #stroke(myArray[i][j]);
        stroke(20)
        #fill(myArray[i][j]);
        fill(255)
        triangle(2,Ncols-30*j,10*i,10*i+j,i,i+4);
        
        
save("tri_stripe_14.tif")