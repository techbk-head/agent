__author__ = 'techbk'

import pcap as pCap
import dpkt
import time

PCAP_PATH = 'pcap/'

class ManagerPcap(object):

    def __init__(self, time_limited = 30):
        self._pc = pCap.pcap()
        self._time_limited = time_limited

    def loop(self, ti=None, time_limited = None):
        try:
            if not time_limited:
                time_limited = self._time_limited
            if not ti:
                ti = time.time()
            #filename = time.strftime("%Y%m%d-%H%M%S")+'.pcap'
            filename = _filename(ti)
            pcw = dpkt.pcap.Writer(open(filename,'wb'))

            for ts, pkt in self._pc:
                #t = time.time()
                if ts - ti >= time_limited:
                    pcw.close()
                    #filename = time.strftime("%Y%m%d-%H%M%S")+'.pcap'
                    filename = _filename(ts)
                    pcw = dpkt.pCap.Writer(open(filename,'wb'))
                    pcw.writepkt(pkt,ts)
                    ti = ts
                    continue
                pcw.writepkt(pkt,ts)
        except KeyboardInterrupt:
            print self._pc.stats()

def _filename(t):

    return PCAP_PATH+str(int(t))+'.pcap'
if __name__ == "__main__":
    manager_pcap = ManagerPcap()
    manager_pcap.loop()