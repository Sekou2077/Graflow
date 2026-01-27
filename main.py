# Author: Sekou Traore
# Network monitoring script
# Make a minimum working version and incrementally improve


# interesting library that provides system and network information
import psutil
import time


# Returns system-wide network I/O statistics as a named tuple(pernic=False lists all interfaces and allows me to
# access individual interface stats since the returned object remains a named tuple)
network_stats = psutil.net_io_counters(pernic=False, nowrap=True)

print("Welcome to my network monitoring script")
time.sleep(1)
print("Gathering network statistics...")
time.sleep(3)
# Display network statistics in easier formatting
print(
    f"network stats: bytes sent = {network_stats.bytes_sent}, bytes received = {network_stats.bytes_recv}, pac"
    f"kets sent = {network_stats.packets_sent}, packets received = {network_stats.packets_recv}, total receiving errors"
    f" = {network_stats.errin}, total sending errors = {network_stats.errout}, total dropped packets"
    f" = {network_stats.dropin + network_stats.dropout}"
)
