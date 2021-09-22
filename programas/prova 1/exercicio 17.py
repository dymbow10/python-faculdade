Divine=Limit=0
while Limit<4:
	soma=0
	Divine+=1
	for i in range(1,Divine):
		if Divine % i == 0:
			soma+=i
	if Divine == soma:
		Limit+=1
		print Divine
		
