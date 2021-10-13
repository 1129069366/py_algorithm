class Solution(object):
    # 1.分发饼干    (1).小饼干满足小胃口
    def findContentChildren(self, g, s):
        """
        :type g: List[int]   小孩胃口  此长度表示小孩数量
        :type s: List[int]   饼干数量
        :rtype: int
        """
        s.sort()
        g.sort()
        res = 0
        for i in s:
            if res < len(s) and i >= g[res]:
                res += 1

        return res






if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren_2([1, 2, 3], [1, 2]))