import asyncore, smtpd

def server_start():
    smtpd.DebuggingServer(('localhost', 25), None)
    asyncore.loop()

if __name__ == '__main__':
    server_start()
