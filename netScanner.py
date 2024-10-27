import scapy.all as scapy
import optparse

class Scanner:

    def __init__(self):
        pass

    def getValue(self):
        opt=optparse.OptionParser()
        opt.add_option('-n','--network',dest='network',help='Network range to scan, e.g., 192.168.1.0/24')
        opt.add_option('-g','--graph',action='store_true',dest='graph',default=False,help='Display graphical output')
        (options,args)=opt.parse_args()
        if not options.network:
            opt.error("Please specify a network range using -n or --network")
        else:
            print(f"network range entered : {options.network}")
            return options



    def broadcast(self,network_range,show_graph):
        arp=scapy.ARP(pdst=network_range)
        broadcast_packet=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        combined_packet=broadcast_packet/arp
        (answered,unanswered)=scapy.srp(combined_packet,timeout=1,verbose=False)
        answered.summary()

        if show_graph:
            answered.conversations()



scanner=Scanner()
options=scanner.getValue()
scanner.broadcast(options.network,options.graph)