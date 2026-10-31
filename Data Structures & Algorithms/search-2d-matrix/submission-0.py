class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        while(t<=b):
            mid = (t + b)//2
            if(matrix[mid][0] == target):
                return True
            elif(matrix[mid][0]<target):
                t = mid + 1
            else:
                b = mid - 1
        l = 0
        r = len(matrix[0])-1
        print(t)
        while(l<=r):
            mid = (l+r)//2
            if(matrix[t-1][mid] == target):
                return True
            elif(matrix[t-1][mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return False

        