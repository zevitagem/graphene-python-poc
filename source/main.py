from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from core.infrastructure.http.action.SearcherController import SearcherController

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def sanitize_path(self, path):
        path = path.replace('/', '').strip()

        if (len(path) == 0):
            return 'index'
        return path

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = getattr(SearcherController(), self.sanitize_path(self.path))()

        self.wfile.write(bytes(response, "utf-8"))

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
