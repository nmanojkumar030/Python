import paramiko


class CustomSSHClient:
    def __init__(self, host, port, user, pwd):  # Constructor
        self.host = host
        self.port = port
        self.user = user
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # ack for the key
        self.ssh.connect(host, port, user, pwd)

    def check_output(self, job):
        stdin, stdout, stderr = self.ssh.exec_command(job)
        return stdout.read()

    def __del__(self):
        self.ssh.close()  # Destructor


ssh = CustomSSHClient('ravijaya.info', 22, 'training', 'training')
op = ssh.check_output('date')
print(op)


