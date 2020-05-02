# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        first,last=1,n
        
        if n==1:
            return 1
        
        while first<=last:
            mid=(first+last)//2
            if isBadVersion(first):
                return first
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                first=first+1
                last=mid
            else:
                first = mid+1
        return first
