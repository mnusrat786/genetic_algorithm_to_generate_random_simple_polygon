# genetic_algorithm_to_generate_random_simple_polygon
Libraries
I have imported shapely library because I have to create a polygon from input points that’s why I imported shapely module. 
For arrays I have used Numpy library and for plotting the graph I have used Matplotlib library.
To generate random numbers I have used random library.
There are 4 steps of genetic algorithm
Population Generation
First I have generated population by taking multiple points named p0,p1,p2,p3,p4,p5 and p6 respectively. I used random. shuffle function to shuffle the chromosomes(p0,p1,p2,p3,p4,p5,p6)
Chromosomes
A chromosome is an individual in a population. Here p0,p1,p2,p3,p4,p5,p6 are 7 chromosomes in a population. Plot chain function passes lists of points 2d lists in its argument and plots the chain with the help of the points. 
Check intersect lines function finds if l1 and l2 are intersecting or not. I have used a check which makes sure that it does not include end point intersection of lines in check
intersection function.
Calculate intersections function overall calculates intersections of all the lines instead of finding it one by one separately as we did above in the check intersect lines function.
Roulette Wheel Function
Get chain (list of points) function shuffles the points until it gets a chain with no intersection.
Fitness Function
I have used a fitness function get fitness (list of points) because it checks if we are getting a polygon without intersection or not. If we get a polygon with intersection then we have to use mutation step.
Mutation Function
I have used a mutation function named (modify chain) it gets rid of the intersection problem of the polygonal chain when we join the starting and the end points.

