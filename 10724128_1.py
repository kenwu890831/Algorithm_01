#演算法分析機側
#學號 : 10724128
#姓名 : 吳宇哲
#中原大學資訊工程系
import time
lowIndex = 0
highIndex = 0
def maxSubArray(arr, startIndex, endIndex): #Divide and Conquer
    global lowIndex1
    global highIndex1
    if startIndex >= endIndex :
       return arr[startIndex]
    midIndex = int ((startIndex+endIndex)/2) # cut
    leftMax= maxSubArray(arr,startIndex, midIndex-1)
    rightMax= maxSubArray(arr,midIndex+1, endIndex)
    crossMax = getCrossMax( arr, startIndex, midIndex, endIndex)
    return max(leftMax, rightMax, crossMax)


def getCrossMax( arr, startIndex, midIndex, endIndex) :
   global lowIndex
   global highIndex
   crossLeft = 0 
   crossRight = 0
   tempValue = 0
   lowIndex = midIndex
   highIndex = midIndex
   for i in range ( midIndex -1, startIndex-1, -1 ) : #left
      tempValue += arr[i]
      if tempValue > crossLeft :
         lowIndex = i
      crossLeft = max( tempValue, crossLeft)
   tempValue = 0
   for i in range ( midIndex+1, endIndex) : # right
      tempValue += arr[i]
      if tempValue > crossRight :
         highIndex = i
      crossRight = max( tempValue, crossRight)

   return crossRight + crossLeft + arr[midIndex]
   
print("最大子陣列問題(Maximun-Subarray Problem)")
size_arr = int(input("輸入字串大小 : (輸入 0 結束執行) : "))
while size_arr != 0 :
    arr1 = []
    arr1 = input().split()
    #print(arr1)
    arr2 = []
    if len(arr1) < size_arr :
        print("請輸入足夠數量的整數")
    else :
      start_time = time.time()
      for i in range(size_arr) :
        n = int(arr1[i])
        arr2.append(n) 
      result = maxSubArray(arr2, 0, len(arr2)-1)
      total_time = time.time() - start_time
      if arr2[len(arr2)-1] > 0 and (highIndex+2) == len(arr2):
         highIndex = highIndex+1
         result = result + arr2[len(arr2)-1]
      print("low = ", lowIndex+1, "high = ", highIndex+1, "Sum = ", result)
      print ( "run time : ",total_time )
    size_arr = int(input("輸入字串大小 : "))
print ("end")
#8
#-3 4 -1 2 1 -5 4 -2
#8
#-2 1 -3 4 -1 2 1 -5
#low =  4 high =  7 Sum =  6
#16
#13 -3 -25 20 -3 -16 -23 18 20 -7 12 -5 -22 15 -4 7
#low =  8 high =  11 Sum =  43