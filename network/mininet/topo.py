from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        firstHost = self.addHost( 'h1' )
        secondHost = self.addHost( 'h2' )
        thirdHost = self.addHost('h3')
        fourthHost = self.addHost('h4')
        fifthHost = self.addHost('h5')

        firstSwitch = self.addSwitch( 's1' )
        secondSwitch = self.addSwitch( 's2' )
        thirdSwitch = self.addSwitch( 's3' )
        fourthSwitch = self.addSwitch( 's4' )
        fifthSwitch = self.addSwitch( 's5' )

        # Add links
        self.addLink( firstHost, firstSwitch )
        self.addLink( secondHost, firstSwitch )
        self.addLink( firstSwitch, secondSwitch )
        self.addLink( thirdHost, secondSwitch )
        self.addLink( secondSwitch, thirdSwitch )
        self.addLink( thirdSwitch, fourthSwitch )
        self.addLink( thirdSwitch, fifthSwitch )
        self.addLink( fourthSwitch, fifthSwitch )
        self.addLink( fifthHost, fifthSwitch )
        self.addLink( fourthSwitch, fourthHost )



topos = { 'mytopo': ( lambda: MyTopo() ) }

