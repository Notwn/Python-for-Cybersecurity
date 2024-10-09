#pinging on the entire network
import platform
import os

#setting the ip prefix
ip_prefix= 	"192.168.0."
#determine the current os
current_os = platform.system(). lower()
#loop from  o to 254
for final_octet in range (254):
    #assign ip to ping to a variable
    #adding 1 to the final octet because loop starts at 0
    ip= ip_prefix +  str(final_octet + 1)

    if current_os ==  "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > null"
    else:
        ping_cmd = f"ping -c 1  -w {ip} > /dev/null 2> & 1"
# Execute command and capture exit code
exit_code= os.system(ping_cmd)
# Print results to console only if successful
if exit_code== 0:
    print("{0} is online".format(ip))
