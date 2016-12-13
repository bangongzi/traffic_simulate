#!/usr/bin/python
# -*- coding: UTF-8 -*-

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call



def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    h = []

    info( '*** Adding controller ***\n' )
    RYU=net.addController(name='RYU',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Adding switches ***\n')
    s1 = net.addSwitch('s1',cls=OVSKernelSwitch)


    info( '*** Adding hosts ***\n')
    #Adding normal hosts
    for i in range(101):
        host_name = 'h' + str( i + 1 )
        ip_addr = '10.0.0.' + str( i + 1 )
        hs = net.addHost(host_name,cls = Host,ip = ip_addr,defaultRoute=None)
        h.append( hs )
    #Adding the special host "h101" 
    #hs = net.addHost('h81',cls = Host,ip = '10.0.0.81',defaultRoute=None)
    #h.append( hs )


    info( '*** Adding links ***\n')
    for i in range( 101 ):
        net.addLink(s1,h[i])
    
    info( '*** Starting network ***\n')
    net.build()

    info( '*** Starting controllers ***\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches ***\n')
    net.get(s1.name).start([RYU])

    info( '*** Post configure switches and hosts ***\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()            