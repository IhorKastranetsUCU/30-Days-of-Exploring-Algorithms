from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event_arr = []
        for num , par , to in trips:
            event_arr.append( (par, 1 , num)  )
            event_arr.append( (to , -1 , num) )

        curr_cap = capacity

        event_arr = sorted(event_arr , key = lambda x : (x[0] , x[1] , x[2]) )
        print(event_arr)
        for x , type , num in event_arr:
            if type == 1:
                curr_cap -= num
            else:
                curr_cap += num

            if curr_cap < 0:
                return False

        return True

if __name__ == "__main__":
    print(Solution.carPooling(Solution , [[2,1,5],[3,3,7]] , 4))
