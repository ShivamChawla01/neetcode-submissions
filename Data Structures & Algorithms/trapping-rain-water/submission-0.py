class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        runningVolume = 0
        maxHeight = 0
        i = 0
        while(i<len(height)):
            if(height[i]>=maxHeight):
                total+=runningVolume
                runningVolume = 0
                maxHeight = height[i]
            else:
                if(height[i]<=height[i-1]):
                    runningVolume += (maxHeight - height[i])
                else:
                    total += (height[i]-height[i-1])
                    runningVolume += (maxHeight - height[i])
                    runningVolume-=(height[i]-height[i-1])

            i+=1
        return total
        