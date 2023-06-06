import sys
import time
import logging
import os

import binding_topology
import binding_amplificador_raman # importe el módulo binding_amplificador_raman

from pyangbind.lib.serialise import pybindIETFXMLEncoder, pybindIETFXMLDecoder
#from binding_amplificador_raman import yc_amplificador_raman_amplificador_raman__amplificador_raman

from netconf import nsmap_add, NSMAP
from netconf import server, util
from lxml import etree

logging.basicConfig(level=logging.DEBUG)

nsmap_add("amplificador-raman", "urn:amplificador-raman") # agregue el espacio de nombres del amplificador Raman

class MyServer(object):
    def __init__(self, username, password, port):
        host_key_value = os.path.join(os.path.abspath(os.path.dirname(__file__)), "server-key")
        auth = server.SSHUserPassController(username=username, password=password)
        self.server = server.NetconfSSHServer(server_ctl=auth, server_methods=self, port=port, host_key=host_key_value, debug=False)
        self.load_file()

    def load_file(self):
        # create configuration
        xml_root = open('amplificador-raman.xml', 'r').read()
        print(xml_root)
        topo = pybindIETFXMLDecoder.decode(xml_root, binding_amplificador_raman, "amplificador-raman")
        xml = pybindIETFXMLEncoder.serialise(topo)
        tree = etree.XML(xml)
        data = util.elm("nc:data")
        data.append(tree)
        self.node_topology = data

    def nc_append_capabilities(self, capabilities):
        util.subelm(capabilities, "capability").text = "urn:ietf:params:netconf:capability:xpath:1.0"
        util.subelm(capabilities, "capability").text = NSMAP["amplificador-raman"] # agregue la capacidad del amplificador Raman

    def rpc_get_config(self, session, rpc, source_elm, filter_or_none):
        logging.debug("--GET CONFIG--")
        logging.debug(session)
        logging.debug(etree.tostring(rpc))
        return util.filter_results(rpc, self.node_topology, None)

    def close(self):
        self.server.close()

def main(*margs):
    s = MyServer("admin","admin", 830)

    if sys.stdout.isatty():
        logging.debug("^C to quit server")

    try:
        while True:
            time.sleep(1)

    except Exception:
        logging.debug("quitting server")

    s.close()

if __name__ == "__main__":
    main()
