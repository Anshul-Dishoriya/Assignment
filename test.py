import requests

# =========================== Change the code as per Need =========================== #

# Defining the base URL
base_url = "http://localhost:8000/" 

# -----------------------------------------------------------------------------------#

# Function to test get request
def test_get_reminders():
    url = base_url + "reminder/"
    response = requests.get(url)
    print("GET /reminder/")
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
    print()

# -----------------------------------------------------------------------------------#

# Function to test get request by id
def test_get_reminder_by_id(pk):
    url = base_url + f"reminder/{pk}/"
    response = requests.get(url)
    print(f"GET /reminder/{pk}/")
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
    print()

# -----------------------------------------------------------------------------------#

# Function to test ge post request (to create reminder)
def test_create_reminder(data):
    url = base_url + "reminder/"
    response = requests.post(url, json=data)
    print("POST /reminder/")
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
    print()

# -----------------------------------------------------------------------------------#

# Function to test update request (to update the reminder by id)
def test_update_reminder(pk, data):
    url = base_url + f"reminder/{pk}/"
    response = requests.put(url, json=data)
    print(f"PUT /reminder/{pk}/")
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
    print()

# -----------------------------------------------------------------------------------#

# Function to test delete request (to delete remider by id)
def test_delete_reminder(pk):
    url = base_url + f"reminder/{pk}/"
    response = requests.delete(url)
    print(f"DELETE /reminder/{pk}/")
    print("Status Code:", response.status_code)
    print()

# -----------------------------------------------------------------------------------#
    
if __name__ == "__main__":
    # calling the function to test get all the reminders from database
    test_get_reminders()

    # calling the function to test get the reminder by ID from database
    test_get_reminder_by_id(1)  

    # calling the function to test Post/Create  the reminder in database
    reminder_data = {
        "date": "2024-03-25",
        "time": "14:30:00",
        "message": "Don't forget the team meeting at 2:30 PM"
    }
    test_create_reminder(reminder_data)

    # Debuging  
    test_get_reminders()

    # calling the function to test Put/Update the reminder in the database by id
    reminder_data = {
        "date": "2024-03-15",
        "time": "15:00:00",
        "message": "Updated meeting time to 3:00 PM"
    }
    test_update_reminder(1, reminder_data)

    #  Debuging
    test_get_reminders()
    
    # calling the function to test delete the reminder from database by id 
    test_delete_reminder(1)  
