import platform
import os

# Assign IP to ping to a variable
ip ="127.0.0.1"
current_os= platform.system().lower()
if current_os == "windows":
#building our ping commands to windows
    ping_cmd= f"ping -n 1 -w 2 {ip} > null"
else:
    ping_cmd= f"ping -c 1 -w 2 {ip}> /dev/null 2>&1"
# Execute command and capture exit code
exit_code = os.system(ping_cmd)
# Print results to console
print(exit_code)
