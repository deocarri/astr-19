import numpy as np 

def main():
	x = 0
	x = np.linspace(0,2*np.pi,1000)
	y = np.linspace(0,np.sin(2*np.pi),1000)
	end = np.column_stack((x,y))
	print(end)

if __name__ == '__main__':
	main()

#0,1,2,3,4,5,6,..(1000 terms)..,2pi
#sin(0), ..(1000 terms)..,sin(2pi)