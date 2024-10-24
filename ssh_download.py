import paramiko
import paramiko.ssh_exception

def ssh_command(ip, user, password, local_path, remote_path):
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=user, password=password)
        print(f"Connected to {ip} as {user}")

        sftp = ssh.open_sftp()

        sftp.get(remote_path, local_path)
        print(f"The file {remote_path} has been downloaded to {local_path}")

        sftp.close()
    except paramiko.AuthenticationException:
        print("Failed to authenticate")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    ssh_command("10.2.10.150", "debian", "iths2023", "test.txt", "/home/debian/remote.txt")