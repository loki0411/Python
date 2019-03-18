

import 类和实例的使用
import sys
from  类和实例的使用 import class1

print( r'c:a\name' )
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print( 类和实例的使用.__name__ )

class1.__init__(class1.__init__,'cls1')

print( class1.cname )


class system_call: #这里是注释，#不能改为引号
  "system command"
  
  skillname = 'default name'
  command = 'default command'
  def __init__(self, name):    
    self.skillname = name
  def fun1(x, y, z ):
    pass
  

system_call.fun1(3, z=3,y=4 )
myadd = lambda x,y : x+y
print( myadd(3,4) )


sonicleap = system_call("sonicleap")
Quadripartite_chopping = system_call("Quadripartite chopping")
sonicleap.command = 'sword skill sonic leap'
print( sonicleap.skillname )
print( sonicleap.command )

print( Quadripartite_chopping.skillname )
