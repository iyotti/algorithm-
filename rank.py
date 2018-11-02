#値が大きいほど順位が高い
def rank(ary):
	rank = [0] * len(ary)
	for i in range(len(ary)):
		for j in range(len(ary)):
			if ary[i] < ary[j]:
				rank[i]+=1
	return rank

score = list(map(int,input().split()))
print(rank(score))