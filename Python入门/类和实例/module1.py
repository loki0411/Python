import 类和实例的使用


from 类和实例的使用 import class1

print( r'c:a\name' )
print( """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""" )

print( 类和实例的使用.__name__ )

class1.__init__( class1.__init__, 'cls1' )

print( class1.cname )


class SystemCall:  # 这里是注释，#不能改为引号
    """"system command"""

    skillname = 'default name'
    command = 'default command'

    def __init__( self, name ):
        self.skillname = name

    def fun1( x, y, z ):
        pass


SystemCall.fun1( 3, z = 3, y = 4 )
addxy = lambda x, y: x + y
print( addxy( 3, 4 ) )

sonicleap = SystemCall( "sonicleap" )
Quadripartite_chopping = SystemCall( "Quadripartite chopping" )
sonicleap.command = 'sword skill sonic leap'
print( sonicleap.skillname )
print( sonicleap.command )

print( Quadripartite_chopping.skillname )
