import csv
import requests
from bs4 import BeautifulSoup

def scrape_asiri_hospital_labs():
    url = "https://www.asirihealth.com/laboratory-services/labs-directory-departments-location-finder/collection-centres/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    hospital_names = []

    # Find the hospital name elements on the page
    name_elements = soup.find_all("h4", class_="media-heading")

    # Extract the hospital names
    for name_element in name_elements:
        hospital_name = name_element.text.strip()
        hospital_names.append(hospital_name)

    return hospital_names

# Call the scraping function
hospital_names = scrape_asiri_hospital_labs()

# Export hospital names to a CSV file
filename = "asiri_hospital_labs.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Hospital Name"])
    writer.writerows([[name] for name in hospital_names])

print(f"Data exported to {filename} successfully.")
