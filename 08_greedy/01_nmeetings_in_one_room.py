class Solution:
    def maximumMeetings(self,start,end):
        
        start, end = zip(*sorted(zip(start, end), key=lambda x:x[1]))
        
        res = 0
        prev_end = float("-inf")
        for a,b in zip(start, end):
            if a > prev_end:
                prev_end = b
                res += 1
        return res