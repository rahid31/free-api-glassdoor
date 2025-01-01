import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# RAPID API Credentials
url = os.getenv("baseUrl")

params = {"companyId":"545277",
               "page":1
			}

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "x-rapidapi-host": os.getenv("RAPIDAPI_HOST")
}

# Empty dataframe to store data
all_data = []

# Fetching data
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    json_response = response.json()
    total_pages = json_response.get('data', []).get('employerReviewsRG', []).get('numberOfPages', [])
    print(f"Total pages available: {total_pages}")

# Fetching data, loop through all pages
for page in range(1, total_pages + 1):
	params['page'] = page 
	
	response = requests.get(url, headers=headers, params=params)
            
	if response.status_code == 200:
		data = response.json().get('data', []).get('employerReviewsRG', []).get('reviews', [])
		all_data.extend(data)
		print(f"Page {page} fetched successfully.")
	else:
		print(f"Error on page {page}: {response.status_code}")
else:
	print(f"Failed to fetch data: {response.status_code}")

# Converting data to dataframe
data = pd.DataFrame(all_data)
print(data)

# Save data to CSV
employer = json_response.get('data', []).get('employer', []).get('shortName', [])

folder_path = r'C:\Users\Admin\Desktop\Alvin\DE Bootcamp\API Testing\Glassdoor API\data'
os.makedirs(folder_path, exist_ok=True)
save_path = os.path.join(folder_path, f'{employer}_reviews.csv')

data.to_csv(save_path, index=False)

print(f"{employer} reviews data saved into {save_path}")