#Q5 Given are two one-dimensional arrays A and B which are sorted in
#  ascending order. Write a program to merge them into a single sorted array C
#that contains every item from arrays A and B, in ascending order. [List]
import numpy as np
a = np.array([[1,5,9],[2,6,10]])
b = np.array([[3,7,11],[4,8,12]])
print(np.concatenate((a,b), axis=0))
