import paramiko
import paramiko.ssh_exception

def ssh_command(ip, user, password, commands):
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=user, password=password)
        print(f"Connected to {ip} as {user}")

        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)

            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                print(output)
            if error:
                print(f"Error: {error}")

    except paramiko.AuthenticationException:
        print("Failed to authenticate")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    
    commands = ["uname -a", "whoami", "df -h"]
    ssh_command("10.2.10.150", "debian", "iths2023", commands)