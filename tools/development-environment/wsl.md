
Using WSL allows us to use familiar linux commands for our development workflow. In addition, we can also keep track of our development configurations by leveraging Ansible.

# Setup
- Follow the [latest instructions to install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).
- Install distro of choice from Windows Store. 
- Launch the distro, which will finish the setup, and should prompt for creating user and password. (If it doesn't, You can manually run [this script](https://github.com/tloeber/utils_and_configs/blob/f362e7ff06489c0dbd66b542b32cc97eb79cb5cd/machine_setup/WSL/create_user.sh).
- Only after finishing this last step will be new distro show up in VSCode under WSL targets after you click refresh. If not, you may have to restart VSCode, WSL (`wsl --shutdown`) or worst case the Windows machine.

# Configuration
See https://learn.microsoft.com/en-us/windows/wsl/wsl-config
Remember to keep these configurations files in version control.

# Issues
I have repeatedly encountered the following issues, and have decided that it's not worth my time keep trying to make them work:
- Git Credential Manager
- SSH key forwarding. It would be good to have the option, but not that important anyway because SSH keys don't work well with ephemeral cloud infrastructure. Also doesn't work with AWS Sagemaker Studio notebooks, because unfortunately there is no officially reported way to connect to them remotely through VS Ccode.


# Troubleshooting
- Restart WSL to solve all kinds of erros (e.g., can't open WSL in VSCode; can't authenticate to AWS SSO because clock time is off; etc)
  - Open Powershell and run `wsl --shutdown`. (No admin permissions needed.) It will start again automatically. 

- Errors resulting from system clock being off, such as `apt-get update` or AWS SSO login failing:
  - Confirm system clock is off by running `date`
  - If that's the case, synchronize:
    - Hardware clock: `sudo timedatectl set-local-rtc 1`
    - System clock: `sudo timedatectl set-ntp true`

- Error when trying to use `sudo`: `user not in sudoers group`
  - Cause: For me, it seems to be connected to Windows updates.
  - Solution:
    - The key is to start a privileged WSL shell from the Windows environment: open a command prompt and enter `wsl --user root`
    - Now you can add back the sudo privileges again: `usermod -aG sudo ${username}`
    - Restart WSL: 
      - Exit WSL to go back to cmd: `exit`
      - From cmd, restart WSL: `wsl --shutdown`
      - Start Docker Desktop again
      - Restart VSCode

- Zone-identifier files created for every file copied from Windows drive. I haven't found a quick way to stop this, sound like this is a bug that may be fixed at some point. So for now I'm simply deleting the zone identifier files by running ` find . -type f -name "*.Identifier" -exec rm -f {} \;`