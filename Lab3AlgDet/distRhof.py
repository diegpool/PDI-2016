def distRhot(u,b):
	import math
	sum = (u[0]-b[0])**2 +(u[1]-b[1])**2 +(u[2]-b[2])**2 + (u[3]-b[3])**2 + (u[4]-b[4])**2 +(u[5]-b[5])**2 +(u[6]-b[6])**2 +(u[7]-b[7])**2 +(u[8]-b[8])**2
	result = math.sqrt(sum)
	return result
