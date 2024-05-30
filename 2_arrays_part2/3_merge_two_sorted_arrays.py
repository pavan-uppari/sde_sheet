#Check another approach - Using gap method

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        1. Iterate throught both the arrays, if array2 element is less than array1 element,
            then pop last item(zero) from arr1 and insert arr2 item into arr1 at that index
        2. Make a count of number of zeros removed in that process
        3. At the end of that iteration, there might be some large elements left over in arr2.
        4. Insert them into arr1
        """
        i = j = 0
        zeroes_removed = 0
        while i< m+n and j<n:
            if nums1[i] > nums2[j]:
                zeroes_removed += 1
                nums1.pop()
                nums1.insert(i, nums2[j])
                j+=1
            i+=1
        for i in range(m+zeroes_removed, m+n):
            nums1[i] = nums2[j]
            j+=1
    
        