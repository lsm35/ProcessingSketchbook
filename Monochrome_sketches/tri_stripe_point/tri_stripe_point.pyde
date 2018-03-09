size(400,400);
background(20);
Ncols = width;
Nrows = height;

# Set up 2D array
myArray = [[0]*Ncols]*Nrows;

for i  in range(0,Ncols,20):
    for j in range(0,Nrows,20):
        myArray[i][j] = int(random(255));
        stroke(myArray[i][j]);
        fill(myArray[i][j]);
        triangle(i,20,i,i,i,i);
        point(i,j)

save("tri_stripe_point.tif")