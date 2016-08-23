

# VARIABLE NAMING CONVENTION
size_*  The byte size of malloc'able arrays
dim_*   The overall size of malloc'able arrays

grid    Any reference to the array per node ie, nx
space   Any reference to the total grids  ie snx



snx                 Size of the space in cells in the x direction
ngx                 Number of nodes in cells in the x direction
nx = snx/ngx + 2    Size of the grid (node) in cells in the x direction



dim_N = nx+2 * ny+2 * nz+2 

  0  1  2  3   nx-2  nx-1  nx   nx+1
  |  |  |            |     |      |
  h  e  face   or   edge   e      h 



for (i=0; i<nx; i++)
for (j=0; j<ny; j++)
for (k=0; k<nz; k++)

for (x=0; x<ngx; x++)
for (y=0; y<ngy; y++)
for (z=0; z<ngz; z++)








