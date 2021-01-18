def hanoi(n,start,mid,end):
		if(n==1):
			#하나 남을 경우, 바로 마지막으로 이동
			print(start, end)
		else:
			#두개 이상 남을 경우
			# 1. 시작의 조각을 중간으로 보냄
			# 2. 중간의 조각을 시작부분으로 보냄
			hanoi(n-1,start,end,mid)
			print(start, end)
			hanoi(n-1,mid,start,end)

num=int(input())
print(2**num-1)
hanoi(num,1,2,3)
