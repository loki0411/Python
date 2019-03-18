

def hanoi( a, b, c, n ):
  '递归方法解汉诺塔'
  if n==1:
    print('n=1');print( a,'->',c )
    
  else:    
    print( 'a,c,b,n-1:',a,c,b,n-1 );hanoi( a,c,b,n-1 )
    print( a,'->',c )
    print( 'b,a,c,n-1:',b,a,c,n-1);hanoi( b,a,c,n-1 )


hanoi('盘1','盘2','盘3',4)



