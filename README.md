# Anti-Virus Script

<p align="center">
  <img src="https://cdn.icon-icons.com/icons2/39/PNG/64/antivirus_virus_linux_penguin_6258.png" alt="Image" width="200" height="200" />
</p>

This is a Python script that performs various security checks on a Linux system to detect and mitigate potential threats.
Features

    * Creates a backup of the original syslog file and truncates it to clear any sensitive information.
    * Checks for sudo vulnerabilities by attempting to execute the sudoedit command with the -A and ALL flags.
    * Lists open ports on the system and saves the output to a file.
    * Lists running processes on the system and saves the output to a file.
    * Checks user configuration files and saves the output to a file.
    * Extracts password policies and hash storage method information and saves the output to a file.
    * Checks for rootkits using the chkrootkit command.
    * Prints a banner upon completion of the script.

## Contributors

- **User:** [0x01](https://github.com/0x01-sec)
- **User:** [Discord Server](https://discord.gg/gQ4sPRWq)

Requirements

    This script is designed to be run on a Linux system.
    The user running the script must have administrative privileges.

Installation


    git clone https://github.com/0x01-sec/AntiVirus-Linux-.git

Install the required packages:

     cd anti-virus-script


License

This project is licensed under the MIT License - see the LICENSE file for details.
