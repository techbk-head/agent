__author__ = 'techbk'

#tao 2 thread. gui file pcap + tao file pcap

from multiprocessing import Process,Queue
from managerpcap import ManagerPcap
from client import Client

if __name__ == "__main__":
    q=Queue()
    manager_pcap = ManagerPcap(q)
    client = Client(q)
    p_pcap_loop = Process(target=manager_pcap.loop)
    p_client_loop = Process(target=client.loop)
    p_client_loop.start()
    p_pcap_loop.start()

    #p_pcap_loop.join()
    #p_client_loop.join()


