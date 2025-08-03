"""Single Threaded SSH Client using Paramiko"""

import paramiko


class CustomSSHClient:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        # self.pwd = pwd

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, pwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdout.read().decode('ascii')

    def __del__(self):
        self.ssh.close()

    def upload(self, file_name):
        # SFTP upload
        sftp = self.ssh.open_sftp()
        sftp.put(file_name, file_name)
        sftp.close()


if __name__ == '__main__':
    ssh = CustomSSHClient('ravijaya.info', 22, 'training', 'training')
    ssh.upload('getinfo.sh')
    # op = ssh.check_output('lscpu')
    op = ssh.check_output('bash getinfo.sh')
    print(op)
