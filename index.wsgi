def application(environ, start_response):
    status = '200 OK'
    my_name = 'Anil Raj Rimal'
    output = f'Hello, World! This is a simple Python WSGI application. My name is {my_name}.'.encode('utf-8')

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)
    return [output]

