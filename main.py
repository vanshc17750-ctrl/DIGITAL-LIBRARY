import requests

book_name = input("Enter book name: ").strip()
url = "https://openlibrary.org/search.json"
request_succesfull = False
try:
    response = requests.get(url, params={"q": book_name})
    response.raise_for_status()
    data = response.json()
    request_succesfull = True
except requests.RequestException:
    print("Internet ya API request mein problem hui.")
    

if request_succesfull:
    if data["docs"]:
        for number, item in enumerate (data["docs"][:5], start=1):
            print(f"{number}. {item.get("title")}")
            print("Author:", item.get("author_name"))
            print("First published:", item.get("first_publish_year"))
            print("Website link:", "https://openlibrary.org" + item.get("key", ""))
            print("Gutenberg ID:", item.get("id_project_gutenberg"))
            print()
            ids = item.get("id_project_gutenberg", [])

            if ids:
                print("Reading link:", f"https://www.gutenberg.org/ebooks/{ids[0]}")
            else:
                print("No Gutenberg link found.")
    else:
        print("No books found.")


