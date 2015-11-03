__author__ = 'techbk'

import pcap, dpkt


def process( ts, pkt , pcw):
    #eth = dpkt.ethernet.Ethernet(pkt)
    #ip = eth.data
    #if ip.__class__==dpkt.ip.IP:
        #global count
        #count += 1
        #src_ip = socket.inet_ntoa(ip.src)
        #dst_ip = socket.inet_ntoa(ip.dst)
        #print 'Packet #%d, %s=>%s, length %d, proto: %d' % (count, src_ip, dst_ip, ip.len, ip.p)
        # Save packet to file...
    pcw.writepkt(pkt,ts)

if __name__ == "__main__":
    pc = pcap.pcap()
    #count =0
    #Pcap writer
    pcw = dpkt.pcap.Writer(open('pkts.pcap','wb'))
    try:
        pc.loop(process, pcw)
    except KeyboardInterrupt:
        print pc.stats()
        pcw.close()