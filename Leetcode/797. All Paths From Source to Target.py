from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # print(graph)
        def dfs(s, t, cp, g, gp):
            # print("--", s,t,cp)
            if t in g[s]:
                gp.append(cp+[t])
            arr = [s_ for s_ in g[s] if (s_ not in cp) and (s != t)]
            [dfs(s_, t, cp+[s_], g, gp) for s_ in arr]
        gp = []
        dfs(0, len(graph)-1, [], graph, gp)
        return [[0]+gp_ for gp_ in gp]


s = Solution()
print(s.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))
print("Answer: [[0,1,3],[0,2,3]]")
print(s.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
print("Answer: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]")
