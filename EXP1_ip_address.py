
import socket

# Get the hostname of the system
hostname = socket.gethostname()

# Get the IP address
ip_address = socket.gethostbyname(hostname)

# Display the result
print("Hostname:", hostname) 
print("IP Address:", ip_address)
