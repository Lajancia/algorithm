num, mx=map(int, input().split())
li=list(map(int,input().split()))
# print(li)
s=mx
temp=0

for i in range(num-2):
		for j in range(i+1,num-1):
			for k in range(j+1,num):
				if(li[i]+li[j]+li[k]<=mx):
					if(mx-(li[i]+li[j]+li[k])<s):
						# print(li[i],end='+')
						# print(li[j],end='+')
						# print(li[k],end='=')
						temp=li[i]+li[j]+li[k]
						# print(temp)
						s=mx-(li[i]+li[j]+li[k])
print(temp)
