# QuickSelect
This code is a an implementation of QuickSelect Algorithm in Python
QuickSelect is a very similar algorithm to QuickSort as both of them are Divide&Conqure algorithms and both of them use Partition to divide the array.

The code contains two functions:
1. Partition: (Same as in QuickSort) This function take an array (a) and two integers for the beginning and the end of the array (l, r) and choose the last element of the array as a pivot, then it sorts the array putting the pivot in the right place, so that all the elements that are smaller than the pivot on left of it and all elements that are larger than the pivot on the right of it, then returns the index of the pivot.

2. kthlargest: it takes an array (a) and an integer (k) and returns the k'th largest element of the array by splitting the array using Partition and calling itself recuresivly with the suitable argument (subarray and modified k).
