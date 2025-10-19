from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080


current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "catalog", "templates", "Contacts.html")


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Метод для обработки входящих гет запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        r = read_html(html_path)
        self.wfile.write(r.encode("utf-8"))


def read_html(current_file):
    """Функция чтения шаблона html"""
    with open(current_file, "r", encoding="UTF-8") as file_html:
        result = file_html.read()
    return result


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Сервер остановлен")
