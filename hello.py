def app(environ, start_response):

    args = environ.get('QUERY_STRING').split("&")
    response_headers = [("Content-type", "text/plain")]
    start_response('200 OK', response_headers)
    response_body = '\n'.join(args)
    return [response_body.encode('utf-8')]
