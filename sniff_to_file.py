__author__ = 'techbk'

import pcap, dpkt, time


def process( ts, pkt , pcw):
    print pkt

    pcw.writepkt(pkt,ts)

def loop(pc, ti):

    #filename = time.strftime("%Y%m%d-%H%M%S")+'.pcap'
    filename = str(ti)+'.pcap'
    pcw = dpkt.pcap.Writer(open(filename,'wb'))

    for ts, pkt in pc:
        t = time.time()
        if t - ti >= 30:
            pcw.close()
            #filename = time.strftime("%Y%m%d-%H%M%S")+'.pcap'
            filename = str(t)+'.pcap'
            pcw = dpkt.pcap.Writer(open(filename,'wb'))
            pcw.writepkt(pkt,ts)
            ti = t
            continue
        pcw.writepkt(pkt,ts)

if __name__ == "__main__":


    #count =0
    #Pcap writer

    try:
        pc = pcap.pcap()

        loop(pc, time.time())
    except KeyboardInterrupt:
        print pc.stats()
