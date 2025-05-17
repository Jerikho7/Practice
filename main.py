from http.server import BaseHTTPRequestHandler, HTTPServer
from path import root_join

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            file_path = root_join("html", "contacts.html")
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        except FileNotFoundError:
            self.send_error(404, "Файл не найден")


# Запуск сервера
if __name__ == "__main__":
    server_address = ("", 8000)  # Порт 8000
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен на http://localhost:8000")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
         pass

    httpd.server_close()
    print('Server stopped')
