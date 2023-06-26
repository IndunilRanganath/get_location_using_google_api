import csv
import googlemaps

def get_hospital_location(hospital_name):
    api_key = 'API KYE'  # Replace with your actual API key
    gmaps = googlemaps.Client(key=api_key)

    geocode_result = gmaps.geocode(hospital_name + ", Sri Lanka")

    if len(geocode_result) > 0:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude

    return None

# Define a list of hospitals
hospitals = ["Asiri Collecting Centre - Kada 50, No 1, Bandaranayake Mawatha", "Asiri Collecting Centre - Kuliyapitiya No 95, Hettipola Road"]

# Create a list to store the hospital data
hospital_data = []

# Retrieve location data for each hospital
for hospital_name in hospitals:
    location = get_hospital_location(hospital_name)
    if location is not None:
        latitude, longitude = location
        hospital_data.append([hospital_name, latitude, longitude])
    else:
        hospital_data.append([hospital_name, None, None])

# Export data to a CSV file
filename = "hospital_locations.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Hospital Name", "Latitude", "Longitude"])
    writer.writerows(hospital_data)

print(f"Data exported to {filename} successfully.")
