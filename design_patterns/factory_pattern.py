class SocketH:
    """ 
    HTTP protocol example of the ind

    """
    def __init__(self, name):
        self.name = name

    def action(self):
        return f"Connection: {self.name}"


class SocketF:
    """
    Class example object FTP
    """
    def __init__(self, name):
        self.name = name

    def action(self):
        return f"Connection: {self.name}"


def get_connection(connection="http"):
    """ The factory method """
    connections = {'http': SocketH("http_connection"), 'ftp': SocketF('ftp_connection')}
    return connections[connection]


# Running factory function
http = get_connection('http')
print(f"Object -> {http.action()}")


ftp = get_connection('ftp')
print(f"Object -> {ftp.action()}")
