import loggging

class Rdb(pdb.Pdb):
    """
    This will run pdb as a ephemeral telnet service. Once you connect no one
    else can connect. On construction this object will block execution till a
    client has connected.

    Based on https://github.com/tamentis/rpdb I think ...

    To use this::

        Rdb(4444).set_trace()

    Then run: telnet 127.0.0.1 4444
    """
    def __init__(self, port=0):
        self.old_stdout = sys.stdout
        self.old_stdin = sys.stdin
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.bind(('0.0.0.0', port))
        if not port:
            logging.critical("PDB remote session open on: %s", self.listen_socket.getsockname())
            print >> sys.__stderr__, "PDB remote session open on:", self.listen_socket.getsockname()
            sys.stderr.flush()
        self.listen_socket.listen(1)
        self.connected_socket, address = self.listen_socket.accept()
        self.handle = self.connected_socket.makefile('rw')
        pdb.Pdb.__init__(self, completekey='tab', stdin=self.handle, stdout=self.handle)
        sys.stdout = sys.stdin = self.handle

    def do_continue(self, arg):
        sys.stdout = self.old_stdout
        sys.stdin = self.old_stdin
        self.handle.close()
        self.connected_socket.close()
        self.listen_socket.close()
        self.set_continue()
        return 1

    do_c = do_cont = do_continue

def set_trace():
    """
    Opens a remote PDB on first available port.
    """
    rdb = Rdb()
    rdb.set_trace()
