# import pprint as pp
def pprint(*args):
	print("--", end=" ")
	[print(x, end=" ") for x in args]
	print()

# def bfs(node, visited, adj):
#   for node_ in visited:
#       if adj[node][node_] != 0:
#           print("cycle")
#           return 1
#       elif bfs(node_, visited+[node_], adj) != 1:
#           continue
#       else:
#           return 1

# def findCycle(node, adj, visited):
#   pprint(node, visited)
#   for i in range(len(adj)):
#       if adj[node][i] != 0:
#           if i in visited:
#               print("Cycle!")
#               return True
#           else:
#               return findCycle(i, adj, visited+[i])


for i in range(int(input())):
	n, m = [int(x) for x in input().strip().split()]
	adj = [[0 for i in range(int(n+1))] for j in range(int(n+1))]
	# adj = [[0 for i in range(int(n))] for j in range(int(n))]

	for j in range(m):
		a, b = [int(x) for x in input().strip().split()]
		# a -= 1
		# b -= 1
		# adj[a][b] = 2**(j+1)
		adj[b][a] = 2**(j+1)

	def dfs(adj, cur, tar, cost, visited, back):
		if cur == tar and cost != 0:
			return cost
		if len(visited) == len(adj):
			return 0
		back = []
		m = 1e5
		for i in range(len(adj)):
			if adj[cur][i] != 0:
				z, zback= dfs(adj, i, tar, cost+adj[cur][i], visited + [i], back + [i])
				if z != 0:
					if z < m:
						back = zback
						m = z
		return m, back

	for i in range(n):
		print(dfs(adj, i, i, 0, [], []))