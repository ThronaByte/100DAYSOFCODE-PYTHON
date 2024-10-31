import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "thronabyte"
TOKEN = "jn239jd23d2udn2"
GRAPH_ID = "sex"

PIXEL_PARAMS = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}
# pixel = requests.post(url=PIXELA_ENDPOINT, json=PIXEL_PARAMS)
# print(pixel.text)

HEADER = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

cont = True
while cont:
    print("Choose an action:")
    print("1. Create a new graph")
    print("2. Add a new entry")
    print("3. Update an existing entry")
    print("4. Delete an entry")

    choice = input("Enter the number of your choice: ")

    today = datetime.now().strftime("%Y%m%d")

    if choice == "2":
        quantity = input("Entry Name? ")
        post_config = {
            "date": today,
            "quantity": quantity
        }
        post_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
        post = requests.post(url=post_endpoint, json=post_config, headers=HEADER)
        print(post.text)

    elif choice == "3":
        date_to_edit = input("Enter the date you want to edit (YYYYMMDD): ")
        quantity = input("How much needs to be edited? ")
        put_config = {
            "quantity": quantity
        }
        put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_edit}"
        put = requests.put(url=put_endpoint, json=put_config, headers=HEADER)
        print(put.text)

    elif choice == "4":
        date_to_delete = input("Enter the date you want to delete (YYYYMMDD): ")
        delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"
        delete = requests.delete(url=delete_endpoint, headers=HEADER)
        print(delete.text)

    elif choice == "1":
        print("Note: The graph ID must have alphabetical character first.")

        graph_id = input("Enter a new graph ID: ")
        graph_name = input("Enter a name for the graph: ")
        graph_unit = input("Enter the unit of measurement (e.g., Hour, commit, kilogram, calory): ")
        graph_type = input("Enter the data type (int or float): ")
        graph_color = input("Choose a color for the graph (e.g., shibafu (green), momiji (red), sora (blue), "
                            "ichou (yellow), ajisai (purple) and kuro (black)  ): ")

        graph_config = {
            "id": graph_id,
            "name": graph_name,
            "unit": graph_unit,
            "type": graph_type,
            "color": graph_color
        }

        response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADER)
        print(response.text)


    else:
        cont = False
        print("Invalid choice. Please restart the program and choose a valid option.")
        break
