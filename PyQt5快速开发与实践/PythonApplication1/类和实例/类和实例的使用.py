

class class1:
  ccnt = 0
  cname = 'name:class1'

  def  __init__( self, name ):
    self.cname = name    
    print('类的变量是%s,对象的变量是%s' % ( class1.cname, self.cname ) )
  
  def setcnt( self, cnt ):
    self.ccnt = cnt
    
  def getcnt( self ):
    return self.ccnt


if __name__ == "__main__" :
  print( "__name__ = %s" % __name__ )
  cls = class1('loki')
  cls.setcnt(10)
  print( 'cnt=%d' % cls.getcnt() )
