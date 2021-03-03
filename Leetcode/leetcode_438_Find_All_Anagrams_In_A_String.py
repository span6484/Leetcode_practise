# git branch new_branch_name 然后, git checkout new_branch_name
# 等价于
# git checkout -b new_branch_name


# git branch -d  branch_name -- 用来删分支

from collections import Counter

class Solution:

    def create_dict(self, string: str):
        window = dict()
        for ch in string:
            if ch not in window:
                window[ch] = 0
            window[ch] += 1
        return window


    def findAnagrams(self, s: str, p: str):
        """
        如何只用dict不用Counter来解决这个问题
        """
        target = self.create_dict(p)
        result = []
        if len(s) < len(p):
            return []

        window_dict = self.create_dict(s[0:len(p)])
        i = len(p)
        while True:
            # 0. check sliding window
            if window_dict == target:
                result.append(i-len(p))

            if i == len(s):
                break

            # 1. slide, add most right element into window
            add_elem = s[i]
            if add_elem not in window_dict:
                window_dict[add_elem] = 0
            window_dict[add_elem] += 1

            # 2. slide, delete most left element out of window
            del_elem = s[i-len(p)]
            window_dict[del_elem]-=1
            if window_dict[del_elem] == 0:
                del window_dict[del_elem]
            i += 1
                
        return result
# git branch new_branch_name 然后, git checkout new_branch_name
# 等价于
# git checkout -b new_branch_name


# git branch -d  branch_name -- 用来删分支

from collections import Counter

class Solution:

    def create_dict(self, string: str):
        window = dict()
        for ch in string:
            if ch not in window:
                window[ch] = 0
            window[ch] += 1
        return window


    def findAnagrams(self, s: str, p: str):
        """
        如何只用dict不用Counter来解决这个问题
        """
        target = self.create_dict(p)
        result = []
        if len(s) < len(p):
            return []

        window_dict = self.create_dict(s[0:len(p)])
        i = len(p)
        while True:
            # 0. check sliding window
            if window_dict == target:
                result.append(i-len(p))

            if i == len(s):
                break

            # 1. slide, add most right element into window
            add_elem = s[i]
            if add_elem not in window_dict:
                window_dict[add_elem] = 0
            window_dict[add_elem] += 1

            # 2. slide, delete most left element out of window
            del_elem = s[i-len(p)]
            window_dict[del_elem]-=1
            if window_dict[del_elem] == 0:
                del window_dict[del_elem]
            i += 1
                
        return result


if __name__ == "__main__":
    s = 'abcaccabc'
    p = 'abc'
    res = Solution().findAnagrams(s, p)
    for i in res:
        print(i, s[i:i+len(p)])