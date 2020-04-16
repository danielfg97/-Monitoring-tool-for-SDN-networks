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
        sixthHost = self.addHost('h6')

        firstSwitch = self.addSwitch( 's1' )
        secondSwitch = self.addSwitch( 's2' )
        thirdSwitch = self.addSwitch( 's3' )
        fourthSwitch = self.addSwitch( 's4' )
        fifthSwitch = self.addSwitch( 's5' )
        sixthSwitch = self.addSwitch( 's6' )
        seventhSwitch = self.addSwitch( 's7' )
        eighthSwitch = self.addSwitch( 's8' )

        # Add links
        self.addLink( firstHost, secondSwitch )
        self.addLink( secondHost, seventhSwitch )
        self.addLink( thirdHost, seventhSwitch )
        self.addLink( firstSwitch, secondSwitch )
        self.addLink( thirdSwitch, fourthHost )
        self.addLink( thirdSwitch, secondSwitch )
        self.addLink( thirdSwitch, firstSwitch )
        self.addLink( firstSwitch, fourthSwitch )
        self.addLink( firstSwitch, fifthSwitch )
        self.addLink( fourthSwitch, seventhSwitch )
        self.addLink( fourthSwitch, sixthSwitch )
        self.addLink( sixthSwitch, eighthSwitch )
        self.addLink( fifthHost, fifthSwitch )
        self.addLink( eighthSwitch, sixthHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }

