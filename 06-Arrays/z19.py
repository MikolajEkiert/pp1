import random
arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr5 = [i*2 for i in range(1,10)]
arr7 = [[] for i in range(5)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr10=[4,3,0]
arr11=[0 for i in range(1,16)]
arr12=[random.randint(0,1) for i in range(21)]
print(arr1,arr2,arr3,arr4,arr5,"\n",arr6,arr7,arr8,arr9,"\n",arr10,"\n",arr11)
print(arr12)
arr13=[[False for i in range(5)]for i in range(2)]
print(arr13)