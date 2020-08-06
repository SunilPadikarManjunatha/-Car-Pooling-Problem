class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        pool = {}
        
        for trip in trips:
            start = trip[1]
            end = trip[2]
            while(start<end):
                if start in pool:
                    pool[start] += trip[0]
                else:
                    pool[start] = trip[0]
                if pool[start] > capacity: return False
                start +=1

        return True