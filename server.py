import http.server
import socketserver
import os

# Porta do servidor
PORT = 8000

# Diretório a ser servido (pasta atual)
DIRECTORY = os.getcwd()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Iniciar o servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    print("Pressione Ctrl+C para parar.")
    httpd.serve_forever()