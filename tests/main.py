from functions import CreateUsers, CreateActivity

port = 5000
password = "test"

if __name__ == "__main__":
    users = CreateUsers(100, password=password, port=port)
    for i in range(3):
        CreateActivity(users, password=password, port=port)
