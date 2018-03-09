size(400,400);
Ncols = width;
Nrows = height;

# Declare 2D array
myArray = [[0]*Ncols]*Nrows;

for i  in range(0,Ncols):
    for j in range(0,Nrows):
        myArray[i][j] = int(random(255));
        stroke(myArray[i][j]);
        point(i,j);

save("greyscale_grid.tif")




