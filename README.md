Generate random polygons from a list of 2d points using genetic algorithm

Involves the following steps:

- Create a population and identify individual chromosomes 
- Use a roulette wheel to get a chain of points with no intersections
- Do a fitness test on the chain
- Mutate the chain if the fitness test is failed (fitness != 0)


For in-depth details, refer to method-1 of the paper: **"Use of simple polygonal chains in generating random simple polygons"**
https://link.springer.com/article/10.1007/s13160-017-0258-8
