#!/usr/bin/env python3
"""
Servidor HTTP simples para servir o frontend
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def serve_frontend():
    """Inicia um servidor HTTP para servir o frontend"""
    
    # Configurações do servidor
    PORT = 8080
    DIRECTORY = Path(__file__).parent
    
    # Mudar para o diretório do projeto
    os.chdir(DIRECTORY)
    
    # Configurar o handler
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 Servidor frontend iniciado!")
            print(f"📁 Diretório: {DIRECTORY}")
            print(f"🌐 URL: http://localhost:{PORT}")
            print(f"📄 Frontend: http://localhost:{PORT}/frontend.html")
            print(f"📚 API Docs: http://localhost:8000/docs")
            print("\n" + "="*50)
            print("💡 Dicas:")
            print("- Certifique-se de que a API está rodando na porta 8000")
            print("- Acesse http://localhost:8080/frontend.html")
            print("- Pressione Ctrl+C para parar o servidor")
            print("="*50 + "\n")
            
            # Abrir o navegador automaticamente
            webbrowser.open(f'http://localhost:{PORT}/frontend.html')
            
            # Manter o servidor rodando
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Servidor parado pelo usuário")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Porta {PORT} já está em uso!")
            print("💡 Tente parar outros servidores ou usar uma porta diferente")
        else:
            print(f"❌ Erro ao iniciar servidor: {e}")

if __name__ == "__main__":
    serve_frontend() 