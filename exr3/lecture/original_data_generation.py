## original professor function

jump = lambda drift, stdev: int(np.random.normal(drift,stdev))  # center, stdev
np.random.seed(12345)
# original
# pattern parameters: Z=nr of steps, A=amplitude
Z=12
A=500

# number of data samples
N=10000
# size of each sample of the timeseries
L=60
# step parameters: introduce small positive bias 
DX = 50
bias = 5

#def generate():
y = [0] * N
x = [[0] * L for i in range(N)]
for i in range(N):
    if i>0:
        x[i][0] = x[i-1][-1] + jump(bias,DX)
    
    for j in range(1,L):
        x[i][j] = x[i][j-1] + jump(bias,DX)
        
    y[i] = i%3 
    ##y[i] = random.randint(0,2)
    if y[i]>0:
        j0 = np.random.randint(0,L-1-Z)
        ###print(i,j0,j1)
        sign = 3-2*y[i]
        for j in range(Z):
            x[i][j0+j] += sign*pattern(j,Z,A)
            
for i in range(min(3,N)):
    print(x[i],y[i])
    
    

Show_data(x,L,"original data")