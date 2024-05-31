from functions import CreateUsers, CreateActivity
import threading

port = 5000
password = "test"

if __name__ == "__main__":
    users = CreateUsers(100, password=password, port=port)

    print("[i] Starting threads...")
    threads = []
    for i in range(50):
        thread = threading.Thread(target=CreateActivity, args=(users, password, port))
        thread.start()
        threads.append(thread)
        print("[+] Thread", len(threads), "started")
        # CreateActivity(users, password=password, port=port)
    
    for thread in threads: thread.join()
