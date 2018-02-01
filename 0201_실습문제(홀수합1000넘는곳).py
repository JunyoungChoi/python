hap,num=0,0
for a in range(1,1001,2):
  if hap >1000:
    print("1부터 1000까지의 홀수의 합중 최초로 1000이 넘는 위치 : %d"%(a-2))
    break
  hap+=a
