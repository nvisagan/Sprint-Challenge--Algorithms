#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is an O(n). The first while is an O(n) and then O(1). Multiply those gives
you O(n)


b) This is a tricky one, but I believe its O(n), the for loop start with O(n) and then has O(2n)
but ultimately when you drop the constants it is just O(n)

c) The return recursive function on the bottom is called by linear time so O(n)

## Exercise II

I would use a divide and conquer algorithm, like merge sort. You can start by dividing n in half and then dropping the egg from the middle floor. If it breaks, then n is high and dont need to test the higher n. I can then divide the lower floors in half and do the process again. If the egg doesn't break from the middle floor, I can eliminate the lower floors and divide the higher floors in half and do same thing from the new middle. I do this until I reach the highest floor an egg can drop without breaking. This will be a O(n log n) 
