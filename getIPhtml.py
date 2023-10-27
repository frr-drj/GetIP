import requests

def get_html_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to retrieve the HTML content. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

def main():
    while True:
        website = input("Enter a website URL: ")
        html_content = get_html_content(website)

        if html_content.startswith("Failed"):
            print(html_content)
        else:
            with open("website.html", "w") as file:
                file.write(html_content)
                print("HTML content saved to 'website.html'.")

        choice = input("Do you want to restart (R) or exit (E)? ").strip().lower()

        if choice != 'r':
            break

if __name__ == "__main__":
    main()
          
