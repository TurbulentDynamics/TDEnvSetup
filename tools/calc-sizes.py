#!/usr/bin/env python

import sys
import math
import argparse



parser = argparse.ArgumentParser(description='LBM sizing')


#TODO add nodes

parser.add_argument('-n', action="store", dest="n", default=1, type=int, help="Number of Nodes (default 1)")

#parser.add_argument('-t', action="store", dest="target", default=4, type=int, help="Target gb per core (default 4)")
parser.add_argument('-c', action="store", dest="cores", default=4, type=int, help="Number of cores available per node (default 1)")

parser.add_argument('-q', action="store", dest="q", default=19, choices=(9,19,27),  help="Number of Vectors (default 27)")
parser.add_argument('-type', action="store", dest="vtype", default=4, choices=(4,8), help="Type of Vectors, default 4  Single (4) or Double (8)")



group = parser.add_mutually_exclusive_group()
group.add_argument('-x', action="store", dest="x", type=int, help="Size of nx for cube")
group.add_argument('-tb', action="store", dest="t", type=int, help="Num of terrabytes available, returns nx: size of cube")
group.add_argument('-gb', action="store", dest="g", type=int, help="Num of gigabytes  available, returns nx: size of cube")
group.add_argument('-mb', action="store", dest="m", type=int, help="Num of megabytes  available, returns nx: size of cube")


r = parser.parse_args()

#Stoney either 640 or 320 nodes Xeon E5-2695
cores = 12 #24 threads 

print "Params Q:%s vType: %s" % (r.q, 'Single' if r.vtype ==4 else 'Double')

def sizetxt(size):

    if size/(1024**4.0) > 1:
        return "%.2ftb" % (size/(1024**4.0))

    elif size/(1024**3.0) > 1:
        return "%.2fgb" % (size/(1024**3.0))

    elif size/(1024**2.0) > 1:
        return "%.2fmb" % (size/(1024**2.0))

    else:
        return "%.2fkb" % (size/1024.0)


if r.x:
    size = r.x*r.x*r.x*r.vtype*r.q

    # ngx should be even an even number and divisable by cores
    ngx = r.n**(1/3.)

    nx_per_core = math.ceil(r.x/ngx/r.cores /2.) * 2 
    nx = nx_per_core * r.cores
    snx = ngx * nx

    size = snx*snx*snx*r.vtype*r.q

    #Output size of vector is always single (float)
    output_size = snx*snx*snx*4*3 
    output_plane_size = snx*snx*4*3 

    print "Exact sizing, total space snx:%s  per grid nx:%s" % (nx*ngx, nx)

    if r.n == 1:
        print "Need 1 node with %s available for cube of nx=%s" % (sizetxt(size), snx)
    else:
        print "Need %s nodes with %s each for cube of nx=%s (total %s)" % (r.n, sizetxt(size/r.n), snx, sizetxt(size))

    print "Size of output vectors %s, or per node %s" % (sizetxt(output_size), sizetxt(output_size/r.n))
    print "Size of output plane (slice) vectors %s, or per node %s" % (sizetxt(output_plane_size), sizetxt(output_plane_size/r.n))

    print "Works out at %s per core, with %s core%s" % (sizetxt(size/r.n/r.cores), r.cores, 's' if r.cores > 1 else '')




elif r.tb:
    print "Size of nx cube '%s' with %stb available" % ((r.t*(1024**2)/r.vtype/r.q)**(1/3.0), r.tb)
elif r.gb:
    print "Size of nx cube '%s' with %sgb available" % ((r.g*(1024**3)/r.vtype/r.q)**(1/3.0), r.gb)
elif r.mb:
    print "Size of nx cube '%s' with %smb available" % ((r.m*(1024**4)/r.vtype/r.q)**(1/3.0), r.mb)




