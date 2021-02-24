def d():
		a=input()
		count=0
		
		if(len(a)>=3):
			
			for i in range(1,10):
				for j in range(0,10):
					if(i+2*j<=9):
						if(111*i+12*j<=int(a)):
							count=count+1
				for j in range(1,10):
					if(i-2*j>=0):
						if(111*i-12*j<=int(a)):
							count=count+1
			for i in range(1,100):
				count=count+1
			print(count)
			
		elif len(a)>=2:
			
			for i in range(1,int(a)+1):
				count=count+1
			print(count)
			
		elif len(a)>=1:
			
			for i in range(1,int(a)+1):
				count=count+1
			print(count)
		
d()
