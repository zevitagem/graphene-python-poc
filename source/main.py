import os
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from core.infrastructure.http.action.SearcherController import SearcherController
from urllib import parse

hostName = "0.0.0.0"
serverPort = 8082


class MyServer(BaseHTTPRequestHandler):

    def sanitize_path(self, path):
        if re.search("\.", self.path) is not None:
            raise ValueError('URL inválida')

        path = path.replace('/', '').strip()

        if (len(path) == 0):
            return 'index'
        elif '?' in path:
            return path.split('?')[0]
        else:
            return path

    def get_query_parameters(self, url):
        query_params = {}
        if '?' in url:
            query_params = dict(
                parse.parse_qsl(
                    parse.urlsplit(url).query
                )
            )
        return query_params

    def end(self, response):
        self.wfile.write(bytes(response, "utf-8"))

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        try:
            response = getattr(SearcherController(), self.sanitize_path(self.path))({
                "query": self.get_query_parameters(self.path)
            })

            self.end(response)
        except KeyboardInterrupt as KI:
            raise KI
        except Exception as e:
            response = 'Sorry:: ' + str(e)
            self.end(response)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        os.environ["package"] = "source"
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
