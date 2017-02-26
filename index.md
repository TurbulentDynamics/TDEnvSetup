# Turbulent Dynamics


This document gives some guidelines to contributing code to Turbulent Dynamics.

 * [Vector Identifiers](graphics/arrows.html) The vectors are numbered differently than usual LBM implementations
 * [Item Identifiers](graphics/cube.html) The cells in the outer shell of the lattice grid has been given an itentification.
 * [Visualisation 1000 cubes](graphics/1000.html) 

 
 
 ### Utilities
 
 * [Size Calculator](tools/calc-sizes.html) for setting dimensions of the lattice.


### Coordinate system
```
\ k,z +ve to the back
  \
   \____  i,x +ve to the right
    |
    | j,y +ve downwards
``` 

### Variable Naming Conventions
 * idx, idy, idz node identifiers
 * ngx, ngy, ngz node dimensions
 * hi, hj, hk halo identifiers
 * nx, ny, nz dimensions
 * nxb, nyb, nzb dimensions including buffer
 * i, j, k loop counters
