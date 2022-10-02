'''
name : Abhinav Tiwari



  Python program to triple all numbers of a given
     list of integers. Use Python map.

sample list: [1, 2, 3, 4, 5, 6, 7]

'''




lst = [1,2,3,4,5,6,7]

res = list(map(lambda lst:lst*3,lst))
print(res)