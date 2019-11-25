import http.server
import socketserver
from data_structure import Stack, Linked_list

PORT = 8000

myStack = Stack()
myList = Linked_list()


def ParseRequest(self):
    if self.headers["Content-Length"]:
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode("UTF-8").split("&")
        request = {}
        for i in body:
            i = i.split("=")
            if len(i) == 2:
                request[i[0]] = i[1]
        return request


def SendResponse(self, responseCode, responsebody=None):
    if responsebody:
        self.send_response(responseCode)
        self.end_headers
        self.wfile.write(bytes(responsebody, "UTF-8"))
    else:
        self.send_response(responseCode)
        self.end_headers
    return


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        request = ParseRequest(self)
        if not request:
            self.send_response(401)
            self.end_headers()
            return

        if "data_type" in request and "action" in request:
            if request["data_type"] == "stack" and request["action"] == "show":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(myStack.show(), "utf-8"))
            elif request["data_type"] == "linked_list" and request["action"] == "show":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(myList.show(), "utf-8"))
            else:
                self.send_response(401)
                self.end_headers()

    def do_PUT(self):

        request = ParseRequest(self)
        if not request:
            self.send_response(401)
            self.end_headers()
            return

        if "data_type" in request and "action" in request:
            if request["data_type"] == "stack":
                if request["action"] == "push" and "value" in request:
                    if request["value"].isalnum():
                        myStack.push(request["value"])
                        self.send_response(200)
                    else:
                        self.send_response(401)

                elif len(myStack.stack) >= 1 and request["action"] == "pop":
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(myStack.pop(), "utf-8"))
                else:
                    self.send_response(401)

            elif request["data_type"] == "linked_list" and "action" in request:
                if request["action"] == "insert" and "value" in request:
                    if "successor" in request:
                        try:
                            if request["value"].isalnum():
                                myList.insert(request["value"], request["successor"])
                                self.send_response(200)
                            else:
                                self.send_response(401)
                        except:
                            self.send_response(401)
                            self.end_headers()
                            self.wfile.write(b"Successor not found")
                    else:
                        if request["value"].isalnum():
                            myList.insert(request["value"])
                            self.send_response(200)
                        else:
                            self.send_response(401)
                elif request["action"] == "remove" and "value" in request:
                    try:
                        myList.remove(request["value"])
                        self.send_response(200)
                    except:
                        self.send_response(401)
                        self.end_headers()
                        self.wfile.write(b"Value not in list")
                else:
                    self.send_response(401)
            else:
                self.send_response(401)
        else:
            self.send_response(401)
        self.end_headers()


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
