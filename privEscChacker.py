import subprocess
import pyfiglet
def run_cmd(cmd, shell=False):
    try:
        result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        return "[+] Command returned non-zero exit code or access denied."
    except FileNotFoundError:
        return "[+] Command not found on this system."
    except Exception as e:
        return f"[+] Error: {e}"
print(pyfiglet.figlet_format("User"))
print(f"[+] Current user is : {run_cmd(['whoami'])}\n")
print(f"[+] Contents of /etc/passwd :\n{run_cmd(['cat', '/etc/passwd'])}\n")
awk_cmd = "cat /etc/passwd | grep '0:0' | awk -F: '{ print $1}'"
print(f"[+] Root user accounts : {run_cmd(awk_cmd, shell=True)}\n")
print(f"[+] Current user/group info: {run_cmd(['id'])}\n")
print(f"[+] Hostname: {run_cmd(['hostname'])}\n")
print(f"[+] Logged on users:\n{run_cmd(['w'])}\n")
print(pyfiglet.figlet_format("Kernel"))
print(f"[+] Kernel information : {run_cmd(['uname', '-a'])}\n")
print(pyfiglet.figlet_format("Cron Jobs"))
print(f"[+] Contents of /etc/crontab:\n{run_cmd(['cat', '/etc/crontab'])}\n")
print(f"[+] Cron directories & permissions:\n{run_cmd('ls -la /etc/cron*', shell=True)}\n")
cmd_writable = "find /etc/cron* -perm -0002 -type f -exec ls -la {} \\; 2>/dev/null"
writable_out = run_cmd(cmd_writable, shell=True)
if writable_out and not writable_out.startswith("[-]"):
    print(f"[+] wrpng: Found world-writable cron file(s):\n{writable_out}\n")
else:
    print("[+] No world-writable cron files found.\n")
print(f"[+] Current user's crontab:\n{run_cmd(['crontab', '-l'])}\n")
cmd_timers = "systemctl list-timers --no-pager 2>/dev/null | head -n 15"
print(f"[+] Active Systemd Timers (First 15):\n{run_cmd(cmd_timers, shell=True)}\n")
print(pyfiglet.figlet_format("Sudo"))
sudo_out = run_cmd(["sudo", "-n", "-l"])
print(f"[+] Sudo permissions check:\n{sudo_out}\n")
print(pyfiglet.figlet_format("SUID"))
suid_cmd = "find / -perm -4000 -type f 2>/dev/null"
print(f"[+] SUID files found:\n{run_cmd(suid_cmd, shell=True)}\n")
print(pyfiglet.figlet_format("Ports"))
ports_cmd = "ss -tuln 2>/dev/null || netstat -tuln 2>/dev/null"
print(f"[+] Listening ports (TCP/UDP):\n{run_cmd(ports_cmd, shell=True)}\n")
print(pyfiglet.figlet_format("PATH"))
path_cmd = "echo $PATH"
print(f"[+] Current PATH: {run_cmd(path_cmd, shell=True)}\n")
print(pyfiglet.figlet_format("Processes"))
ps_cmd = "ps aux | grep root | head -n 20"
print(f"[+] Root processes (Top 20):\n{run_cmd(ps_cmd, shell=True)}\n")
print(pyfiglet.figlet_format("SSH"))
find_cmd = "find / -name 'id_rsa' 2>/dev/null"
print(f"[+] id_rsa files location:\n{run_cmd(find_cmd, shell=True)}\n")
