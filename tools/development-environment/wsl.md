
Using WSL allows us to use familiar linux commands for our development workflow. In addition, we can also keep track of our development configurations by leveraging Ansible.

# Issues
I have repeatedly encountered the following issues, and have decided that it's not worth my time keep trying to make them work:
- Git Credential Manager
- SSH key forwarding. It would be good to have the option, but not that important anyway because SSH keys don't work well with ephemeral cloud infrastructure. Also doesn't work with AWS Sagemaker Studio notebooks, because unfortunately there is no officially reported way to connect to them remotely through VS Ccode.


# Troubleshooting
- Restart WSL to solve all kinds of erros (e.g., can't open WSL in VSCode; can't authenticate to AWS SSO because clock time is off; etc)
  - Open Powershell and run `wsl --shutdown`. (No admin permissions needed.) It will start again automatically. 

- Error when trying to use `sudo`: `user not in sudoers group`
  - Cause: For me, it seems to be connected to Windows updates.
  - Solution:
    - The key is to start a privileged WSL shell from the Windows environment: open a command prompt and enter `wsl --user root`
    - Now you can add back the sudo privileges again: `usermod -aG sudo ${username}`
    - Restart WSL: 
      - From cmd: `wsl --shutdown`
      - Start Docker Desktop again
      - Restart VSCode
