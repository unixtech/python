class SocketH:
    '''
    One of the objects to be returned
    '''

    def action(self):
        return f"Connection established: http"


    def __str__(self):
        return "Socket_H"


class SocketFactory:
    '''
    Concrete factorty
    '''

    def get_connection(self):
        '''
        Returns a Get request object
        '''
        return SocketH()


    def get_request(self):
        '''
        Returns a Get Request object
        '''
        return "get request"

class Connections:
    '''
    Connections class houses our abstract factory
    '''

    def __init__(self, connection_factory = None):
        '''
        Connections class is our abstract factory
        '''
        self._connection_factory = connection_factory


    def show_connection(self):
        '''
        Utility method to display details of objects returned by the connection factory
        '''
        connection = self._connection_factory.get_connection()
        request = self._connection_factory.get_request()

        print(f"Connection: {connection}")
        print(f"Action: {connection.action()}")
        print(f"Request: {request}")


factory_a = SocketFactory()
factory_b = SocketFactory()


# Create a connections, Our Abstract Factory
connect = Connections(factory_b)


# Invoke the utility method to show the details.
connect.show_connection()
