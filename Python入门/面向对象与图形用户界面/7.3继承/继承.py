import system_call


class Calc:

    def __init__( self ):
        self.data = []

    def append2( self, x ):
        self.data.append( x )
        self.data.append( x )


class Calc_child( Calc ):

    def add( self, a, b ):
        return a + b

    def __init__( self ):
        Calc.__init__( self )


c_child = Calc_child( )
c_child.append2( 4 )
print( c_child.data )
print( c_child.add( 4, 4 ) )
