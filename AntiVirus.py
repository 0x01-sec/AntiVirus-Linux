# Created by 0x Web Moroccan 
# This script checks for various security vulnerabilities in the system.
import shutil
import subprocess
import time
import os

# Define the path to the syslog file
syslog_path = "/var/log/syslog"

# Create a backup of the original syslog file
shutil.copy(syslog_path, syslog_path + ".bak")

# Truncate the syslog file
with open(syslog_path, "w"):
    pass

# Check for sudo vulnerabilities
try:
    subprocess.run(["sudoedit", "-A", "ALL"], check=True)
except subprocess.CalledProcessError:
    print("sudoedit command is not vulnerable")
else:
    print("sudoedit command is vulnerable")

# Check for open ports
try:
    output = subprocess.check_output(["netstat", "-tulpn"])
    with open("open_ports.txt", "w") as f:
        f.write(output.decode())
except subprocess.CalledProcessError:
    print("Error checking for open ports")

# List running processes and save output to file
try:
    output = subprocess.check_output(["ps", "aux"])
    with open("running_processes.txt", "w") as f:
        f.write(output.decode())
except subprocess.CalledProcessError:
    print("Error listing running processes")

# Check user config and save output to file
try:
    user_config_dir = os.path.expanduser("~/.config")
    output = subprocess.check_output(["ls", "-al", user_config_dir])
    with open("user_config.txt", "w") as f:
        f.write(output.decode())
except subprocess.CalledProcessError:
    print("Error checking user config")

# Extract password policies and hash storage method information and save in file
try:
    output = subprocess.check_output(["sudo", "grep", "^PASS_.*", "/etc/login.defs"])
    with open("password_policies.txt", "w") as f:
        f.write(output.decode())
    output = subprocess.check_output(["sudo", "authconfig", "--test"])
    with open("hash_storage.txt", "w") as f:
        f.write(output.decode())
except subprocess.CalledProcessError:
    print("Error extracting password policies and hash storage information")

time.sleep(3.4)

# Check for rootkits
try:
    subprocess.run(["chkrootkit"], check=True)
except subprocess.CalledProcessError:
    print("No rootkits found")
else:
    print("Rootkits found")

# Print a banner
print("=" * 50)
print("Anti-Virus script completed Create By 0x01 /")
print("=" * 50)
