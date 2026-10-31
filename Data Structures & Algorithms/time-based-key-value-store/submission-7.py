class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        temp = self.d[key]
        if(len(temp) == 0):
            return ""
        l = 0
        r = len(temp) - 1
        mid = -1
        while(l <= r):
            mid = (l+r)//2
            if(temp[mid][0] == timestamp):
                return temp[mid][1]
            
            elif(temp[mid][0] > timestamp):
                r = mid - 1
            else:
                if(mid < len(temp)-1 and temp[mid+1][0]>timestamp):
                    return temp[mid][1]
                l = mid + 1
        if(temp[mid][0] < timestamp):
            return temp[mid][1]
        else:
            return ""
        
        
