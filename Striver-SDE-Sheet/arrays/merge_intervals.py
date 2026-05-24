class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def custom_sort(ele):
            return ele[0]
        sorted_list = sorted(intervals, key=custom_sort)
        #print(sorted_list)
        first_ele=None
        second_ele=None
        ret_list = [sorted_list[0]]
        for ele in sorted_list[1:]:
            if ele[0]<=ret_list[-1][1]:
                ret_list[-1][1]=max(ele[1],ret_list[-1][1])
            else:
                ret_list.append(ele)
        return ret_list