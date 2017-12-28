import pandas as pd 

class  estimate:

	"""准确率评估"""
	def Score(self,M,T):
		score = []
		y = T['type']
		x = T.drop(['id','type'],1)
		x_test = x.values
		y_test = y.values
		for i in range(3):
			score.append(M[i].score(x_test,y_test))
		return score	
		
