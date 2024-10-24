import sublist3r
import requests

domain = "example.com"

subdomains = sublist3r.main(domain, 20, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)

output_file = "subdomains.txt"

with open(output_file, 'w') as file:
    for subdomain in subdomains:
        try:
            response = requests.get(f"https://{subdomain}", timeout=5)
            status = response.status_code
            print(f"Subdomain is UP: {subdomain}, Status code: {status}")
            file.write(f"Subdomain is UP: {subdomain}, Status code: {status}\n")
        except requests.ConnectionError:
            print(f"Subdomain is DOWN: {subdomain}")
            file.write(f"Subdomain is DOWN: {subdomain}\n")
        except requests.Timeout:
            print(f"Subdomain timed out: {subdomain}")
            file.write(f"Subdomain timed out: {subdomain}\n")

print(f"Done. Saved results to {output_file}")