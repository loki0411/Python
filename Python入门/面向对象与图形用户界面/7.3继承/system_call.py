import PyQt5



class systemcall( object ):
    priority = 0
    name = 'システムコール'

    def __init__( self, name ):
        self.name = name
        self.dat = []

    def setname( self, name ):
        self.name = name

    def getname( self ):
        return self.name


class generate( systemcall ):
    pass


class element( object ):
    counter = 0

    def __init__( self, name, ADDR ):
        self.name = name
        self.addr = ADDR
        element.counter += 1

    def setname( self, new_name ):
        self.name = new_name
        return self.name

    if __name__ == "__main__":
        pass


FIR = element( 123, 333 )

print( FIR.name, FIR.addr )

thermal = element( 'thermal element', 122 )
print( thermal.addr )

print( element.setname( element, 'firew' ) )  # 给类起名
print( element.counter )
