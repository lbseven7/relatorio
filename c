elatorio\app.py
if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Acesse o aplicativo em: http://{local_ip}:8501")
    
    # Não é necessário iniciar o servidor Streamlit manualmente
    # O comando 'streamlit run app.py' já faz isso automaticamente