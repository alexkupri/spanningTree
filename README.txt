Purpose
This prototype demonstrates the algorithm of building of minimal spanning tree.
In some conditions, in some sence it runs faster than widely known algorithms.

Not exploring every edge
Assume we have N objects, and a function dist(i,j) which returns the distance between i-th and j-th objects. 
The conventional alogorithms calculate the distance between each pair of objects, thus exploring O(n*n) edjes.
However, the function dist can be expensive by itself (assume the objects are some strings or DNA sequences, and dist is a Levenstein distance). 
It would be beneficial to build minimal spanning tree exactly, but call dist function less than O(n*n) times.
(Minimal spanning tree can be used for clusterisation algorithms of arbitrary objects.)

Skipping of calculation of some edges
We can skip calculation of distances between some pairs of objects by using the triangle inequality.
Assume we have built some subsets of objects A and B, the subset A contains the object A_capitol, the subset B contains the object B_capitol.
Assume the distance between each element of region A and capitol of region A is smaller than radius_A.
For each obj belonging A: dist(obj,capitol_A)<=radius_A
The same for region B.
Then for each objA belonging A and each objB belongin B: dist(objA, objB) >= dist(capitol_A,capitol_B) - radius_A - radiusB
So we have lower estimation of distance between each pair of objects in region A and region B.
If we have already built some approximation of spanning tree (I omit some details here) which has the minimal edge of length cur, and the lower estimation of distance between each pair of objects in regions A and B is greater than cur, then we can skip even the calculation of distances between each pair of objects in regions A and B.
The regions correspond to the class RegionalTree in the code.
Skipping of comparison between the whole regions is done in the function Interconnect.

What the code does
The code demonstrates and counts only the number of calls to dist function.
The code is fairly inoptimal in other places (it can be optimized further, but it is a prototype showing only a particular property of the algorithm).
The class CartesianModel has the function dist and the function nVertices (besides constructor).
In the experiment, this class counts calls to its dist function.
It returns the distance between points in n-dimentional space.
The experiments show that for 2-dimentional space, for example, for 1024 objects, the function dist is called roughly 39 000 times, while conventional algorithms which calculate distance between each pair would call it roughly 500 000 times.
To run it, call:
python test_Main.py
 
Further notes
The performance of the algorithm highly depends on the nature of the input data.
It is possible to construct such input data, that the algorithm would need to expore each edge of the task (worst case).
Assume that dist(i,j)=a for each i!=j, e.g., n-1-dimentional regular thetrahedron for n objects.
The experiments with uniformely distributed points in n-dimentional cube show, that number of calls to dist function grows with grow of n. 
